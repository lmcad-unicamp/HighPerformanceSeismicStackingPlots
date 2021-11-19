from pathlib import Path
from statistics import mean, stdev
from typing import Dict, List, Type

from helpers.plot_helpers import PlotHelpers
from model.execution_data import Execution, AwsInstance, Implementation, Implementations, DummyExecution
from model.plot_model import LOCALE


class GraphHelpers:

    @staticmethod
    def create_directory(path_to_dir: str):
        Path(path_to_dir).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def build_int_per_sec_relative_perf_data(instance: AwsInstance,
                                             implementations: List[Implementation],
                                             exec_type: Type[Execution],
                                             reference_int_per_sec: float) -> Dict[str, List[float]]:

        data_to_plot: Dict[str, List[float]] = {
            PlotHelpers.INTERPOLATION_PER_SEC_KEY: [],
            PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY: [],
            PlotHelpers.RELATIVE_PERF_KEY: []
        }

        for impl in implementations:
            __exec = exec_type.execution(instance, impl)
            data_to_plot[PlotHelpers.INTERPOLATION_PER_SEC_KEY].append(__exec.avg_int_per_second)
            data_to_plot[PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY].append(__exec.std_dev_int_per_second)
            data_to_plot[PlotHelpers.RELATIVE_PERF_KEY].append(__exec.relative_int_per_second(reference_int_per_sec))

        return data_to_plot

    @staticmethod
    def plot_interpolations_per_sec_with_relative_performance(instances: List[AwsInstance],
                                                              implementations: List[Implementation],
                                                              exec_type: Type[Execution],
                                                              reference_impl: Implementation):

        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, exec_type.model())

        GraphHelpers.create_directory(folder)

        for instance in instances:
            prefix = ''.join(['{}_'.format(impl.impl_id) for impl in implementations])

            filename = '{}/{}{}_{}_{}_{}_{}.svg'.format(folder,
                                                        prefix,
                                                        exec_type.data_name(),
                                                        exec_type.model(),
                                                        exec_type.compute_method(),
                                                        reference_impl.platform,
                                                        LOCALE)

            reference_int_per_sec = exec_type.execution(instance, reference_impl).avg_int_per_second

            data_to_plot = GraphHelpers.build_int_per_sec_relative_perf_data(instance=instance,
                                                                             implementations=implementations,
                                                                             exec_type=exec_type,
                                                                             reference_int_per_sec=reference_int_per_sec)

            PlotHelpers.plot_interpolations_per_sec_with_relative_performance(implementations=implementations,
                                                                              data_to_plot=data_to_plot,
                                                                              filename_to_save=filename,
                                                                              annotate=True,
                                                                              show=False)

    @staticmethod
    def plot_v20_gimenes_et_all_int_per_sec_total_exec_time_and_relative_perf(instances: List[AwsInstance],
                                                                              implementations: List[Implementation],
                                                                              exec_type: Type[Execution],
                                                                              our_impl: Implementation,
                                                                              reference_impl: Implementation):
        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, exec_type.model())

        GraphHelpers.create_directory(folder)

        filename_total_exec_time_and_relative_perf = '{}/compare_time_{}_{}_{}_{}_{}.svg'.format(
            folder, exec_type.model(), exec_type.data_name(), exec_type.compute_method(),
            implementations[0].platform, LOCALE)

        filename_int_per_sec = '{}/compare_inter_sec_{}_{}_{}_{}_{}.svg'.format(
            folder, exec_type.model(), exec_type.data_name(), exec_type.compute_method(),
            implementations[0].platform, LOCALE)

        data_to_plot: Dict[AwsInstance, Dict[Implementation, Dict[str, float]]] = {}

        for instance in instances:
            data_to_plot[instance] = {}

            for implementation in implementations:
                execution = exec_type.execution(instance, implementation) or \
                            DummyExecution().execution(instance, implementation)
                ref_execution = exec_type.execution(instance, reference_impl)

                data_to_plot[instance][implementation] = {
                    PlotHelpers.INTERPOLATION_PER_SEC_KEY: execution.avg_int_per_second,
                    PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY: execution.std_dev_int_per_second,
                    PlotHelpers.KERNEL_EXEC_TIME_KEY: execution.avg_kernel_execution_time,
                    PlotHelpers.KERNEL_EXEC_TIME_STD_DEV_KEY: execution.std_kernel_execution_time,
                    PlotHelpers.RELATIVE_PERF_KEY: execution.relative_kernel_execution_time(
                        ref_execution.avg_kernel_execution_time)
                }

        PlotHelpers.plot_interpolation_per_sec(instances=instances,
                                               data_to_plot=data_to_plot,
                                               implementations=implementations,
                                               filename_to_save=filename_int_per_sec,
                                               annotate=True,
                                               show=False)

        PlotHelpers.plot_execution_time_with_relative_performance(instances=instances,
                                                                  data_to_plot=data_to_plot,
                                                                  implementations=implementations,
                                                                  our_impl=our_impl,
                                                                  filename_to_save=filename_total_exec_time_and_relative_perf,
                                                                  annotate=True,
                                                                  show=False)

    @staticmethod
    def plot_exec_time(instances: List[AwsInstance],
                       exec_type: Type[Execution],
                       impl: Implementation):

        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, exec_type.model())

        GraphHelpers.create_directory(folder)

        filename = '{}/exec_time_{}_{}_{}_{}_{}.svg'.format(
            folder, exec_type.model(), exec_type.data_name(), exec_type.compute_method(),
            impl.platform, LOCALE)

        data_to_plot: Dict[AwsInstance, Dict[str, float]] = {}

        for instance in instances:
            execution = exec_type.execution(instance, impl)
            data_to_plot[instance] = {
                PlotHelpers.EXEC_TIME_KEY: execution.avg_total_execution_time,
                PlotHelpers.EXEC_TIME_STD_DEV_KEY: execution.std_dev_total_execution_time
            }

        PlotHelpers.plot_exec_time(data_map=data_to_plot, filename_to_save=filename, annotate=True, show=False)

    @staticmethod
    def plot_interpolation_per_sec_and_exec_time(instances: List[AwsInstance],
                                                 exec_type: Type[Execution],
                                                 impl: Implementation):

        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, exec_type.model())

        GraphHelpers.create_directory(folder)

        filename = '{}/all_{}_{}_{}_{}_{}.svg'.format(
            folder, exec_type.model(), exec_type.data_name(), exec_type.compute_method(),
            impl.platform, LOCALE)

        data_to_plot: Dict[AwsInstance, Dict[str, float]] = {}

        for instance in instances:
            execution = exec_type.execution(instance, impl)

            data_to_plot[instance] = {
                PlotHelpers.INTERPOLATION_PER_SEC_KEY: execution.avg_int_per_second,
                PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY: execution.std_dev_int_per_second,
                PlotHelpers.EXEC_TIME_KEY: execution.avg_total_execution_time,
                PlotHelpers.EXEC_TIME_STD_DEV_KEY: execution.std_dev_total_execution_time
            }

        PlotHelpers.plot_interpolation_per_sec_and_total_exec_time(data_map=data_to_plot,
                                                                   filename_to_save=filename,
                                                                   annotate=True,
                                                                   show=False)

    @staticmethod
    def plot_interpolation_per_sec_and_exec_time_cuda_opencl(instances: List[AwsInstance],
                                                             exec_type: Type[Execution]):

        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, exec_type.model())

        GraphHelpers.create_directory(folder)

        suffix = '{}_{}_{}'.format(exec_type.data_name(), exec_type.model(), exec_type.compute_method())

        filename = '{}/all_int_per_sec_{}_cuda_opencl_{}.svg'.format(folder, suffix, LOCALE)
        filename_exec = '{}/all_exec_time_{}_cuda_opencl_{}.svg'.format(folder, suffix, LOCALE)

        data_to_plot_cuda: Dict[AwsInstance, Dict[str, float]] = {}
        data_to_plot_opencl: Dict[AwsInstance, Dict[str, float]] = {}

        for instance in instances:
            cuda_execution = exec_type.execution(instance, Implementations.SOLUTION_V20)
            opencl_execution = exec_type.execution(instance, Implementations.SOLUTION_V20_OPENCL)

            data_to_plot_cuda[instance] = {
                PlotHelpers.INTERPOLATION_PER_SEC_KEY: cuda_execution.avg_int_per_second,
                PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY: cuda_execution.std_dev_int_per_second,
                PlotHelpers.EXEC_TIME_KEY: cuda_execution.avg_total_execution_time,
                PlotHelpers.EXEC_TIME_STD_DEV_KEY: cuda_execution.std_dev_total_execution_time
            }

            data_to_plot_opencl[instance] = {
                PlotHelpers.INTERPOLATION_PER_SEC_KEY: opencl_execution.avg_int_per_second,
                PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY: opencl_execution.std_dev_int_per_second,
                PlotHelpers.EXEC_TIME_KEY: opencl_execution.avg_total_execution_time,
                PlotHelpers.EXEC_TIME_STD_DEV_KEY: opencl_execution.std_dev_total_execution_time
            }

        PlotHelpers.plot_interpolation_per_sec_cuda_opencl(data_to_plot_cuda=data_to_plot_cuda,
                                                           data_to_plot_opencl=data_to_plot_opencl,
                                                           filename_to_save=filename,
                                                           annotate=True,
                                                           show=False)

        PlotHelpers.plot_total_execution_time_cuda_opencl(data_to_plot_cuda=data_to_plot_cuda,
                                                          data_to_plot_opencl=data_to_plot_opencl,
                                                          filename_to_save=filename_exec,
                                                          annotate=True,
                                                          show=False)

    @staticmethod
    def plot_cost_and_exec_time(instance_families: Dict[str, List[AwsInstance]],
                                spits_class: Type[Execution],
                                impl: Implementation,
                                print_data=False):

        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, spits_class.model())

        GraphHelpers.create_directory(folder)

        suffix = '{}_{}_{}_{}'.format(
            spits_class.data_name(), spits_class.model(), spits_class.compute_method(), impl.platform)

        for instance_family, instances in instance_families.items():
            ref_execution_time = spits_class.execution(instances[0], impl).total_execution_time

            data_to_plot: Dict[AwsInstance, Dict[str, float]] = {}

            for instance in instances:
                execution = spits_class.execution(instance, impl)

                data_to_plot[instance] = {
                    PlotHelpers.EXEC_TIME_KEY: execution.avg_total_execution_time,
                    PlotHelpers.EXEC_TIME_STD_DEV_KEY: execution.std_dev_total_execution_time,
                    PlotHelpers.COST_KEY: execution.avg_cost,
                    PlotHelpers.COST_STD_DEV_KEY: execution.std_dev_cost,
                    PlotHelpers.RELATIVE_PERF_KEY: execution.avg_relative_total_execution_time(ref_execution_time),
                    PlotHelpers.RELATIVE_PERF_STD_DEV_KEY:
                        execution.std_dev_relative_total_execution_time(ref_execution_time)
                }

            if print_data:
                print(data_to_plot)

            filename_cost = '{}/cost_{}_{}_{}.svg'.format(folder, suffix, instance_family, LOCALE)
            filename_relative_perf = '{}/rate_{}_{}_{}.svg'.format(folder, suffix, instance_family, LOCALE)

            PlotHelpers.plot_cost_with_total_exec_time(
                data_to_plot=data_to_plot,
                filename_to_save=filename_cost,
                show=False)

            PlotHelpers.plot_relative_performance(
                data_to_plot=data_to_plot,
                filename_to_save=filename_relative_perf,
                show=False)

    @staticmethod
    def plot_execution_times_greedy_and_de(instances: List[AwsInstance],
                                           de_exec_type: Type[Execution],
                                           greedy_exec_type: Type[Execution],
                                           impl: Implementation):

        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, de_exec_type.model())

        GraphHelpers.create_directory(folder)

        filename = '{}/{}_{}_greedy_de_{}_{}.svg'.format(
            folder, de_exec_type.data_name(), de_exec_type.model(), impl.platform, LOCALE)

        instance_names: List[str] = []
        de_exec_times: List[float] = []
        de_exec_time_std_devs: List[float] = []
        greedy_exec_times: List[float] = []
        greedy_exec_time_std_devs: List[float] = []

        for instance in instances:
            instance_names.append(instance.name)

            de_exec_times.append(de_exec_type.execution(instance, impl).avg_total_execution_time)
            de_exec_time_std_devs.append(de_exec_type.execution(instance, impl).std_dev_total_execution_time)
            greedy_exec_times.append(greedy_exec_type.execution(instance, impl).avg_total_execution_time)
            greedy_exec_time_std_devs.append(greedy_exec_type.execution(instance, impl).std_dev_total_execution_time)

        PlotHelpers.plot_exec_time_de_greedy(instance_names=instance_names,
                                             de_exec_times=de_exec_times,
                                             de_exec_time_std_devs=de_exec_time_std_devs,
                                             greedy_exec_times=greedy_exec_times,
                                             greedy_exec_time_std_devs=greedy_exec_time_std_devs,
                                             filename_to_save=filename,
                                             annotate=True,
                                             show=False)

    @staticmethod
    def plot_thread_benchmark_with_exec_time(thread_counts: List[str],
                                             execution_times: Dict[AwsInstance, List[List[float]]],
                                             data_name: str,
                                             model: str,
                                             compute_method: str,
                                             platform: str):
        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, 'thread_benchmark')

        GraphHelpers.create_directory(folder)

        filename = '{}/{}_{}_{}_{}_{}.svg'.format(
            folder, data_name, model, compute_method, platform, LOCALE)

        execution_time_map: Dict[AwsInstance, Dict[str, List[float]]] = {}

        for instance, execution_time_list in execution_times.items():

            std_devs: List[float] = []
            for exec_times in execution_time_list:
                if len(exec_times) > 1:
                    std_devs.append(stdev(exec_times))
                else:
                    std_devs.append(0)

            execution_time_map[instance] = {
                PlotHelpers.EXEC_TIME_THREADS_KEY: [mean(exec_times) for exec_times in execution_time_list],
                PlotHelpers.EXEC_TIME_THREADS_STD_DEV_KEY: std_devs,
            }

        PlotHelpers.plot_thread_benchmark_with_exec_time(thread_counts=thread_counts,
                                                         execution_times=execution_time_map,
                                                         filename_to_save=filename,
                                                         show=False)
