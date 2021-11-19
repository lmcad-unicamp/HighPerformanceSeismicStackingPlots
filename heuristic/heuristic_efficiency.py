from typing import List, Tuple
from helpers.graph_helpers import GraphHelpers
from helpers.plot_helpers import PlotHelpers
from model.execution_data import AwsInstance, HeuristicData, Instances
from model.plot_model import LOCALE, Legends


class HeuristicEfficiency:

    TREATMENTS = [Legends.HEURISTIC_OFF[LOCALE], Legends.HEURISTIC_ON[LOCALE]]

    SIMPLE_SYNTHETIC_CMP_GREEDY_INT_PER_SEC = {
        Instances.GTX_TITAN: {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(0.23, 7.30E+08),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(100, 1.56E+10)
        }
    }

    FOLD_2000_CMP_GREEDY_INT_PER_SEC = {
        Instances.GTX_TITAN: {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(0.25, 3.42E+08),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(100, 1.86E+10)
        }
    }

    SIMPLE_SYNTHETIC_ZO_CRS_GREEDY_INT_PER_SEC = {
        Instances.GTX_TITAN: {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(3.4, 6.24E+09),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(100, 1.38E+10)
        }
    }

    FOLD_2000_ZO_CRS_GREEDY_INT_PER_SEC = {
        Instances.GTX_TITAN: {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(3.2, 3.43E+09),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(100, 1.54E+10)
        }
    }

    SIMPLE_SYNTHETIC_OCT_GREEDY_INT_PER_SEC = {
        Instances.GTX_TITAN:  {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(3.4, 4.17E+09),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(38.5, 1.02E+10)
        }
    }

    FOLD_2000_OCT_GREEDY_INT_PER_SEC = {
        Instances.GTX_TITAN: {
            Legends.HEURISTIC_OFF[LOCALE]: HeuristicData(2.9, 1.87E+09),
            Legends.HEURISTIC_ON[LOCALE]: HeuristicData(26.3, 6.08E+09)
        }
    }

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
    def get_interpolations_per_sec(data_dict: dict, instance: AwsInstance, treatment: str) -> float:
        return data_dict.get(instance).get(treatment).interpolations_per_sec

    @staticmethod
    def get_trace_efficiency(data_dict: dict, instance: AwsInstance, treatment: str) -> float:
        return data_dict.get(instance).get(treatment).trace_efficiency

    @staticmethod
    def plot_heuristic_efficiency_simple_cmp_greedy():
        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, 'heuristics')
        GraphHelpers.create_directory(folder)

        filename = '{}/heuristics_efficiency_simple_CMP_de_cuda_{}.svg'.format(folder, LOCALE)
        int_per_sec, trace_efficiency = HeuristicEfficiency.build_data_for_plotting(
            HeuristicEfficiency.SIMPLE_SYNTHETIC_CMP_GREEDY_INT_PER_SEC)

        PlotHelpers.plot_interpolations_per_sec_with_trace_use(
            HeuristicEfficiency.TREATMENTS, int_per_sec, trace_efficiency, filename)

    @staticmethod
    def plot_heuristic_efficiency_fold2000_cmp_greedy():
        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, 'heuristics')
        GraphHelpers.create_directory(folder)

        filename = '{}/heuristics_efficiency_fold2000_CMP_de_cuda_{}.svg'.format(folder, LOCALE)
        int_per_sec, trace_efficiency = HeuristicEfficiency.build_data_for_plotting(
            HeuristicEfficiency.FOLD_2000_CMP_GREEDY_INT_PER_SEC)

        PlotHelpers.plot_interpolations_per_sec_with_trace_use(
            HeuristicEfficiency.TREATMENTS, int_per_sec, trace_efficiency, filename)

    @staticmethod
    def plot_heuristic_efficiency_simple_zo_crs_greedy():
        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, 'heuristics')
        GraphHelpers.create_directory(folder)

        filename = '{}/heuristics_efficiency_simple_ZOCRS_de_cuda_{}.svg'.format(folder, LOCALE)
        int_per_sec, trace_efficiency = HeuristicEfficiency.build_data_for_plotting(
            HeuristicEfficiency.SIMPLE_SYNTHETIC_ZO_CRS_GREEDY_INT_PER_SEC)

        PlotHelpers.plot_interpolations_per_sec_with_trace_use(
            HeuristicEfficiency.TREATMENTS, int_per_sec, trace_efficiency, filename)

    @staticmethod
    def plot_heuristic_efficiency_fold2000_zo_crs_greedy():
        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, 'heuristics')
        GraphHelpers.create_directory(folder)

        filename = '{}/heuristics_efficiency_fold2000_ZOCRS_de_cuda_{}.svg'.format(folder, LOCALE)
        int_per_sec, trace_efficiency = HeuristicEfficiency.build_data_for_plotting(
            HeuristicEfficiency.FOLD_2000_ZO_CRS_GREEDY_INT_PER_SEC)

        PlotHelpers.plot_interpolations_per_sec_with_trace_use(
            HeuristicEfficiency.TREATMENTS, int_per_sec, trace_efficiency, filename)

    @staticmethod
    def plot_heuristic_efficiency_simple_oct_greedy():
        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, 'heuristics')
        GraphHelpers.create_directory(folder)

        filename = '{}/heuristics_efficiency_simple_OCT_de_cuda_{}.svg'.format(folder, LOCALE)
        int_per_sec, trace_efficiency = HeuristicEfficiency.build_data_for_plotting(
            HeuristicEfficiency.SIMPLE_SYNTHETIC_OCT_GREEDY_INT_PER_SEC)

        PlotHelpers.plot_interpolations_per_sec_with_trace_use(
            HeuristicEfficiency.TREATMENTS, int_per_sec, trace_efficiency, filename)

    @staticmethod
    def plot_heuristic_efficiency_fold2000_oct_greedy():
        folder = '{}/{}'.format(PlotHelpers.ROOT_IMAGE_DIR, 'heuristics')
        GraphHelpers.create_directory(folder)

        filename = '{}/heuristics_efficiency_fold2000_OCT_de_cuda_{}.svg'.format(folder, LOCALE)
        int_per_sec, trace_efficiency = HeuristicEfficiency.build_data_for_plotting(
            HeuristicEfficiency.FOLD_2000_OCT_GREEDY_INT_PER_SEC)

        PlotHelpers.plot_interpolations_per_sec_with_trace_use(
            HeuristicEfficiency.TREATMENTS, int_per_sec, trace_efficiency, filename, True)

    @staticmethod
    def plot_all():
        HeuristicEfficiency.plot_heuristic_efficiency_simple_cmp_greedy()
        HeuristicEfficiency.plot_heuristic_efficiency_fold2000_cmp_greedy()
        HeuristicEfficiency.plot_heuristic_efficiency_simple_zo_crs_greedy()
        HeuristicEfficiency.plot_heuristic_efficiency_fold2000_zo_crs_greedy()
        HeuristicEfficiency.plot_heuristic_efficiency_simple_oct_greedy()
        HeuristicEfficiency.plot_heuristic_efficiency_fold2000_oct_greedy()
