from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from model.execution_data import ExecutionData, AwsInstance, Execution, Implementation, Implementations, Instances


class Fold2000CommonMidpointDifferentialEvolution(Execution):
    EXECUTION_DATA: Dict[Implementation, Dict[AwsInstance, ExecutionData]] = {
        Implementations.SOLUTION_V20: {
            Instances.GTX_TITAN: ExecutionData(
                test_id='e7abbca',
                int_per_second=[3.45E+10, 3.02E+10, 3.24E+10, 3.14E+10, 3.10E+10, 3.05E+10,
                                3.05E+10, 3.03E+10, 3.03E+10, 3.03E+10],
                total_execution_time=[66.184, 75.1546, 70.3219, 72.4719, 73.4658, 74.2119,
                                      74.6093, 74.7435, 75.0069, 74.7772],
                kernel_execution_time=None
            ),
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='0447d1c',
                int_per_second=[1.21E+11, 1.21E+11,	1.21E+11],
                total_execution_time=[22.6273, 22.5033, 22.4844],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[1.28E+11, 1.27E+11, 1.27E+11, 1.27E+11, 1.27E+11],
                total_execution_time=[7.11247, 7.06753, 7.09233, 7.18468, 7.092042],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[2.51E+10, 2.51E+10, 2.50E+10, 2.51E+10, 2.51E+10],
                total_execution_time=[93.7896, 93.677, 93.9211, 93.8085, 93.8488],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[2.61E+10, 2.60E+10, 2.60E+10, 2.60E+10, 2.61E+10],
                total_execution_time=[14.4151, 14.4769, 14.3929, 14.599, 14.376],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='dcea037',
                int_per_second=[2.60E+10, 2.60E+10, 2.59E+10, 2.60E+10, 2.65E+10],
                total_execution_time=[12.9545, 12.5846, 12.8832, 12.8421, 12.2804],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='e7abbca',
                int_per_second=[2.53E+11, 2.53E+11, 2.53E+11],
                total_execution_time=[14.5667, 14.4752, 14.5267],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='d4e9b53e',
                int_per_second=[2.54E+11, 2.56E+11, 2.56E+11, 2.54E+11, 2.54E+11],
                total_execution_time=[6.10318, 6.08066, 6.02921, 6.00224, 6.16666],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour
            ),
        },
        Implementations.SOLUTION_V20_OPENCL: {
            Instances.G4DN_X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[1.34E+11, 1.33E+11, 1.33E+11, 1.33E+11, 1.33E+11],
                total_execution_time=[22.2663, 22.2722, 22.2345, 22.1559],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_X_LARGE.cost_per_hour
            ),
            Instances.G4DN_12X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[1.34E+11, 1.34E+11, 1.34E+11, 1.34E+11, 1.34E+11],
                total_execution_time=[7.56414, 7.36507, 7.36844, 7.43581],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.G4DN_12X_LARGE.cost_per_hour
            ),
            Instances.P2_X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.68E+10, 2.67E+10, 2.67E+10, 2.67E+10, 2.67E+10],
                total_execution_time=[90.223, 90.0294, 89.9881, 89.9741],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_X_LARGE.cost_per_hour
            ),
            Instances.P2_8X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.63E+10, 2.67E+10, 2.64E+10, 2.64E+10, 2.64E+10],
                total_execution_time=[14.6238, 14.4034, 14.6838, 14.8405],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_8X_LARGE.cost_per_hour
            ),
            Instances.P2_16X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.63E+10, 2.63E+10, 2.63E+10, 2.63E+10, 2.62E+10],
                total_execution_time=[13.1215, 13.0355, 13.1427, 13.0863],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P2_16X_LARGE.cost_per_hour
            ),
            Instances.P3_2X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.53E+11, 2.53E+11, 2.53E+11, 2.53E+11, 2.53E+11],
                total_execution_time=[17.1095, 17.0222, 17.09, 17.0548],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_2X_LARGE.cost_per_hour
            ),
            Instances.P3_8X_LARGE: ExecutionData(
                test_id='7587a524',
                int_per_second=[2.51E+11, 2.52E+11, 2.51E+11, 2.52E+11, 2.53E+11],
                total_execution_time=[7.20638, 7.0647, 7.18232, 7.13126],
                kernel_execution_time=None,
                instance_cost_per_hour=Instances.P3_8X_LARGE.cost_per_hour
            ),
        }
    }

    @staticmethod
    def compute_method() -> str:
        return 'de'

    @staticmethod
    def data_name() -> str:
        return 'fold2000'

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        __impl = Fold2000CommonMidpointDifferentialEvolution.EXECUTION_DATA[impl]
        return __impl.get(instance)

    @staticmethod
    def model() -> str:
        return 'cmp'

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
                                    exec_type=Fold2000CommonMidpointDifferentialEvolution,
                                    impl=Implementations.SOLUTION_V20)

    @staticmethod
    def plot_all():
        Fold2000CommonMidpointDifferentialEvolution.plot_interpolation_per_sec_and_exec_time()
