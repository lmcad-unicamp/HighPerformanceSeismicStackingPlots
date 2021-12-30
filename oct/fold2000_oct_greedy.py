from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementation, Implementations, Instances, \
    DataPath, DataSets, ComputeMethods, Models


class Fold2000OffsetContinuationTrajectoryGreedy(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[1.62E+10, 1.62E+10, 1.62E+10, 1.62E+10, 1.62E+10, 1.62E+10,
                                1.62E+10, 1.62E+10, 1.62E+10, 1.62E+10],
                total_execution_time=[17316.4, 17299.9, 17373.3, 17330.1, 17344,
                                      17313.5, 17319.8, 17310.4, 17312.5, 17288],
                kernel_execution_time=None,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_1_v20_cuda_fold2000_oct_greedy'
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[4.47E+10, 4.49E+10, 4.49E+10],
                total_execution_time=[6014.99, 5994.48, 5996.54],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_fold2000_oct_greedy'
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[4.34E+10, 4.37E+10, 4.36E+10],
                total_execution_time=[1550.46, 1543.78, 1545.38],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.12XLARGE_1_v20_cuda_fold2000_oct_greedy'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[1.21E+10],
                total_execution_time=[23061.5],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_fold2000_oct_greedy'
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[1.26E+10],
                total_execution_time=[2806.76],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.8XLARGE_1_v20_cuda_fold2000_oct_greedy'
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[1.25E+10, 1.25E+10],
                total_execution_time=[1465.93, 1472.66],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.16XLARGE_1_v20_cuda_fold2000_oct_greedy'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[1.86E+11],
                total_execution_time=[1696.9],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_v20_cuda_fold2000_oct_greedy'
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[1.83E+11, 1.83E+11, 1.83E+11],
                total_execution_time=[438.222, 438.021, 437.636],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.8XLARGE_1_v20_cuda_fold2000_oct_greedy'
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return ComputeMethods.GREEDY

    @staticmethod
    def data_name() -> str:
        return DataSets.FOLD2000

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = Fold2000OffsetContinuationTrajectoryGreedy.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return Fold2000OffsetContinuationTrajectoryGreedy.EXECUTION_DATA[impl]

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
                                                              exec_type=Fold2000OffsetContinuationTrajectoryGreedy,
                                                              impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_all():
        Fold2000OffsetContinuationTrajectoryGreedy.plot_interpolation_per_sec_and_exec_time()

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=Fold2000OffsetContinuationTrajectoryGreedy,
            impl=Implementations.SOLUTION_V20)

