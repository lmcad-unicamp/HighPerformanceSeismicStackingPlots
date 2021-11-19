from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Instances, Implementations, Implementation


class SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[5.41E+10],
                total_execution_time=[935.132],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[5.42E+10],
                total_execution_time=[482.354],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_2.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[5.46E+10],
                total_execution_time=[258.989],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_4.cost_per_hour
            ),
            Instances.G4DN_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.55E+10],
                total_execution_time=[168.769],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_8.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[5.42E+10],
                total_execution_time=[932.115],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.75E+10],
                total_execution_time=[485.868],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_2.cost_per_hour
            ),
            Instances.P2_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.74E+10],
                total_execution_time=[271.711],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_4.cost_per_hour
            ),
            Instances.P2_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.73E+10],
                total_execution_time=[161.449],
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
        __impl = SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.EXECUTION_DATA[impl]
        return __impl.get(instance)

    @staticmethod
    def model() -> str:
        return 'zocrs'

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
            spits_class=SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits,
            impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_all():
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.plot_cost_and_exec_time()
