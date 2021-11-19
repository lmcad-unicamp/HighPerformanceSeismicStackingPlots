from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from model.execution_data import ExecutionData, AwsInstance, Implementation, Execution, Instances, Implementations


class Fold2000ZeroOffsetCommonReflectionSurfaceGreedy(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V11: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='v1.1',
                int_per_second=[1.11E+10]
            ),
        },
        Implementations.GIMENES_ET_AL: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[2.72E+10, 2.71E+10, 2.72E+10, 2.72E+10, 2.72E+10, 2.72E+10,
                                2.72E+10, 2.72E+10, 2.72E+10, 2.72E+10],
                total_execution_time=None,
                kernel_execution_time=[9782.450775, 9790.14006, 9782.21726, 9785.034084, 9783.620394,
                                       9783.708131, 9784.093818, 9782.610032, 9783.97814, 9783.043019]
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[7.19E+10, 7.13E+10, 7.14E+10],
                total_execution_time=None,
                kernel_execution_time=[3695.282128, 3726.524154, 3719.729008],
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[1.16E+11, 1.17E+11, 1.16E+11],
                total_execution_time=None,
                kernel_execution_time=[2283.372247, 2279.603516, 2282.022087],
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour
            )
        },
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[3.98E+10, 3.98E+10, 3.97E+10, 3.97E+10, 3.97E+10,
                                3.98E+10, 3.98E+10, 3.98E+10, 3.97E+10, 3.98E+10],
                total_execution_time=[6711.92, 6712.52, 6713.85, 6713.54, 6715.21,
                                      6711.07, 6711.32, 6711.71, 6713.6, 6712.32],
                kernel_execution_time=[6711.92, 6712.52, 6713.85, 6713.54, 6715.21,
                                       6711.07, 6711.32, 6711.71, 6713.6, 6712.32]
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[8.88E+10, 8.99E+10, 9.42E+10],
                total_execution_time=[3029.49, 2986.53, 2887.13],
                kernel_execution_time=[i * 400 for i in [7.4907, 7.38324, 7.05585]],
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[9.48E+10, 9.11E+10, 9.09E+10],
                total_execution_time=[717.705, 742.513, 745.666],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[3.04E+10],
                total_execution_time=[8802.8],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[2.94E+10, 2.92E+10, 2.93E+10],
                total_execution_time=[1170.77, 1171.38, 1168.84],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[2.92E+10, 2.92E+10, 2.89E+10],
                total_execution_time=[587.633, 584.468, 592.761],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[1.75E+11, 1.75E+11],
                total_execution_time=[1559.42, 1557.98],
                kernel_execution_time=[i * 400 for i in [3.79346, 3.79013]],
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[1.77E+11, 1.77E+11, 1.77E+11],
                total_execution_time=[391.987, 392.297, 392.045],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour
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
        __impl = Fold2000ZeroOffsetCommonReflectionSurfaceGreedy.EXECUTION_DATA[impl]
        return __impl.get(instance)

    @staticmethod
    def model() -> str:
        return 'zocrs'

    @staticmethod
    def plot_v11_gimenes_et_al():
        instances: List[AwsInstance] = [Instances.GTX_TITAN]
        implementations: List[Implementation] = [Implementations.SOLUTION_V11, Implementations.GIMENES_ET_AL]

        GraphHelpers.plot_interpolations_per_sec_with_relative_performance(instances=instances,
                                                                           implementations=implementations,
                                                                           exec_type=Fold2000ZeroOffsetCommonReflectionSurfaceGreedy,
                                                                           reference_impl=Implementations.GIMENES_ET_AL)

    @staticmethod
    def plot_v11_v20_gimenes_et_al():
        instances: List[AwsInstance] = [Instances.GTX_TITAN]
        implementations: List[Implementation] = \
            [Implementations.SOLUTION_V11, Implementations.GIMENES_ET_AL, Implementations.SOLUTION_V20]

        GraphHelpers.plot_interpolations_per_sec_with_relative_performance(instances=instances,
                                                                           implementations=implementations,
                                                                           exec_type=Fold2000ZeroOffsetCommonReflectionSurfaceGreedy,
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
                                                              exec_type=Fold2000ZeroOffsetCommonReflectionSurfaceGreedy,
                                                              impl=Implementations.SOLUTION_V20)

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
                                                                                           exec_type=Fold2000ZeroOffsetCommonReflectionSurfaceGreedy,
                                                                                           our_impl=Implementations.SOLUTION_V20,
                                                                                           reference_impl=Implementations.GIMENES_ET_AL)

    @staticmethod
    def plot_all():
        Fold2000ZeroOffsetCommonReflectionSurfaceGreedy.plot_v11_gimenes_et_al()
        Fold2000ZeroOffsetCommonReflectionSurfaceGreedy.plot_v11_v20_gimenes_et_al()
        Fold2000ZeroOffsetCommonReflectionSurfaceGreedy. \
            plot_v20_gimenes_et_all_int_per_sec_total_exec_time_and_relative_perf()
        Fold2000ZeroOffsetCommonReflectionSurfaceGreedy.plot_interpolation_per_sec_and_exec_time()
