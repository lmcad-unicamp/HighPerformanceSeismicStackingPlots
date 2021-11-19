from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from model.execution_data import ExecutionData, AwsInstance, ExecutionBreakDownData, Execution, Implementation, \
    Implementations, Instances
from helpers.plot_helpers import PlotHelpers
from model.plot_model import LOCALE


class Fold2000CommonMidpointGreedy(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V11: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='v1.1',
                int_per_second=[1.64E+10]
            ),
        },
        Implementations.GIMENES_ET_AL: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[4.81E+10, 4.43E+10, 4.47E+10, 4.45E+10, 4.44E+10, 4.44E+10,
                                4.43E+10, 4.45E+10, 4.43E+10, 4.43E+10],
                total_execution_time=None,
                kernel_execution_time=[43.980403, 47.660188, 47.231901, 47.501007, 47.633301, 47.60013,
                                       47.743768, 47.700471, 47.730187, 47.750897]
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[1.73E+11, 1.76E+11, 1.77E+11],
                total_execution_time=None,
                kernel_execution_time=[12.191952, 11.985501, 11.928525],
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[4.34E+11, 4.35E+11, 4.34E+11],
                total_execution_time=None,
                kernel_execution_time=[4.865091, 4.849345, 4.855813],
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour
            )
        },
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='c51bf56ee',
                int_per_second=[4.79E+10, 4.64E+10, 4.45E+10, 4.41E+10, 4.41E+10],
                total_execution_time=[43.84, 45.2776, 47.2752, 47.6452, 47.68045],
                kernel_execution_time=[43.84, 45.2776, 47.2752, 47.6452, 47.68045]
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[1.57E+11, 1.56E+11, 1.61E+11, 1.62E+11],
                total_execution_time=[18.7215, 18.7238, 18.5588, 18.5049],
                kernel_execution_time=[i * 400 for i in [0.033636, 0.0336774, 0.0327756, 0.0326115]],
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.56E+11, 1.55E+11, 1.56E+11, 1.55E+11, 1.55E+11],
                total_execution_time=[6.43283, 6.42951, 6.45396],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[3.26E+10, 3.23E+10, 3.23E+10, 3.23E+10, 3.23E+10],
                total_execution_time=[74.5289, 74.4988, 74.4788, 74.5148],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[3.31E+10, 3.30E+10, 3.30E+10, 3.29E+10, 3.35E+10],
                total_execution_time=[12.2269, 12.1862, 12.2584, 11.9615],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[3.32E+10, 3.31E+10, 3.31E+10, 3.37E+10, 3.35E+10],
                total_execution_time=[11.719, 11.699, 11.2473, 10.9227],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='55766d4e2ff',
                int_per_second=[4.30E+11, 4.30E+11, 4.30E+11],
                total_execution_time=[12.8569, 10.9201, 10.7768],
                kernel_execution_time=[i * 400 for i in [0.0122197, 0.0122168, 0.012213]],
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='55766d4e2ff',
                int_per_second=[4.25E+11, 4.24E+11, 4.31E+11],
                total_execution_time=[5.40737, 5.29438],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour
            ),
        }
    }

    BREAKDOWN_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionBreakDownData]] = {
        Implementations.SOLUTION_V20: {
            Instances.P2_X_LARGE: ExecutionBreakDownData(
                read_data=1.95,
                write_data=0.28,
                init_gpus=0.04,
                compute_sembl=86.63,
                copy_buffer=0.14
            ),
            Instances.P2_8X_LARGE: ExecutionBreakDownData(
                read_data=1.82,
                write_data=0.27,
                init_gpus=0.32,
                compute_sembl=11.11,
                copy_buffer=1.42
            ),
            Instances.P2_16X_LARGE: ExecutionBreakDownData(
                read_data=1.90,
                write_data=0.26,
                init_gpus=1.00,
                compute_sembl=6.54,
                copy_buffer=3.68
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return 'greedy'

    @staticmethod
    def data_name() -> str:
        return 'fold2000'

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = Fold2000CommonMidpointGreedy.EXECUTION_DATA[impl]
        return __impl.get(instance)

    @staticmethod
    def model() -> str:
        return 'cmp'

    @staticmethod
    def execution_breakdown(instance: AwsInstance, impl: Implementation) -> ExecutionBreakDownData:
        impl = Fold2000CommonMidpointGreedy.BREAKDOWN_DATA[impl]
        return impl[instance]

    @staticmethod
    def plot_v11_gimenes_et_al():
        instances: List[AwsInstance] = [Instances.GTX_TITAN]
        implementations: List[Implementation] = [Implementations.SOLUTION_V11, Implementations.GIMENES_ET_AL]

        GraphHelpers.plot_interpolations_per_sec_with_relative_performance(instances=instances,
                                                                           implementations=implementations,
                                                                           exec_type=Fold2000CommonMidpointGreedy,
                                                                           reference_impl=Implementations.GIMENES_ET_AL)

    @staticmethod
    def plot_v11_v20_gimenes_et_al():
        instances: List[AwsInstance] = [Instances.GTX_TITAN]
        implementations: List[Implementation] = \
            [Implementations.SOLUTION_V11, Implementations.GIMENES_ET_AL, Implementations.SOLUTION_V20]

        GraphHelpers.plot_interpolations_per_sec_with_relative_performance(instances=instances,
                                                                           implementations=implementations,
                                                                           exec_type=Fold2000CommonMidpointGreedy,
                                                                           reference_impl=Implementations.GIMENES_ET_AL)

    @staticmethod
    def plot_v20_gimenes_et_all_int_per_sec_total_exec_time_and_relative_perf():
        instances: List[AwsInstance] = [
            Instances.GTX_TITAN,
            Instances.G4DN_X_LARGE,
            Instances.P3_2X_LARGE
        ]

        implementations: List[Implementation] = [
            Implementations.GIMENES_ET_AL,
            Implementations.SOLUTION_V20
        ]

        GraphHelpers.plot_v20_gimenes_et_all_int_per_sec_total_exec_time_and_relative_perf(instances=instances,
                                                                                           implementations=implementations,
                                                                                           exec_type=Fold2000CommonMidpointGreedy,
                                                                                           our_impl=Implementations.SOLUTION_V20,
                                                                                           reference_impl=Implementations.GIMENES_ET_AL)

    @staticmethod
    def plot_interpolation_per_sec_and_exec_time():
        instances: List[AwsInstance] = [
            Instances.GTX_TITAN,
            Instances.G4DN_X_LARGE,
            Instances.G4DN_12X_LARGE,
            Instances.P2_X_LARGE,
            Instances.P2_8X_LARGE,
            Instances.P2_16X_LARGE,
            Instances.P3_2X_LARGE,
            Instances.P3_8X_LARGE
        ]

        GraphHelpers.plot_interpolation_per_sec_and_exec_time(instances=instances,
                                                              exec_type=Fold2000CommonMidpointGreedy,
                                                              impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_breakdown_bar():
        filename = 'images/breakdown_cmp_fold2000_greedy_cuda_{}.svg'.format(LOCALE)

        instances: List[AwsInstance] = [
            Instances.P2_X_LARGE,
            Instances.P2_8X_LARGE,
            Instances.P2_16X_LARGE
        ]

        implementation = Implementations.SOLUTION_V20

        data_to_plot = {}

        for instance in instances:
            breakdown_data = Fold2000CommonMidpointGreedy.execution_breakdown(instance, implementation)
            data_to_plot[instance] = [
                breakdown_data.read_data_sec,
                breakdown_data.write_data_sec,
                breakdown_data.init_gpus_sec,
                breakdown_data.compute_semblance_sec,
                breakdown_data.copy_buffer_sec]

        labels = ['Leitura', 'Escrita', 'Inicialização GPUs', 'Cálculo semblance', 'Cópia de dados']

        PlotHelpers.plot_execution_breakdown_stacked_bar(data_to_plot, labels=labels, filename_to_save=filename)

    @staticmethod
    def plot_all():
        Fold2000CommonMidpointGreedy.plot_v11_gimenes_et_al()
        Fold2000CommonMidpointGreedy.plot_v11_v20_gimenes_et_al()
        Fold2000CommonMidpointGreedy.plot_interpolation_per_sec_and_exec_time()
        Fold2000CommonMidpointGreedy.plot_v20_gimenes_et_all_int_per_sec_total_exec_time_and_relative_perf()
