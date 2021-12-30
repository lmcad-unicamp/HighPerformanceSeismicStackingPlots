from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementation, Implementations, Instances, \
    DataPath, ComputeMethods, DataSets, Models


class SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolution(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[1.38E+10, 1.38E+10, 1.38E+10, 1.38E+10, 1.38E+10, 1.38E+10, 1.38E+10,
                                1.38E+10, 1.38E+10, 1.38E+10],
                total_execution_time=[516.451, 517.248, 516.922, 517.087, 516.574, 516.958, 516.142,
                                      516.868, 516.886, 516.822],
                kernel_execution_time=None,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_1_v20_cuda_simple_synthetic_oct_de'
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[2.58E+10, 2.58E+10, 2.58E+10, 2.58E+10, 2.58E+10],
                total_execution_time=[288.995, 289.2, 288.676, 288.412, 288.589],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_simple_synthetic_oct_de'
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[2.61E+10, 2.61E+10, 2.61E+10],
                total_execution_time=[73.3806, 73.4086, 73.2946],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.12XLARGE_1_v20_cuda_simple_synthetic_oct_de'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[1.13E+10, 1.13E+10, 1.13E+10],
                total_execution_time=[628.688, 628.751, 629.622],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_simple_synthetic_oct_de'
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.12E+10, 1.12E+10, 1.12E+10],
                total_execution_time=[81.0409, 81.1337, 81.0365],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.8XLARGE_1_v20_cuda_simple_synthetic_oct_de'
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.10E+10, 1.10E+10, 1.10E+10],
                total_execution_time=[45.215, 45.32, 45.215],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.16XLARGE_1_v20_cuda_simple_synthetic_oct_de'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[6.32E+10, 6.32E+10, 6.30E+10],
                total_execution_time=[119.959, 119.941, 120.249],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_v20_cuda_simple_synthetic_oct_de'
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[6.29E+10, 6.29E+10, 6.29E+10],
                total_execution_time=[31.3434, 31.3857, 31.3812],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.8XLARGE_1_v20_cuda_simple_synthetic_oct_de'
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return ComputeMethods.DE

    @staticmethod
    def data_name() -> str:
        return DataSets.SIMPLE_SYNTHETIC

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolution.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolution.EXECUTION_DATA[impl]

    @staticmethod
    def model() -> str:
        return Models.OCT

    @staticmethod
    def plot_interpolation_per_sec_and_exec_time():
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
                                    exec_type=SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolution,
                                    impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_all():
        SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolution.plot_interpolation_per_sec_and_exec_time()

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolution,
            impl=Implementations.SOLUTION_V20)
