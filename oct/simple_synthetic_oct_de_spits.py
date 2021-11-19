from typing import Dict, List

from helpers.graph_helpers import GraphHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementation, Instances, Implementations


class SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.54E+10],
                total_execution_time=[934.85],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.55E+10],
                total_execution_time=[479.365],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_2.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.54E+10],
                total_execution_time=[266.878],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_4.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.55E+10],
                total_execution_time=[158.607],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_8.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.10E+10],
                total_execution_time=[935.235],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.09E+10],
                total_execution_time=[486.114],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_2.cost_per_hour
            ),
            Instances.P2_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.10E+10],
                total_execution_time=[263.835],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_4.cost_per_hour
            ),
            Instances.P2_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.12E+10],
                total_execution_time=[163.388],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_8.cost_per_hour
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return 'de_spits'

    @staticmethod
    def data_name() -> str:
        return 'simple_synthetic'

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits.EXECUTION_DATA[impl]
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
                Instances.P2_X_LARGE_8
            ],
            "g4dn": [
                Instances.G4DN_X_LARGE,
                Instances.G4DN_X_LARGE_2,
                Instances.G4DN_X_LARGE_4,
                Instances.G4DN_X_LARGE_8
            ],
        }

        GraphHelpers.plot_cost_and_exec_time(
            instance_families=instance_families,
            spits_class=SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits,
            impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_all():
        SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits.plot_cost_and_exec_time()
