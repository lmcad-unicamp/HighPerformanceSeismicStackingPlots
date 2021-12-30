from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, Instances, Implementations, Implementation, SpitsExecution, \
    DataPath, ComputeMethods, DataSets, Models


class SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits(SpitsExecution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[5.41E+10],
                total_execution_time=[935.132],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_simple_synthetic_zocrs_de_spits'
            ),
            Instances.G4DN_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[5.42E+10],
                total_execution_time=[482.354],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_2.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_2_v20_cuda_simple_synthetic_zocrs_de_spits'
            ),
            Instances.G4DN_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[5.46E+10],
                total_execution_time=[258.989],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_4.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_4_v20_cuda_simple_synthetic_zocrs_de_spits'
            ),
            Instances.G4DN_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.55E+10],
                total_execution_time=[168.769],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_8.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_8_v20_cuda_simple_synthetic_zocrs_de_spits'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[5.42E+10],
                total_execution_time=[932.115],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_simple_synthetic_zocrs_de_spits'
            ),
            Instances.P2_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.75E+10],
                total_execution_time=[485.868],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_2.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_2_v20_cuda_simple_synthetic_zocrs_de_spits'
            ),
            Instances.P2_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.74E+10],
                total_execution_time=[271.711],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_4.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_4_v20_cuda_simple_synthetic_zocrs_de_spits'
            ),
            Instances.P2_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.73E+10],
                total_execution_time=[161.449],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_8.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_8_v20_cuda_simple_synthetic_zocrs_de_spits'
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
        __impl = SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.EXECUTION_DATA[impl]

    @staticmethod
    def model() -> str:
        return Models.ZOCRS

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

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits,
            impl=Implementations.SOLUTION_V20)