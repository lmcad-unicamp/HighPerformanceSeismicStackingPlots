from cmp.fold2000_cmp_de import Fold2000CommonMidpointDifferentialEvolution
from cmp.fold2000_cmp_greedy import Fold2000CommonMidpointGreedy
from cmp.simple_synthetic_cmp_de import SimpleSyntheticCommonMidpointDifferentialEvolution
from cmp.simple_synthetic_cmp_greedy import SimpleSyntheticCommonMidpointGreedy
from helpers.plot_helpers import PlotHelpers
from heuristic.heuristic_efficiency import HeuristicEfficiency
from model.actions import Actions
from oct.fold2000_oct_de import Fold2000OffsetContinuationTrajectoryDifferentialEvolution
from oct.fold2000_oct_de_greedy import Fold2000OffsetContinuationTrajectoryGreedyAndDifferentialEvolution
from oct.fold2000_oct_de_spits import Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits
from oct.fold2000_oct_greedy import Fold2000OffsetContinuationTrajectoryGreedy
from oct.simple_synthetic_oct_de import SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolution
from oct.simple_synthetic_oct_de_spits import SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits
from oct.simple_synthetic_oct_greedy import SimpleSyntheticOffsetContinuationTrajectoryGreedy
from thread.thread_benchmark import ThreadBenchmark
from zocrs.fold2000_zocrs_de import Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution
from zocrs.fold2000_zocrs_de_greedy import Fold2000ZeroOffsetCommonReflectionSurfaceGreedyAndDifferentialEvolution
from zocrs.fold2000_zocrs_de_spits import Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits
from zocrs.fold2000_zocrs_greedy import Fold2000ZeroOffsetCommonReflectionSurfaceGreedy
from zocrs.simple_synthetic_zocrs_de import SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolution
from zocrs.simple_synthetic_zocrs_de_spits import \
    SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits
from zocrs.simple_synthetic_zocrs_greedy import SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy


def main(action: str = Actions.CREATE_PLOTS):

    if action == Actions.CREATE_PLOTS:

        PlotHelpers.apply_general_settings()

        ## Heuristic efficiency
        HeuristicEfficiency.plot_all()

        ## Thread benchmarking
        ThreadBenchmark.plot_all()

        ## CMP
        # Greedy
        SimpleSyntheticCommonMidpointGreedy.plot_all()
        Fold2000CommonMidpointGreedy.plot_all()

        # DE
        SimpleSyntheticCommonMidpointDifferentialEvolution.plot_all()
        Fold2000CommonMidpointDifferentialEvolution.plot_all()

        ## ZOCRS
        # Greedy
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy.plot_all()
        Fold2000ZeroOffsetCommonReflectionSurfaceGreedy.plot_all()

        # DE + Greedy
        Fold2000ZeroOffsetCommonReflectionSurfaceGreedyAndDifferentialEvolution.plot_execution_times()

        # DE
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolution.plot_all()
        Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution.plot_all()

        # SPITS
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.plot_cost_and_exec_time()
        Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.plot_cost_and_exec_time()

        ## OCT
        # Greedy
        SimpleSyntheticOffsetContinuationTrajectoryGreedy.plot_all()
        Fold2000OffsetContinuationTrajectoryGreedy.plot_all()

        # DE + Greedy
        Fold2000OffsetContinuationTrajectoryGreedyAndDifferentialEvolution.plot_execution_times()

        # DE
        SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolution.plot_all()
        Fold2000OffsetContinuationTrajectoryDifferentialEvolution.plot_all()

        # SPITS
        SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits.plot_all()
        Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits.plot_all()

    elif action == Actions.SEARCH_FOR_FILES:

        ## Heuristic efficiency
        HeuristicEfficiency.search_for_execution_data()

        ## Thread benchmarking
        ThreadBenchmark.search_for_execution_data()

        ## CMP
        # Greedy
        SimpleSyntheticCommonMidpointGreedy.search_for_data_and_persist()
        Fold2000CommonMidpointGreedy.search_for_data_and_persist()

        # DE
        SimpleSyntheticCommonMidpointDifferentialEvolution.search_for_data_and_persist()
        Fold2000CommonMidpointDifferentialEvolution.search_for_data_and_persist()

        ## ZOCRS
        # Greedy
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceGreedy.search_for_data_and_persist()
        Fold2000ZeroOffsetCommonReflectionSurfaceGreedy.search_for_data_and_persist()

        # DE
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolution.search_for_data_and_persist()
        Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolution.search_for_data_and_persist()

        # SPITS
        SimpleSyntheticZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.search_for_data_and_persist()
        Fold2000ZeroOffsetCommonReflectionSurfaceDifferentialEvolutionSpits.search_for_data_and_persist()

        ## OCT
        # Greedy
        SimpleSyntheticOffsetContinuationTrajectoryGreedy.search_for_data_and_persist()
        Fold2000OffsetContinuationTrajectoryGreedy.search_for_data_and_persist()

        # DE
        SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolution.search_for_data_and_persist()
        Fold2000OffsetContinuationTrajectoryDifferentialEvolution.search_for_data_and_persist()

        # SPITS
        SimpleSyntheticOffsetContinuationTrajectoryDifferentialEvolutionSpits.search_for_data_and_persist()
        Fold2000OffsetContinuationTrajectoryDifferentialEvolutionSpits.search_for_data_and_persist()


if __name__ == '__main__':
    main(action=Actions.CREATE_PLOTS)
