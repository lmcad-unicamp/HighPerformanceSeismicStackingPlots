from typing import List

from helpers.graph_helpers import GraphHelpers
from model.execution_data import AwsInstance, Instances, Implementations
from zocrs.fold2000_zocrs_greedy import Fold2000ZeroOffsetCommonReflectionSurfaceGreedy
from zocrs.fold2000_zocrs_de import Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution


class Fold2000ZeroOffsetCommonReflectionSurfaceGreedyAndDifferentialEvolution:

    @staticmethod
    def plot_execution_times():
        instances: List[AwsInstance] = [
            Instances.P2_X_LARGE,
            Instances.P2_8X_LARGE,
            Instances.P2_16X_LARGE,
            Instances.P3_2X_LARGE,
            Instances.P3_8X_LARGE,
            Instances.G4DN_X_LARGE,
            Instances.G4DN_12X_LARGE
        ]

        GraphHelpers.plot_execution_times_greedy_and_de(instances=instances,
                                                        de_exec_type=Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution,
                                                        greedy_exec_type=Fold2000ZeroOffsetCommonReflectionSurfaceGreedy,
                                                        impl=Implementations.SOLUTION_V20)
