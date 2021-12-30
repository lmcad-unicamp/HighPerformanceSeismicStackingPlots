import csv
import distutils.dir_util
import os

from pathlib import Path
from statistics import mean
from typing import Type, Dict
import subprocess

from model.execution_data import Implementation, Execution, AwsInstance, ExecutionData


class PersistenceHelpers:

    @staticmethod
    def create_directory(path_to_dir: str):
        Path(path_to_dir).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def path_exists(path: str):
        return Path(path).exists()

    @staticmethod
    def get_average_from_csv(csv_file: str):
        with open(csv_file) as file:
            reader = csv.reader(file, delimiter=',')
            return mean([float(row[1]) for row in reader])

    @staticmethod
    def get_dir_name(filename: str, is_spit_exec: bool = False) -> str:
        if is_spit_exec:
            job_manager_split = filename.split('jobmanager')
            if len(job_manager_split) > 1:
                return job_manager_split[0]

            return filename.split('logs')[0]

        return os.path.dirname(filename)

    @staticmethod
    def test_all_decimal_cases_up_to(max_dec_cases: int, content: str, int_per_sec: float):
        if int_per_sec is None:
            return False

        for dec_case in range(1, max_dec_cases + 1):
            format_flag = '{:.' + str(dec_case) + 'e}'
            if format_flag.format(int_per_sec) in content:
                return True

        return False

    @staticmethod
    def grep_log_for_data_in_folder(folder:str, int_per_sec: float = None, exec_time: float = None, tail_file: bool = False) -> str:
        for root, dir_names, filenames in os.walk(folder):
            for filename in filenames:
                if not filename.endswith(('.out', '.log')):
                    continue

                path = os.path.join(root, filename)
                try:
                    with open(path, 'rb') as file:
                        content = file.read().decode(errors='replace')
                        is_int_per_sec_in_file = PersistenceHelpers.test_all_decimal_cases_up_to(
                            max_dec_cases=5, content=content, int_per_sec=int_per_sec)
                        is_exec_time_in_file = exec_time is not None and "{}".format(exec_time) in content
                        if is_int_per_sec_in_file or is_exec_time_in_file:
                            if tail_file:
                                proc = subprocess.Popen(['tail', '-n', '20', path])
                                proc.communicate()
                            return path
                except UnicodeDecodeError as e:
                    print('Exception {} while reading {}. Skipping.'.format(e, path))


        raise RuntimeError("No file found")

    @staticmethod
    def search_for_execution_data(search_folder:str,
                                  result_folder:str,
                                  exec_class: Type[Execution],
                                  impl: Implementation,
                                  copy: bool = True):
        not_found_list = []
        instances: Dict[AwsInstance, ExecutionData] = exec_class.executions(impl)
        for instance, execution in instances.items():
            exec_times = execution.total_execution_time if execution.total_execution_time is not None else execution.kernel_execution_time

            copy_to_dirname = '{}_{}_{}_{}_{}_{}_{}'.format(instance.name.upper().replace(' ', '_'),
                                                            instance.node_count,
                                                            impl.impl_id,
                                                            impl.platform,
                                                            exec_class.data_name(),
                                                            exec_class.model(),
                                                            exec_class.compute_method())

            print('---------------')
            print(copy_to_dirname)
            print('---------------')

            for test_number, (int_per_sec, exec_time) in enumerate(zip(execution.int_per_second, exec_times)):
                try:
                    print("Looking for {} and {} ({} nodes, {})".format(exec_class.data_name(),
                                                                        instance.name,
                                                                        instance.node_count,
                                                                        exec_class.compute_method()))

                    copy_to_test_dirname = '{}/{}/{}'.format(result_folder, copy_to_dirname, test_number + 1)

                    if PersistenceHelpers.path_exists(path=copy_to_test_dirname):
                        print('{} already exists. Skipping'.format(copy_to_test_dirname))
                        continue

                    filename = PersistenceHelpers.grep_log_for_data_in_folder(
                        folder=search_folder, int_per_sec=int_per_sec, exec_time=exec_time)

                    dirname = PersistenceHelpers.get_dir_name(
                        filename=filename, is_spit_exec=not exec_class.is_single_node_exec())

                    print("Copying {} to {}".format(dirname, copy_to_test_dirname))

                    if copy:
                        PersistenceHelpers.create_directory(path_to_dir=copy_to_test_dirname)
                        distutils.dir_util.copy_tree(src=dirname, dst=copy_to_test_dirname, update=True)

                except RuntimeError as e:
                    print("Exception caught: {}".format(e))
                    not_found_list.append((instance.name, instance.node_count, impl.impl_id, int_per_sec, exec_time))

        print('Summary for {} {} {} {}'.format(
            exec_class.data_name(), exec_class.model(), exec_class.compute_method(), impl.impl_id))
        print('--------------------')
        print('+ Could not find result file for ', not_found_list)


