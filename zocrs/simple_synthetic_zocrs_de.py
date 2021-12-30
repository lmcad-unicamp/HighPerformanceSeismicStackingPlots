from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from helpers.persistence_helpers import PersistenceHelpers
from model.execution_data import ExecutionData, AwsInstance, Implementation, Implementations, Instances, Execution, \
    DataPath, ComputeMethods, DataSets, Models


class SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolution(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca5',
                int_per_second=[2.10E+10, 2.09E+10, 2.10E+10, 2.10E+10, 2.10E+10, 2.10E+10, 2.10E+10,
                                2.09E+10, 2.10E+10, 2.09E+10],
                total_execution_time=[328.825, 329.678, 329.151, 329.506, 328.927, 328.934, 329.102,
                                      329.542, 329.381, 329.653],
                kernel_execution_time=None,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/GTX_TITAN_1_v20_cuda_simple_synthetic_zocrs_de'
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='55766d4e2',
                int_per_second=[9.93E+10, 9.87E+10, 9.91E+10],
                total_execution_time=[71.7613, 72.2028, 71.9492],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.XLARGE_1_v20_cuda_simple_synthetic_zocrs_de'
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.00E+11, 1.00E+11, 1.00E+11, 9.94E+10, 9.87E+10],
                total_execution_time=[18.608, 21.3896, 18.7034, 18.825, 18.9989],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/G4DN.12XLARGE_1_v20_cuda_simple_synthetic_zocrs_de'
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[1.67E+10, 1.67E+10, 1.67E+10],
                total_execution_time=[410.642, 411.276, 410.601],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.XLARGE_1_v20_cuda_simple_synthetic_zocrs_de'
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.73E+10, 1.73E+10, 1.73E+10, 1.73E+10, 1.73E+10],
                total_execution_time=[51.5988, 51.5509, 51.575, 51.8197, 51.666],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.8XLARGE_1_v20_cuda_simple_synthetic_zocrs_de'
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.71E+10, 1.71E+10, 1.71E+10, 1.71E+10, 1.71E+10],
                total_execution_time=[30.2541, 30.3255, 30.2639, 30.3497, 30.2878],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P2.16XLARGE_1_v20_cuda_simple_synthetic_zocrs_de'
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[1.14E+11, 1.14E+11, 1.14E+11],
                total_execution_time=[64.674, 64.4233, 64.3011],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.2XLARGE_1_v20_cuda_simple_synthetic_zocrs_de'
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[1.18E+11, 1.18E+11, 1.18E+11, 1.18E+11, 1.18E+11],
                total_execution_time=[16.8361, 16.7056, 16.8248, 16.7876, 16.7499],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour,
                link_to_data='https://github.com/lmcad-unicamp/HighPerformanceSeismicStackingClapExperiment/tree/master/P3.8XLARGE_1_v20_cuda_simple_synthetic_zocrs_de'
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
        __impl = SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolution.executions(impl)
        return __impl.get(instance)

    @staticmethod
    def executions(impl: Implementation) -> Dict[AwsInstance, ExecutionData]:
        return SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolution.EXECUTION_DATA[impl]

    @staticmethod
    def model() -> str:
        return Models.ZOCRS

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
                                    exec_type=SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolution,
                                    impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_all():
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolution.\
            plot_interpolation_per_sec_and_exec_time()

    @staticmethod
    def search_for_data_and_persist():
        PersistenceHelpers.search_for_execution_data(
            search_folder=DataPath.RAW_DATA_DIR,
            result_folder=DataPath.GIT_DATA_DIR,
            exec_class=SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolution,
            impl=Implementations.SOLUTION_V20)