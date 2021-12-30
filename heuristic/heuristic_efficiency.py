import distutils.dir_util
import os

from typing import List, Tuple, Dict
from helpers.persistence_helpers import PersistenceHelpers
from helpers.plot_helpers import PlotHelpers
from model.execution_data import AwsInstance, HeuristicData, Instances, DataPath, DataSets, Models
from model.plot_model import LOCALE, Legends


class HeuristicEfficiency:

    EFFICIENCY_CSV_FILENAME = 'efficiency.csv'
    INT_PER_SEC_CSV_FILENAME = 'interpolation_per_sec.csv'
    DATA_SET = 'data_set'
    MODEL = 'model'
    LINK_TO_DATA = 'link_to_data'
    TREATMENTS = [Legends.HEURISTIC_OFF[LOCALE], Legends.HEURISTIC_ON[LOCALE]]

    SIMPLE_SYNTHETIC_CMP_DE_INT_PER_SEC = {
        DATA_SET: 'simple-synthetic',
        MODEL: Models.CMP,
        Instances.GTX_TITAN: {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(0.23, 7.30E+08),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(100, 1.56E+10)
        },
        LINK_TO_DATA:
            'https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_heuristics_efficiency_simple-synthetic_cmp'
    }

    FOLD_2000_CMP_DE_INT_PER_SEC = {
        DATA_SET: DataSets.FOLD2000,
        MODEL: Models.CMP,
        Instances.GTX_TITAN: {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(0.25, 3.42E+08),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(100, 1.86E+10)
        },
        LINK_TO_DATA:
            'https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_heuristics_efficiency_fold2000_cmp'
    }

    SIMPLE_SYNTHETIC_ZO_CRS_DE_INT_PER_SEC = {
        DATA_SET: 'simple-synthetic',
        MODEL: Models.ZOCRS,
        Instances.GTX_TITAN: {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(3.4, 6.24E+09),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(100, 1.38E+10)
        },
        LINK_TO_DATA:
            'https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_heuristics_efficiency_simple-synthetic_zocrs'
    }

    FOLD_2000_ZO_CRS_DE_INT_PER_SEC = {
        DATA_SET: DataSets.FOLD2000,
        MODEL: Models.ZOCRS,
        Instances.GTX_TITAN: {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(3.2, 3.43E+09),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(100, 1.54E+10)
        },
        LINK_TO_DATA:
            'https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_heuristics_efficiency_fold2000_zocrs'
    }

    SIMPLE_SYNTHETIC_OCT_DE_INT_PER_SEC = {
        DATA_SET: 'simple-synthetic',
        MODEL: Models.OCT,
        Instances.GTX_TITAN:  {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(3.4, 4.17E+09),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(38.5, 1.02E+10)
        },
        LINK_TO_DATA:
            'https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_heuristics_efficiency_simple-synthetic_oct'
    }

    FOLD_2000_OCT_DE_INT_PER_SEC = {
        DATA_SET: DataSets.FOLD2000,
        MODEL: Models.OCT,
        Instances.GTX_TITAN: {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(2.9, 1.87E+09),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(26.3, 6.08E+09)
        },
        LINK_TO_DATA:
            'https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_heuristics_efficiency_fold2000_oct'
    }

    EXECUTIONS = [
        SIMPLE_SYNTHETIC_CMP_DE_INT_PER_SEC,
        FOLD_2000_CMP_DE_INT_PER_SEC,
        SIMPLE_SYNTHETIC_ZO_CRS_DE_INT_PER_SEC,
        FOLD_2000_ZO_CRS_DE_INT_PER_SEC,
        SIMPLE_SYNTHETIC_OCT_DE_INT_PER_SEC,
        FOLD_2000_OCT_DE_INT_PER_SEC,
    ]

    @staticmethod
    def build_data_for_plotting(data_dict: dict) -> Tuple[List[float], List[float]]:
        int_per_sec = [
            HeuristicEfficiency.get_interpolations_per_sec(
                data_dict=data_dict,
                instance=Instances.GTX_TITAN,
                treatment=Legends.HEURISTIC_OFF[LOCALE]
            ),
            HeuristicEfficiency.get_interpolations_per_sec(
                data_dict=data_dict,
                instance=Instances.GTX_TITAN,
                treatment=Legends.HEURISTIC_ON[LOCALE]
            )
        ]

        trace_efficiency = [
            HeuristicEfficiency.get_trace_efficiency(
                data_dict=data_dict,
                instance=Instances.GTX_TITAN,
                treatment=Legends.HEURISTIC_OFF[LOCALE]
            ),
            HeuristicEfficiency.get_trace_efficiency(
                data_dict=data_dict,
                instance=Instances.GTX_TITAN,
                treatment=Legends.HEURISTIC_ON[LOCALE]
            )
        ]

        return int_per_sec, trace_efficiency

    @staticmethod
    def convert_new_model_to_old(new_model:str) -> str:
        new_to_old_map = {
            Models.CMP: 'cmp',
            Models.ZOCRS: 'crs',
            Models.OCT: 'crp',
        }
        return new_to_old_map.get(new_model)

    @staticmethod
    def get_data_set(data_dict: dict) -> str:
        return data_dict.get(HeuristicEfficiency.DATA_SET)

    @staticmethod
    def get_model(data_dict: dict) -> str:
        return data_dict.get(HeuristicEfficiency.MODEL)

    @staticmethod
    def get_interpolations_per_sec(data_dict: dict, instance: AwsInstance, treatment: str) -> float:
        return data_dict.get(instance).get(treatment).interpolations_per_sec

    @staticmethod
    def get_trace_efficiency(data_dict: dict, instance: AwsInstance, treatment: str) -> float:
        return data_dict.get(instance).get(treatment).trace_efficiency

    @staticmethod
    def plot_heuristic_efficiency(execution: Dict):
        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, 'heuristics')
        PersistenceHelpers.create_directory(folder)

        filename = '{}/heuristics_efficiency_{}_{}_de_cuda_{}.svg'.format(
            folder,
            HeuristicEfficiency.get_data_set(data_dict=execution),
            HeuristicEfficiency.get_model(data_dict=execution),
            LOCALE)

        int_per_sec, trace_efficiency = HeuristicEfficiency.build_data_for_plotting(data_dict=execution)

        PlotHelpers.plot_interpolations_per_sec_with_trace_use(
            HeuristicEfficiency.TREATMENTS, int_per_sec, trace_efficiency, filename)

    @staticmethod
    def plot_all():
        for execution in HeuristicEfficiency.EXECUTIONS:
            HeuristicEfficiency.plot_heuristic_efficiency(execution=execution)

    @staticmethod
    def check_for_average_efficiency_and_int_per_sec(
            folder:str, efficiency_target: float, int_per_sec_target: float, data_set: str, model: str) -> str:
        for root, dir_names, filenames in os.walk(folder):
            for filename in filenames:
                if 'ga' not in root \
                        or model not in root \
                        or data_set not in root \
                        or filename != HeuristicEfficiency.EFFICIENCY_CSV_FILENAME:
                    continue

                efficiency_path = os.path.join(root, filename)
                int_per_sec_file = os.path.join(root, HeuristicEfficiency.INT_PER_SEC_CSV_FILENAME)

                average_efficiency = 100 * PersistenceHelpers.get_average_from_csv(csv_file=efficiency_path)
                average_int_per_sec = PersistenceHelpers.get_average_from_csv(csv_file=int_per_sec_file)

                is_in_efficiency_range = 0.95 * efficiency_target <= average_efficiency <= 1.05 * efficiency_target
                is_in_int_per_sec_range = 0.95 * int_per_sec_target <= average_int_per_sec <= 1.05 * int_per_sec_target

                if is_in_efficiency_range and is_in_int_per_sec_range:
                    print(efficiency_target, average_efficiency)
                    print('{:.5e} {:.5e}'.format(int_per_sec_target, average_int_per_sec))
                    return efficiency_path

        raise RuntimeError("No file found")

    @staticmethod
    def search_for_execution_data(copy: bool = True):
        not_found_list = []

        for execution in HeuristicEfficiency.EXECUTIONS:
            for treatment in HeuristicEfficiency.TREATMENTS:
                trace_efficiency = HeuristicEfficiency.get_trace_efficiency(data_dict=execution,
                                                                            instance=Instances.GTX_TITAN,
                                                                            treatment=treatment)

                int_per_sec = HeuristicEfficiency.get_interpolations_per_sec(data_dict=execution,
                                                                             instance=Instances.GTX_TITAN,
                                                                             treatment=treatment)

                data_set = HeuristicEfficiency.get_data_set(data_dict=execution)
                model = HeuristicEfficiency.get_model(data_dict=execution)

                try:
                    print("Looking for {} and {} ({}, {})".format(treatment,
                                                                  Instances.GTX_TITAN.name,
                                                                  data_set,
                                                                  model))

                    copy_to_dirname = '{}/{}_{}_{}_{}/{}'.format(DataPath.GIT_DATA_DIR,
                                                                 Instances.GTX_TITAN.name.upper().replace(' ', '_'),
                                                                 'heuristics_efficiency',
                                                                 data_set,
                                                                 model,
                                                                 treatment.lower().replace(' ', '_'))

                    if PersistenceHelpers.path_exists(path=copy_to_dirname):
                        print('{} already exists. Skipping'.format(copy_to_dirname))
                        continue

                    filename = HeuristicEfficiency.check_for_average_efficiency_and_int_per_sec(
                        folder=DataPath.HEURISTIC_RAW_DATA_DIR,
                        efficiency_target=trace_efficiency,
                        int_per_sec_target=int_per_sec,
                        data_set=data_set,
                        model=HeuristicEfficiency.convert_new_model_to_old(new_model=model))

                    dirname = PersistenceHelpers.get_dir_name(filename=filename, is_spit_exec=False)

                    if copy:
                        print("Copying {} to {}".format(dirname, copy_to_dirname))
                        PersistenceHelpers.create_directory(path_to_dir=copy_to_dirname)
                        distutils.dir_util.copy_tree(src=dirname, dst=copy_to_dirname, update=True)

                except RuntimeError as e:
                    print("Exception caught: {}".format(e))
                    not_found_list.append((data_set, model, treatment))

        print('Summary for heuristic efficiency')
        print('--------------------------------')
        print('Could not find result file for {}', not_found_list)
