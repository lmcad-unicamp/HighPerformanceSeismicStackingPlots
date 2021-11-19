from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementation, Instances, Implementations


class Fold2000OffsetContinuationTrajectoryDifferentialEvolution(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[1.15E+10, 1.13E+10, 1.13E+10, 1.13E+10, 1.13E+10, 1.13E+10,
                                1.13E+10, 1.13E+10, 1.13E+10, 1.13E+10],
                total_execution_time=[2355.27, 2386.61, 2383.97, 2385.08, 2383.56, 2384.54,
                                      2383.55, 2383.05, 2384.8, 2385.57],
                kernel_execution_time=None
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[3.04E+10, 3.03E+10, 3.03E+10],
                total_execution_time=[925.404, 927.988, 926.559],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[3.11E+10, 3.07E+10, 3.07E+10],
                total_execution_time=[230.414, 233.644, 233.756],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[8.39E+09, 8.42E+09],
                total_execution_time=[3249.85, 3241.94],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[8.76E+09, 8.69E+09, 8.72E+09],
                total_execution_time=[415.768, 417.272, 445.101],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[8.93E+09, 8.92E+09, 8.92E+09],
                total_execution_time=[201.762, 201.098, 202.004],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[4.09E+10, 4.09E+10, 4.09E+10],
                total_execution_time=[737.539, 735.717, 735.795],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[4.09E+10, 4.09E+10],
                total_execution_time=[190.466, 190.829],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour
            ),
        },
        Implementations.SOLUTION_V20_OPENCL: {
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.89E+10, 2.89E+10, 2.90E+10],
                total_execution_time=[1059.04, 1057.1, 1053.45],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.88E+10, 2.87E+10, 2.88E+10],
                total_execution_time=[268.724, 268.069, 267.735],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[8.45E+09, 8.3875e+09, 8.51969e+09],
                total_execution_time=[3432.95, 3472.76, 3415.58],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[8.37E+09, 8.37E+09, 8.37E+09],
                total_execution_time=[436.436, 436.025, 436.166],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[8.33E+09, 8.33E+09, 8.33E+09],
                total_execution_time=[229.754, 229.514, 229.526],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[3.81E+10, 3.81E+10, 3.81E+10],
                total_execution_time=[950.45, 949.307, 949.75],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[3.80E+10, 3.81E+10, 3.81E+10],
                total_execution_time=[246.613, 246.15, 245.985],
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
        __impl = Fold2000OffsetContinuationTrajectoryDifferentialEvolution.EXECUTION_DATA[impl]
        return __impl.get(instance)

    @staticmethod
    def model() -> str:
        return 'oct'

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
                                    exec_type=Fold2000OffsetContinuationTrajectoryDifferentialEvolution,
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
                                                              exec_type=Fold2000OffsetContinuationTrajectoryDifferentialEvolution,
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
            instances=instances, exec_type=Fold2000OffsetContinuationTrajectoryDifferentialEvolution)

    @staticmethod
    def plot_all():
        Fold2000OffsetContinuationTrajectoryDifferentialEvolution.plot_exec_time()
        Fold2000OffsetContinuationTrajectoryDifferentialEvolution.plot_interpolation_per_sec_and_exec_time()
        Fold2000OffsetContinuationTrajectoryDifferentialEvolution.plot_interpolation_per_sec_and_exec_time_cuda_opencl()
