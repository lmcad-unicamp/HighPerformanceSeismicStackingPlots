from typing import Dict, List

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, Implementation, Implementations, Instances, SpitsExecution, \
    DataPath, Models, DataSets, ComputeMethods


class Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits(SpitsExecution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[9.17E+10, 9.86E+10, 9.61E+10],
                total_execution_time=[807.538, 822.86, 825.331],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_simple_synthetic_zocrs_de_spits'
            ),
            Instances.G4DN_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[9.05E+10, 9.54E+10, 9.47E+10],
                total_execution_time=[404.091, 422.501, 422.636],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_2.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_2_v20_cuda_simple_synthetic_zocrs_de_spits'
            ),
            Instances.G4DN_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[9.20E+10, 9.34E+10, 9.68E+10],
                total_execution_time=[204.707, 232.538, 206.206],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_4.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_4_v20_cuda_simple_synthetic_zocrs_de_spits'
            ),
            Instances.G4DN_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[9.43E+10, 9.75E+10, 9.48E+10],
                total_execution_time=[104.892, 103.882, 106.21],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE_8.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_fold2000_zocrs_de_spits'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.98E+10, 2.09E+10, 2.03E+10],
                total_execution_time=[1431.99, 1380.06, 1402.8],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_2_v20_cuda_fold2000_zocrs_de_spits'
            ),
            Instances.P2_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[1.98E+10, 1.96E+10, 1.98E+10],
                total_execution_time=[721.074, 745.533, 737.147],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_2.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_4_v20_cuda_fold2000_zocrs_de_spits'
            ),
            Instances.P2_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.04E+10, 2.09E+10, 2.00E+10],
                total_execution_time=[352.336, 354.937, 368.951],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_4.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_8_v20_cuda_fold2000_zocrs_de_spits'
            ),
            Instances.P2_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.07E+10, 1.77E+10, 2.02E+10],
                total_execution_time=[178.673, 204.507, 183.337],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE_8.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_fold2000_zocrs_de_spits'
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return ComputeMethods.DE_SPITS

    @staticmethod
    def data_name() -> str:
        return DataSets.FOLD2000

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.EXECUTION_DATA[impl]

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
            spits_class=Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits,
            impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_all():
        Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.plot_cost_and_exec_time()

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits,
            impl=Implementations.SOLUTION_V20)