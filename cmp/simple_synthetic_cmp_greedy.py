from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, ExecutionBreakDownData, Execution, Implementation, \
    Implementations, Instances, DataPath, DataSets, Models, ComputeMethods


class SimpleSyntheticCommonMidpointGreedy(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.CARDOSO_HERCULES: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='thesis',
                int_per_second=[1.26E+10]
            ),
        },
        Implementations.SOLUTION_V10: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='v1.0',
                int_per_second=[1.59E+10]
            ),
        },
        Implementations.GIMENES_ET_AL: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[3.17E+10, 2.96E+10, 2.98E+10, 2.97E+10, 2.97E+10, 2.96E+10, 2.97E+10,
                                2.96E+10, 2.96E+10, 2.96E+10],
                total_execution_time=None,
                kernel_execution_time=[14.123772, 15.125578, 15.062458, 15.082742, 15.098323, 15.117057, 15.113919,
                                       15.126885, 15.125487, 15.133652],
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_1_gimenes_cuda_simple_synthetic_cmp_greedy'
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[6.72E+10, 6.73E+10, 6.73E+10],
                total_execution_time=None,
                kernel_execution_time=[6.667072, 6.656811, 6.651377],
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_gimenes_cuda_simple_synthetic_cmp_greedy'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='c2bf4ce',
                int_per_second=[1.23E+11, 1.23E+11, 1.23E+11],
                total_execution_time=None,
                kernel_execution_time=[3.648612, 3.646788, 3.648029],
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_gimenes_cuda_simple_synthetic_cmp_greedy'
            )
        },
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='c51bf56ee',
                int_per_second=[3.67307e+10, 3.66840e+10, 3.66611e+10, 3.49224e+10, 3.47298e+10],
                total_execution_time=[i * 444 for i in [0.0267702, 0.0268018, 0.0268176, 0.0282316, 0.0284525]],
                kernel_execution_time=[i * 444 for i in [0.0267702, 0.0268018, 0.0268176, 0.0282316, 0.0284525]],
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_1_v20_cuda_simple_synthetic_cmp_greedy'
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[1.65E+11, 1.65E+11, 1.71E+11, 1.71E+11, 1.70E+11],
                total_execution_time=[6.99035, 7.07247, 7.86191, 7.21928, 7.06449],
                kernel_execution_time=[i * 444 for i in [0.00598765, 0.00598724, 0.00579245, 0.00579465, 0.00581892]],
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_simple_synthetic_cmp_greedy'
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.61E+11, 1.61E+11, 1.61E+11, 1.60E+11],
                total_execution_time=[2.66911, 2.5363, 2.56345, 2.55961],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.12XLARGE_1_v20_cuda_simple_synthetic_cmp_greedy'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[2.60E+10, 2.60E+10, 2.59E+10],
                total_execution_time=[24.0501, 23.4379, 23.4512],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_simple_synthetic_cmp_greedy'
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[2.35E+10, 2.37E+10, 2.42E+10, 2.38E+10, 2.35E+10],
                total_execution_time=[5.3418, 4.78985, 4.66243, 4.65544, 4.76881],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.8XLARGE_1_v20_cuda_simple_synthetic_cmp_greedy'
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[2.23E+10, 2.23E+10, 2.25E+10, 2.21E+10, 2.28E+10],
                total_execution_time=[6.59893, 6.37733, 6.35478, 6.52768, 6.05073],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.16XLARGE_1_v20_cuda_simple_synthetic_cmp_greedy'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[2.01E+11, 2.01E+11, 2.02E+11, 2.01E+11, 2.02E+11],
                total_execution_time=[6.76276, 6.68065, 6.97359, 6.72273, 6.6656],
                kernel_execution_time=[i * 444 for i in [0.00486895, 0.00486946, 0.00484526, 0.00485909, 0.00484992]],
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_v20_cuda_simple_synthetic_cmp_greedy'
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[2.00E+11, 2.01E+11, 2.00E+11, 2.02E+11, 2.01E+11],
                total_execution_time=[2.88235, 2.88925, 2.90984, 2.90582],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.8XLARGE_1_v20_cuda_simple_synthetic_cmp_greedy'
            ),
        }
    }

    BREAKDOWN_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionBreakDownData]] = {
        Implementations.SOLUTION_V20: {
            Instances.P2_X_LARGE: ExecutionBreakDownData(
                read_data=0.12,
                write_data=0.32,
                init_gpus=0.04,
                compute_sembl=20.62,
                copy_buffer=0.13
            ),
            Instances.P2_8X_LARGE: ExecutionBreakDownData(
                read_data=0.11,
                write_data=0.36,
                init_gpus=0.30,
                compute_sembl=2.74,
                copy_buffer=1.43
            ),
            Instances.P2_16X_LARGE: ExecutionBreakDownData(
                read_data=0.11,
                write_data=0.36,
                init_gpus=0.99,
                compute_sembl=1.73,
                copy_buffer=3.45
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
    def model() -> str:
        return Models.CMP

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        impl = SimpleSyntheticCommonMidpointGreedy.executions(impl)
        return impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return SimpleSyntheticCommonMidpointGreedy.EXECUTION_DATA[impl]

    @staticmethod
    def plot_v11_gimenes_et_al():
        instances: List[AwsInstance] = [Instances.GTX_TITAN]
        implementations: List[Implementation] = [Implementations.SOLUTION_V10, Implementations.GIMENES_ET_AL]

        GraphHelpers.plot_interpolations_per_sec_with_relative_performance(instances=instances,
                                                                           implementations=implementations,
                                                                           exec_type=SimpleSyntheticCommonMidpointGreedy,
                                                                           reference_impl=Implementations.GIMENES_ET_AL)

    @staticmethod
    def plot_v11_v20_gimenes_et_al():
        instances: List[AwsInstance] = [Instances.GTX_TITAN]
        implementations: List[Implementation] = \
            [Implementations.SOLUTION_V10, Implementations.GIMENES_ET_AL, Implementations.SOLUTION_V20]

        GraphHelpers.plot_interpolations_per_sec_with_relative_performance(instances=instances,
                                                                           implementations=implementations,
                                                                           exec_type=SimpleSyntheticCommonMidpointGreedy,
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
                                                              exec_type=SimpleSyntheticCommonMidpointGreedy,
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
                                                                                           exec_type=SimpleSyntheticCommonMidpointGreedy,
                                                                                           our_impl=Implementations.SOLUTION_V20,
                                                                                           reference_impl=Implementations.GIMENES_ET_AL)

    @staticmethod
    def plot_all():
        SimpleSyntheticCommonMidpointGreedy.plot_v11_gimenes_et_al()
        SimpleSyntheticCommonMidpointGreedy.plot_v11_v20_gimenes_et_al()
        SimpleSyntheticCommonMidpointGreedy.plot_v20_gimenes_et_all_int_per_sec_total_exec_time_and_relative_perf()
        SimpleSyntheticCommonMidpointGreedy.plot_interpolation_per_sec_and_exec_time()

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=SimpleSyntheticCommonMidpointGreedy,
            impl=Implementations.SOLUTION_V20)

        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=SimpleSyntheticCommonMidpointGreedy,
            impl=Implementations.GIMENES_ET_AL)
