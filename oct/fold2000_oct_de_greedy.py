from typing import List

from helpers.graph_helpers import GraphHelpers
from model.execution_data import AwsInstance, Instances, Implementations
from oct.fold2000_oct_de import Fold2000OffsetContinuationTrajectoryDifferentialEvolution
from oct.fold2000_oct_greedy import Fold2000OffsetContinuationTrajectoryGreedy


class Fold2000OffsetContinuationTrajectoryGreedyAndDifferentialEvolution:

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
                                                        de_exec_type=Fold2000OffsetContinuationTrajectoryDifferentialEvolution,
                                                        greedy_exec_type=Fold2000OffsetContinuationTrajectoryGreedy,
                                                        impl=Implementations.SOLUTION_V20)
