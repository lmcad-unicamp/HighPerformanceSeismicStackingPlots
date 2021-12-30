from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementation, Instances, Implementations, \
    DataPath, Models, DataSets, ComputeMethods


class Fold2000OffsetContinuationTrajectoryDifferentialEvolution(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[1.15E+10, 1.13E+10, 1.13E+10, 1.13E+10, 1.13E+10, 1.13E+10,
                                1.13E+10, 1.13E+10, 1.13E+10, 1.13E+10],
                total_execution_time=[2355.27, 2386.61, 2383.97, 2385.08, 2383.56, 2384.54,
                                      2383.55, 2383.05, 2384.8, 2385.57],
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_1_v20_cuda_fold2000_oct_de'
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[3.04E+10, 3.03E+10, 3.03E+10],
                total_execution_time=[925.404, 927.988, 926.559],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_fold2000_oct_de'
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[3.11008e+10, 3.06635e+10, 3.06618e+10],
                total_execution_time=[230.414, 233.644, 233.756],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.12XLARGE_1_v20_cuda_fold2000_oct_de'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[8.39159e+09, 8.42248e+09],
                total_execution_time=[3249.85, 3241.94],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_fold2000_oct_de'
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[8.76226e+09, 8.69289e+09, 8.71811e+09],
                total_execution_time=[415.768, 417.272, 445.101],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.8XLARGE_1_v20_cuda_fold2000_oct_de'
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[8.92715e+09, 8.92374e+09, 8.91804e+09],
                total_execution_time=[201.762, 201.098, 202.004],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.16XLARGE_1_v20_cuda_fold2000_oct_de'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[4.09E+10, 4.09E+10, 4.09E+10],
                total_execution_time=[737.539, 735.717, 735.795],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_v20_cuda_fold2000_oct_de'
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[4.09E+10, 4.09E+10],
                total_execution_time=[190.466, 190.829],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.8XLARGE_1_v20_cuda_fold2000_oct_de'
            ),
        },
        Implementations.SOLUTION_V20_OPENCL: {
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.89E+10, 2.89E+10, 2.90E+10],
                total_execution_time=[1059.04, 1057.1, 1053.45],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_opencl_opencl_fold2000_oct_de'
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.88E+10, 2.87E+10, 2.88E+10],
                total_execution_time=[268.724, 268.069, 267.735],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.12XLARGE_1_v20_opencl_opencl_fold2000_oct_de'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[8.45E+09, 8.3875e+09, 8.51969e+09],
                total_execution_time=[3432.95, 3472.76, 3415.58],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_opencl_opencl_fold2000_oct_de'
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[8.37E+09, 8.37E+09, 8.37E+09],
                total_execution_time=[436.436, 436.025, 436.166],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.8XLARGE_1_v20_opencl_opencl_fold2000_oct_de'
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[8.33E+09, 8.33E+09, 8.33E+09],
                total_execution_time=[229.754, 229.514, 229.526],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.16XLARGE_1_v20_opencl_opencl_fold2000_oct_de'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[3.81E+10, 3.81E+10, 3.81E+10],
                total_execution_time=[950.45, 949.307, 949.75],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_v20_opencl_opencl_fold2000_oct_de'
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[3.80E+10, 3.81E+10, 3.81E+10],
                total_execution_time=[246.613, 246.15, 245.985],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.8XLARGE_1_v20_opencl_opencl_fold2000_oct_de'
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return ComputeMethods.DE

    @staticmethod
    def data_name() -> str:
        return DataSets.FOLD2000

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = Fold2000OffsetContinuationTrajectoryDifferentialEvolution.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return Fold2000OffsetContinuationTrajectoryDifferentialEvolution.EXECUTION_DATA[impl]

    @staticmethod
    def model() -> str:
        return Models.OCT

    @staticmethod
    def plot_exec_time():
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
                                    exec_type=Fold2000OffsetContinuationTrajectoryDifferentialEvolution,
                                    impl=Implementations.SOLUTION_V20)

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

        implementation = Implementations.SOLUTION_V20

        GraphHelpers.plot_interpolation_per_sec_and_exec_time(instances=instances,
                                                              exec_type=Fold2000OffsetContinuationTrajectoryDifferentialEvolution,
                                                              impl=implementation)

    @staticmethod
    def plot_interpolation_per_sec_and_exec_time_cuda_opencl():
        instances: List[AwsInstance] = [
            Instances.G4DN_X_LARGE,
            Instances.G4DN_12X_LARGE,
            Instances.P2_X_LARGE,
            Instances.P2_8X_LARGE,
            Instances.P2_16X_LARGE,
            Instances.P3_2X_LARGE,
            Instances.P3_8X_LARGE
        ]

        GraphHelpers.plot_interpolation_per_sec_and_exec_time_cuda_opencl(
            instances=instances, exec_type=Fold2000OffsetContinuationTrajectoryDifferentialEvolution)

    @staticmethod
    def plot_all():
        Fold2000OffsetContinuationTrajectoryDifferentialEvolution.plot_exec_time()
        Fold2000OffsetContinuationTrajectoryDifferentialEvolution.plot_interpolation_per_sec_and_exec_time()
        Fold2000OffsetContinuationTrajectoryDifferentialEvolution.plot_interpolation_per_sec_and_exec_time_cuda_opencl()

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=Fold2000OffsetContinuationTrajectoryDifferentialEvolution,
            impl=Implementations.SOLUTION_V20)

        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=Fold2000OffsetContinuationTrajectoryDifferentialEvolution,
            impl=Implementations.SOLUTION_V20_OPENCL)
