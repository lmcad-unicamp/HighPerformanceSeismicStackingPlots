from typing import Dict, List

from helpers.persistence_helpers import PersistenceHelpers
from helpers.graph_helpers import GraphHelpers
from model.execution_data import ExecutionData, AwsInstance, Implementation, Implementations, Instances, SpitsExecution, \
    DataPath, ComputeMethods, DataSets, Models


class Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits(SpitsExecution):

    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.67626e+10, 2.98553e+10, 3.04953e+10],
                total_execution_time=[1055.79, 975.216, 951.032],
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4DN_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.87782e+10, 2.86276e+10, 2.88944e+10],
                total_execution_time=[497.25, 508.905, 514.43],
                instance_cost_per_hour=Instances.G4DN_X_LARGE_2.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_2_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4DN_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[3.08237e+10, 2.96666e+10, 2.78205e+10],
                total_execution_time=[234.893, 252.077, 266.325],
                instance_cost_per_hour=Instances.G4DN_X_LARGE_4.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_4_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4DN_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.91527e+10, 2.85531e+10, 2.91418e+10],
                total_execution_time=[125.046, 127.608, 126.22],
                instance_cost_per_hour=Instances.G4DN_X_LARGE_8.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_8_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4DN_X_LARGE_16: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.85482e+10, 2.87946e+10],
                total_execution_time=[65.9322, 66.0763],
                instance_cost_per_hour=Instances.G4DN_X_LARGE_16.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_16_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4DN_X_LARGE_32: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[2.93605e+10],
                total_execution_time=[35.9084],
                instance_cost_per_hour=Instances.G4DN_X_LARGE_32.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_32_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[8.56681e+09, 8.39067e+09, 8.72136e+09, 8.85872e+09],
                total_execution_time=[3206.9, 3258.94, 3159.51, 3128.76],
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.P2_X_LARGE_2: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[8.94348e+09, 8.77780e+09, 8.97174e+09, 8.75986e+09],
                total_execution_time=[1535.21, 1582.14, 1538.47, 1589.19],
                instance_cost_per_hour=Instances.P2_X_LARGE_2.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_2_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.P2_X_LARGE_4: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[8.73120e+09, 8.74216e+09, 8.72539e+09, 8.61130e+09],
                total_execution_time=[790.253, 803.191, 788.962, 799.96],
                instance_cost_per_hour=Instances.P2_X_LARGE_4.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_4_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.P2_X_LARGE_8: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[8.70525e+09, 8.80933e+09, 8.74163e+09, 8.79571e+09],
                total_execution_time=[456.129, 396.076, 398.021, 397.5],
                instance_cost_per_hour=Instances.P2_X_LARGE_8.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_8_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.P2_X_LARGE_16: ExecutionData(
                test_id='e81d6e1',
                int_per_second=[8.76933e+09, 8.72898e+09, 8.72882e+09],
                total_execution_time=[202.641, 222.875, 218.152],
                instance_cost_per_hour=Instances.P2_X_LARGE_16.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_16_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.P2_X_LARGE_32: ExecutionData(
                test_id='fa0f66',
                int_per_second=[8.82e+09],
                total_execution_time=[107.465],
                instance_cost_per_hour=Instances.P2_X_LARGE_32.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_32_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4AD_X_LARGE: ExecutionData(
                test_id='fa0f66',
                int_per_second=[2.15525e+10, 2.15578e+10, 2.155e+10, 2.13588e+10],
                total_execution_time=[2567.33, 2531.13, 2547.07, 2598.8], # 2608.82
                instance_cost_per_hour=Instances.G4AD_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4AD.XLARGE_1_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4AD_X_LARGE_2: ExecutionData(
                test_id='fa0f66',
                int_per_second=[2.14134e+10, 2.14224e+10, 2.14093e+10, 2.14577e+10],
                total_execution_time=[1279.59, 1269.61, 1269.2, 1299.87], # 1311.89
                instance_cost_per_hour=Instances.G4AD_X_LARGE_2.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4AD.XLARGE_2_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4AD_X_LARGE_4: ExecutionData(
                test_id='fa0f66',
                int_per_second=[2.12543e+10, 2.12495e+10, 2.12601e+10, 2.12911e+10],
                total_execution_time=[644.247, 640.179, 638.145, 659.22], # 659.23
                instance_cost_per_hour=Instances.G4AD_X_LARGE_4.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4AD.XLARGE_4_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4AD_X_LARGE_8: ExecutionData(
                test_id='fa0f66',
                int_per_second=[2.1356e+10, 2.13627e+10, 2.13666e+10, 2.13362e+10],
                total_execution_time=[325.773, 323.709, 325.838, 338.872], # 338.878
                instance_cost_per_hour=Instances.G4AD_X_LARGE_8.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4AD.XLARGE_8_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4AD_X_LARGE_16: ExecutionData(
                test_id='fa0f66',
                int_per_second=[2.12721e+10, 2.1339e+10, 2.13442e+10],
                total_execution_time=[163.492, 163.948, 161.927],
                instance_cost_per_hour=Instances.G4AD_X_LARGE_16.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4AD.XLARGE_16_v20_cuda_fold2000_oct_de_spits'
            ),
            Instances.G4AD_X_LARGE_32: ExecutionData(
                test_id='fa0f66',
                int_per_second=[2.13469e+10, 2.1347e+10, 2.13573e+10],
                total_execution_time=[83.8987, 85.8951, 83.7863],
                instance_cost_per_hour=Instances.G4AD_X_LARGE_32.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4AD.XLARGE_32_v20_cuda_fold2000_oct_de_spits'
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
        __impl = Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits.EXECUTION_DATA.get(impl)

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
            "g4ad": [
                Instances.G4AD_X_LARGE,
                Instances.G4AD_X_LARGE_2,
                Instances.G4AD_X_LARGE_4,
                Instances.G4AD_X_LARGE_8,
                Instances.G4AD_X_LARGE_16,
                Instances.G4AD_X_LARGE_32
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

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits,
            impl=Implementations.SOLUTION_V20)
