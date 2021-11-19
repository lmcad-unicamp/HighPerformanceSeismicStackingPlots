from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementations, Instances, Implementation


class Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[2.49E+10, 2.48E+10, 2.48E+10, 2.47E+10, 2.48E+10, 2.48E+10,
                                2.48E+10, 2.48E+10, 2.48E+10, 2.47E+10],
                total_execution_time=[1125.4, 1127.98, 1128.05, 1130.71, 1127.7,
                                      1128.24, 1129, 1127.68, 1127.67, 1130.28],
                kernel_execution_time=None
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[9.81E+10, 9.75E+10, 9.61E+10],
                total_execution_time=[302.653, 304.153, 308.875],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[9.91E+10, 9.88E+10, 9.93E+10],
                total_execution_time=[79.0068, 78.7935],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[2.09E+10, 2.09E+10, 2.08E+10],
                total_execution_time=[1353.15, 1353.96, 1356.03],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[2.06E+10, 2.06E+10, 2.06E+10, 2.07E+10, 2.06E+10],
                total_execution_time=[175, 174.883, 174.788, 183.838, 175.203],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[2.02E+10, 2.02E+10, 2.02E+10, 2.04E+10, 2.02E+10],
                total_execution_time=[95.5458, 9.52E+01, 95.595, 94.3661, 95.0995],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[2.41E+11, 2.41E+11, 2.41E+11],
                total_execution_time=[146.09, 145.925, 146.223],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[2.41E+11, 2.41E+11, 2.41E+11, 2.41E+11, 2.41E+11],
                total_execution_time=[39.2768, 39.3147, 39.1467, 39.3105, 39.169],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour
            ),
        },
        Implementations.SOLUTION_V20_OPENCL: {
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[9.63E+10, 9.63E+10, 9.63E+10],
                total_execution_time=[330.067, 329.716, 329.243],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[9.87E+10, 9.77E+10, 9.59E+10],
                total_execution_time=[82.6546, 83.1637, 84.5985],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.03E+10, 2.05E+10, 2.03E+10],
                total_execution_time=[1435.67, 1429.39, 1441.27],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.05E+10, 2.05E+10, 2.05E+10],
                total_execution_time=[182.068, 182.015, 181.887],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.05E+10, 2.04E+10, 2.04E+10],
                total_execution_time=[98.0128, 98.5791, 98.2478],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.41E+11, 2.41E+11, 2.41E+11],
                total_execution_time=[188.678, 187.959, 187.958],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.41E+11, 2.41E+11, 2.41E+11],
                total_execution_time=[51.2641, 50.9236, 50.9502],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return 'de'

    @staticmethod
    def data_name() -> str:
        return 'fold2000'

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution.EXECUTION_DATA[impl]
        return __impl.get(instance)

    @staticmethod
    def model() -> str:
        return 'zocrs'

    @staticmethod
    def plot_exec_time():
        instances: List[AwsInstance] = [
            Instances.G4DN_X_LARGE,
            Instances.G4DN_12X_LARGE,
            Instances.P2_X_LARGE,
            Instances.P2_8X_LARGE,
            Instances.P2_16X_LARGE,
            Instances.P3_2X_LARGE,
            Instances.P3_8X_LARGE
        ]

        GraphHelpers.plot_exec_time(instances=instances,
                                    exec_type=Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution,
                                    impl=Implementations.SOLUTION_V20)

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

        implementation = Implementations.SOLUTION_V20

        GraphHelpers.plot_interpolation_per_sec_and_exec_time(instances=instances,
                                                              exec_type=Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution,
                                                              impl=implementation)

    @staticmethod
    def plot_interpolation_per_sec_and_exec_time_cuda_opencl():
        instances: List[AwsInstance] = [
            Instances.G4DN_X_LARGE,
            Instances.G4DN_12X_LARGE,
            Instances.P2_X_LARGE,
            Instances.P2_8X_LARGE,
            Instances.P2_16X_LARGE,
            Instances.P3_2X_LARGE,
            Instances.P3_8X_LARGE
        ]

        GraphHelpers.plot_interpolation_per_sec_and_exec_time_cuda_opencl(
            instances=instances, exec_type=Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution)

    @staticmethod
    def plot_all():
        Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution.plot_exec_time()
        Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution.\
            plot_interpolation_per_sec_and_exec_time_cuda_opencl()
        Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution.\
            plot_interpolation_per_sec_and_exec_time()
