from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementation, Implementations, Instances, \
    DataPath, ComputeMethods, DataSets, Models


class SimpleSyntheticCommonMidpointDifferentialEvolution(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca',
                int_per_second=[3.17E+10, 2.90E+10, 3.01E+10, 2.96E+10, 2.89E+10, 2.91E+10, 2.87E+10,
                                2.88E+10, 2.85E+10, 2.85E+10],
                total_execution_time=[16.5487, 17.9795, 17.3327, 17.6475, 18.0526, 17.9293, 18.1306,
                                      18.0991, 18.3034, 18.3216],
                kernel_execution_time=None,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_1_v20_cuda_simple_synthetic_cmp_de'
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[1.13E+11, 1.13E+11, 1.13E+11],
                total_execution_time=[6.5778, 6.56364, 6.58946],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_simple_synthetic_cmp_de'
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.10E+11, 1.10E+11, 1.10E+11, 1.10E+11, 1.10E+11],
                total_execution_time=[2.67829, 2.45017, 2.41367, 2.39118, 2.41292],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.12XLARGE_1_v20_cuda_simple_synthetic_cmp_de'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[2.20E+10, 2.20E+10, 2.20E+10, 2.20E+10, 2.20E+10],
                total_execution_time=[26.5766, 26.4653, 26.483, 26.476, 26.4832],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_simple_synthetic_cmp_de'
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[2.18E+10, 2.27E+10, 2.26E+10, 2.20E+10, 2.24E+10],
                total_execution_time=[5.04143, 4.6945, 4.7428, 4.91289, 4.78394],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.8XLARGE_1_v20_cuda_simple_synthetic_cmp_de'
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[2.09E+10, 2.12E+10, 2.23E+10, 2.09E+10, 2.09E+10],
                total_execution_time=[6.86737, 6.4081, 6.07903, 6.53233, 6.4672],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.16XLARGE_1_v20_cuda_simple_synthetic_cmp_de'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.35E+11, 1.35E+11, 1.36E+11],
                total_execution_time=[5.92473, 5.91082, 5.79185],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_v20_cuda_simple_synthetic_cmp_de'
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.29E+11, 1.30E+11, 1.29E+11, 1.29E+11, 1.29E+11],
                total_execution_time=[2.66676, 2.61301, 2.63367, 2.59773, 2.64171],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.8XLARGE_1_v20_cuda_simple_synthetic_cmp_de'
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
        __impl = SimpleSyntheticCommonMidpointDifferentialEvolution.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return SimpleSyntheticCommonMidpointDifferentialEvolution.EXECUTION_DATA[impl]

    @staticmethod
    def model() -> str:
        return Models.CMP

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

        GraphHelpers.plot_exec_time(instances=instances,
                                    exec_type=SimpleSyntheticCommonMidpointDifferentialEvolution,
                                    impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_all():
        SimpleSyntheticCommonMidpointDifferentialEvolution.plot_interpolation_per_sec_and_exec_time()

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=SimpleSyntheticCommonMidpointDifferentialEvolution,
            impl=Implementations.SOLUTION_V20)
