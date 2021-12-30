from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementation, Implementations, Instances, \
    DataPath, Models, DataSets, ComputeMethods


class SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.CARDOSO_HERCULES: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='thesis',
                int_per_second=[1.07E+10]
            ),
        },
        Implementations.SOLUTION_V10: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='v1.0',
                int_per_second=[1.11E+10]
            ),
        },
        Implementations.GIMENES_ET_AL: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[1.97E+10, 1.97E+10, 1.97E+10, 1.97E+10, 1.98E+10, 1.99E+10, 1.99E+10,
                                1.99E+10, 1.99E+10, 1.99E+10],
                total_execution_time=None,
                kernel_execution_time=[3329.541386, 3330.425248, 3330.753449, 3328.231018, 3309.209666, 3297.799106,
                                       3293.236463, 3294.897874, 3291.258931, 3292.484441],
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_1_gimenes_cuda_simple_synthetic_zocrs_greedy'
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[4.23E+10, 4.22E+10, 4.21E+10],
                total_execution_time=None,
                kernel_execution_time=[1555.457869, 1554.276709, 1550.89172],
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_gimenes_cuda_simple_synthetic_zocrs_greedy'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[8.54E+10, 8.54E+10, 8.54E+10],
                total_execution_time=None,
                kernel_execution_time=[767.771957, 767.675853, 767.710438],
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_gimenes_cuda_simple_synthetic_zocrs_greedy'
            )
        },
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[3.57E+10, 3.57E+10, 3.57E+10, 3.57E+10, 3.57E+10, 3.57E+10,
                                3.57E+10, 3.57E+10, 3.57E+10, 3.57E+10],
                total_execution_time=[1880.23, 1881.81, 1880.11, 1880.19, 1880.49, 1879.85,
                                      1879.61, 1880.54, 1880.01, 1881.18],
                kernel_execution_time=[1880.23, 1881.81, 1880.11, 1880.19, 1880.49, 1879.85,
                                       1879.61, 1880.54, 1880.01, 1881.18],
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_1_v20_cuda_simple_synthetic_zocrs_greedy'
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[1.22E+11, 1.21E+11, 1.22E+11],
                total_execution_time=[598.371, 600.249, 595.9],
                kernel_execution_time=[i * 444 for i in [1.20997, 1.22172, 1.21165]],
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_simple_synthetic_zocrs_greedy'
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[1.07E+11, 1.07E+11, 1.07E+11],
                total_execution_time=[174.194, 170.262, 170.727],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.12XLARGE_1_v20_cuda_simple_synthetic_zocrs_greedy'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='dcea037',
                int_per_second=[2.57E+10, 2.55E+10],
                total_execution_time=[2616.1, 2623.69],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_simple_synthetic_zocrs_greedy'
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[2.54E+10, 2.54E+10, 2.54E+10],
                total_execution_time=[331.539, 331.444, 331.407],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.8XLARGE_1_v20_cuda_simple_synthetic_zocrs_greedy'
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[2.54E+10, 2.54E+10, 2.54E+10],
                total_execution_time=[169.867, 169.518, 170.491],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.16XLARGE_1_v20_cuda_simple_synthetic_zocrs_greedy'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[1.95E+11, 1.95E+11, 1.95E+11],
                total_execution_time=[398.106, 395.575, 395.518],
                kernel_execution_time=[i * 444 for i in [0.761138, 0.761385, 0.761438]],
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_v20_cuda_simple_synthetic_zocrs_greedy'
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[1.95E+11, 1.95E+11, 1.95E+11],
                total_execution_time=[108.246, 103.119, 103.174],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.8XLARGE_1_v20_cuda_simple_synthetic_zocrs_greedy'
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
        __impl = SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy.EXECUTION_DATA[impl]

    @staticmethod
    def model() -> str:
        return Models.ZOCRS

    @staticmethod
    def build_int_per_sec_relative_perf_data(instances: List[AwsInstance],
                                             implementations: List[str],
                                             reference_int_per_sec: float) -> (List[float], List[float]):
        int_per_sec: List[float] = []
        relative_performance: List[float] = []

        for instance in instances:
            for impl in implementations:
                __exec = SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy.execution(instance, impl)
                int_per_sec.append(__exec.avg_int_per_second)
                relative_performance.append(__exec.relative_int_per_second(reference_int_per_sec))

        return int_per_sec, relative_performance

    @staticmethod
    def plot_v11_gimenes_et_al():
        instances: List[AwsInstance] = [Instances.GTX_TITAN]
        implementations: List[Implementation] = [Implementations.SOLUTION_V10, Implementations.GIMENES_ET_AL]

        GraphHelpers.plot_interpolations_per_sec_with_relative_performance(instances=instances,
                                                                           implementations=implementations,
                                                                           exec_type=SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy,
                                                                           reference_impl=Implementations.GIMENES_ET_AL)

    @staticmethod
    def plot_v11_v20_gimenes_et_al():
        instances: List[AwsInstance] = [Instances.GTX_TITAN]
        implementations: List[Implementation] = \
            [Implementations.SOLUTION_V10, Implementations.GIMENES_ET_AL, Implementations.SOLUTION_V20]

        GraphHelpers.plot_interpolations_per_sec_with_relative_performance(instances=instances,
                                                                           implementations=implementations,
                                                                           exec_type=SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy,
                                                                           reference_impl=Implementations.GIMENES_ET_AL)

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
                                                              exec_type=SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy,
                                                              impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_v20_gimenes_et_all_int_per_sec_total_exec_time_and_relative_perf():
        instances: List[AwsInstance] = [
            Instances.GTX_TITAN,
            Instances.G4DN_X_LARGE,
            Instances.P3_2X_LARGE
        ]

        implementations: List[Implementation] = [
            Implementations.GIMENES_ET_AL,
            Implementations.SOLUTION_V20
        ]

        GraphHelpers.plot_v20_gimenes_et_all_int_per_sec_total_exec_time_and_relative_perf(instances=instances,
                                                                                           implementations=implementations,
                                                                                           exec_type=SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy,
                                                                                           our_impl=Implementations.SOLUTION_V20,
                                                                                           reference_impl=Implementations.GIMENES_ET_AL)

    @staticmethod
    def plot_all():
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy.plot_v11_gimenes_et_al()
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy.plot_v11_v20_gimenes_et_al()
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy. \
            plot_v20_gimenes_et_all_int_per_sec_total_exec_time_and_relative_perf()
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy.plot_interpolation_per_sec_and_exec_time()

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy,
            impl=Implementations.SOLUTION_V20)

        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy,
            impl=Implementations.GIMENES_ET_AL)
