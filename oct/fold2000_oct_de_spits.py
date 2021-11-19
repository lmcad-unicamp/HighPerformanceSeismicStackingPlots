from typing import Dict, List

from helpers.graph_helpers import GraphHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementation, Implementations, Instances


class Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits(Execution):

    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.68E+10, 2.99E+10, 3.05E+10],
                total_execution_time=[1055.79, 975.216, 951.032],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.88E+10, 2.86E+10, 2.89E+10],
                total_execution_time=[497.25, 508.905, 514.43],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_2.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[3.08E+10, 2.97E+10, 2.78E+10],
                total_execution_time=[234.893, 252.077, 266.325],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_4.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.92E+10, 2.86E+10, 2.91E+10],
                total_execution_time=[125.046, 127.608, 126.22],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_8.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_16: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.85482e+10, 2.87946e+10],
                total_execution_time=[65.9322, 66.0763],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_16.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_32: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.93605e+10, 3.03283e+10, 3.03929e+10],
                total_execution_time=[35.9084, 34.7625, 34.6886],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_32.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[8.57E+09, 8.39E+09, 8.72E+09, 8.86E+09],
                total_execution_time=[3206.9, 3258.94, 3159.51, 3128.7600],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[8.94E+09, 8.78E+09, 8.97E+09, 8.76E+09],
                total_execution_time=[1535.21, 1582.14, 1538.47, 1589.1900],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_2.cost_per_hour
            ),
            Instances.P2_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[8.73E+09, 8.74E+09, 8.73E+09, 8.61E+09],
                total_execution_time=[790.253, 803.191, 788.962, 799.9600],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_4.cost_per_hour
            ),
            Instances.P2_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[8.71E+09, 8.81E+09, 8.74E+09, 8.80E+09],
                total_execution_time=[456.129, 396.076, 398.021, 397.5000],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_8.cost_per_hour
            ),
            Instances.P2_X_LARGE_16: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[8.76933e+09],
                total_execution_time=[202.641],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_16.cost_per_hour
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return 'de_spits'

    @staticmethod
    def data_name() -> str:
        return 'fold2000'

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits.EXECUTION_DATA[impl]
        return __impl.get(instance)

    @staticmethod
    def model() -> str:
        return 'oct'

    @staticmethod
    def plot_cost_and_exec_time():
        instance_families: Dict[str, List[AwsInstance]] = {
            "p2": [
                Instances.P2_X_LARGE,
                Instances.P2_X_LARGE_2,
                Instances.P2_X_LARGE_4,
                Instances.P2_X_LARGE_8,
                Instances.P2_X_LARGE_16
            ],
            "g4dn": [
                Instances.G4DN_X_LARGE,
                Instances.G4DN_X_LARGE_2,
                Instances.G4DN_X_LARGE_4,
                Instances.G4DN_X_LARGE_8,
                Instances.G4DN_X_LARGE_16,
                Instances.G4DN_X_LARGE_32
            ],
        }

        GraphHelpers.plot_cost_and_exec_time(
            instance_families=instance_families,
            spits_class=Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits,
            impl=Implementations.SOLUTION_V20,
            print_data=False)

    @staticmethod
    def plot_all():
        Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits.plot_cost_and_exec_time()
