from typing import Dict, List

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, Implementation, Instances, Implementations, \
    DataPath, SpitsExecution, ComputeMethods, DataSets, Models


class SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits(SpitsExecution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.G4DN_X_LARGE: ExecutionData( # OK
                test_id='e81d6e1',
                int_per_second=[2.53947e+10],
                total_execution_time=[934.85],
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_simple_synthetic_oct_de_spits'
            ),
            Instances.G4DN_X_LARGE_2: ExecutionData( # OK
                test_id='e81d6e1',
                int_per_second=[2.55E+10],
                total_execution_time=[479.365],
                instance_cost_per_hour=Instances.G4DN_X_LARGE_2.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_2_v20_cuda_simple_synthetic_oct_de_spits'
            ),
            Instances.G4DN_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.54E+10],
                total_execution_time=[266.878],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_4.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_4_v20_cuda_simple_synthetic_oct_de_spits'
            ),
            Instances.G4DN_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.55E+10],
                total_execution_time=[158.607],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_8.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_8_v20_cuda_simple_synthetic_oct_de_spits'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.09728e+10],
                total_execution_time=[935.235],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_simple_synthetic_oct_de_spits'
            ),
            Instances.P2_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.09242e+10],
                total_execution_time=[486.114],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_2.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_2_v20_cuda_simple_synthetic_oct_de_spits'
            ),
            Instances.P2_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.10199e+10],
                total_execution_time=[263.835],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_4.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_4_v20_cuda_simple_synthetic_oct_de_spits'
            ),
            Instances.P2_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.11812e+10],
                total_execution_time=[163.388],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_8.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_8_v20_cuda_simple_synthetic_oct_de_spits'
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return ComputeMethods.DE_SPITS

    @staticmethod
    def data_name() -> str:
        return DataSets.SIMPLE_SYNTHETIC

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits.EXECUTION_DATA[impl]

    @staticmethod
    def model() -> str:
        return Models.OCT

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

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits,
            impl=Implementations.SOLUTION_V20)
