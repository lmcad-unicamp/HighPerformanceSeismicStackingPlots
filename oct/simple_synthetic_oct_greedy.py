from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementations, Instances, Implementation, \
    DataPath, ComputeMethods, DataSets, Models


class SimpleSyntheticOffsetContinuationTrajectoryGreedy(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[1.25E+10, 1.25E+10, 1.25E+10, 1.25E+10, 1.24E+10, 1.25E+10, 1.25E+10,
                                1.25E+10, 1.25E+10, 1.25E+10],
                total_execution_time=[3321.46, 3324.07, 3327.83, 3326.12, 3328.4, 3322.31, 3326.57,
                                      3322.32, 3322.39, 3315.09],
                kernel_execution_time=None,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_1_v20_cuda_simple_synthetic_oct_greedy'
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[2.56E+10, 2.57E+10, 2.57E+10],
                total_execution_time=[1611.69, 1612.17, 1610.15],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_simple_synthetic_oct_greedy'
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[2.55E+10, 2.55E+10, 2.56E+10],
                total_execution_time=[405.904, 406.784, 406.386],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.12XLARGE_1_v20_cuda_simple_synthetic_oct_greedy'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[9.23E+09],
                total_execution_time=[4284.33],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_simple_synthetic_oct_greedy'
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[9.25E+09],
                total_execution_time=[559.519],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.8XLARGE_1_v20_cuda_simple_synthetic_oct_greedy'
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[8.90E+09, 8.90E+09, 8.95E+09],
                total_execution_time=[286.263, 284.608, 281.955],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.16XLARGE_1_v20_cuda_simple_synthetic_oct_greedy'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[4.43E+10],
                total_execution_time=[1049.73],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_v20_cuda_simple_synthetic_oct_greedy'
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[4.46E+10, 4.46E+10, 4.45E+10],
                total_execution_time=[265.279, 265.602, 266.453],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.8XLARGE_1_v20_cuda_simple_synthetic_oct_greedy'
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return ComputeMethods.GREEDY

    @staticmethod
    def data_name() -> str:
        return DataSets.SIMPLE_SYNTHETIC

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = SimpleSyntheticOffsetContinuationTrajectoryGreedy.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return SimpleSyntheticOffsetContinuationTrajectoryGreedy.EXECUTION_DATA[impl]

    @staticmethod
    def model() -> str:
        return Models.OCT

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
                                                              exec_type=SimpleSyntheticOffsetContinuationTrajectoryGreedy,
                                                              impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_all():
        SimpleSyntheticOffsetContinuationTrajectoryGreedy.plot_interpolation_per_sec_and_exec_time()

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=SimpleSyntheticOffsetContinuationTrajectoryGreedy,
            impl=Implementations.SOLUTION_V20)
