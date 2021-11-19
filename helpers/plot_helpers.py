import locale
from typing import List, Dict

from matplotlib import rc
from matplotlib.ticker import LinearLocator

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np

from model.execution_data import AwsInstance, Implementation
from model.plot_model import LOCALE, Legends, GraphSize


class PlotHelpers:
    INTERPOLATION_PER_SEC_KEY: str = 'int_per_sec_key'
    INTERPOLATION_PER_SEC_STD_DEV_KEY: str = 'int_per_sec_std_dev_key'
    COST_KEY: str = 'cost_key'
    COST_STD_DEV_KEY: str = 'cost_std_dev_key'
    EXEC_TIME_KEY: str = 'exec_time_key'
    EXEC_TIME_STD_DEV_KEY: str = 'exec_time_std_dev_key'
    EXEC_TIME_THREADS_KEY: str = 'exec_time_threads_key'
    EXEC_TIME_THREADS_STD_DEV_KEY: str = 'exec_time_threads_std_dev_key'
    KERNEL_EXEC_TIME_KEY: str = 'kernel_exec_time_key'
    KERNEL_EXEC_TIME_STD_DEV_KEY: str = 'kernel_exec_time_std_dev_key'
    RELATIVE_PERF_KEY: str = 'relative_perf_key'
    RELATIVE_PERF_STD_DEV_KEY: str = 'relative_perf_std_dev_key'

    ROOT_IMAGE_DIR: str = 'images'

    N_TICKS = 6

    @staticmethod
    def print_int_per_sec(int_per_sec: float, ax) -> str:
        exp = np.floor(np.log10(ax.get_ylim()[1]))
        number = locale.format_string('%.2f', int_per_sec / (10 ** exp))
        return r'%s${\scriptstyle \times 10^{%d}}$' % (number, exp)

    @staticmethod
    def apply_general_settings():
        locale.setlocale(locale.LC_NUMERIC, LOCALE)
        rc('font', **{'family': 'serif', 'sans-serif': ['Computer Modern'], 'size': 16})
        rc('text', usetex=True)
        rc('axes.formatter', use_locale=True)

    @staticmethod
    def round_axes_up(ax, max_y: int = None):
        max_value = ax.get_ylim()[1] if max_y is None else max_y
        decimals = np.floor(np.log10(max_value))
        next_bigger = np.ceil(max_value / (10 ** decimals))
        ax.set_ylim(bottom=0, top=next_bigger * (10 ** decimals))
        ax.yaxis.set_major_locator(LinearLocator(PlotHelpers.N_TICKS))

    @staticmethod
    def save_plot(figure, filename_to_save: str = None):
        if filename_to_save is not None:
            figure.savefig(filename_to_save, format='svg', bbox_inches='tight')
            print('Saved {} successfully'.format(filename_to_save))

    @staticmethod
    def disable_top_border(axes):
        axes.spines['top'].set_visible(False)

    @staticmethod
    def draw_arrows(ax, arrows, xy_coord, width):
        for arrow in arrows:
            from_instance = arrow[0]
            to_instance = arrow[1]

            xy_from = xy_coord[from_instance.name]
            xy_to = xy_coord[to_instance.name]

            x_text = (xy_from[0] + xy_to[0] + width / 2) / 2
            y_text = (xy_from[1] + xy_to[1]) / 2

            ax.annotate(text="", xy=(xy_to[0], xy_to[1] + ax.get_ylim()[1] * 0.1), xycoords='data',
                        xytext=(xy_from[0] + width / 2, xy_from[1] + ax.get_ylim()[1] * 0.05), textcoords='data',
                        arrowprops=dict(color='red', arrowstyle="->", connectionstyle="arc3,rad=-.2", linewidth=2))

            ax.annotate(text=locale.format_string(r'%.1f$\times$', xy_from[1] / xy_to[1]),
                        xy=(x_text, y_text),
                        xytext=(0, 0),
                        textcoords="offset points",
                        ha='center',
                        va='bottom',
                        color="red")

    @staticmethod
    def plot_interpolations_per_sec_with_relative_performance(implementations: List[Implementation],
                                                              data_to_plot: Dict[str, List[float]],
                                                              max_y: int = None,
                                                              filename_to_save: str = None,
                                                              annotate: bool = False,
                                                              show: bool = False):
        plt.close()

        fig, int_per_sec_ax = plt.subplots(figsize=GraphSize.MIDDLE)
        relative_performance_ax = int_per_sec_ax.twinx()

        PlotHelpers.disable_top_border(int_per_sec_ax)
        PlotHelpers.disable_top_border(relative_performance_ax)

        tags = [impl.tag for impl in implementations]

        int_per_sec = data_to_plot[PlotHelpers.INTERPOLATION_PER_SEC_KEY]
        int_per_sec_std_dev = data_to_plot[PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY]
        relative_performance = data_to_plot[PlotHelpers.RELATIVE_PERF_KEY]

        rects = int_per_sec_ax.bar(tags,
                                   int_per_sec,
                                   yerr=int_per_sec_std_dev,
                                   capsize=5,
                                   label=Legends.AVG_INTERPOLATIONS_PER_SEC[LOCALE],
                                   color='lightgray')
        int_per_sec_ax.set_ylabel(Legends.INTERPOLATIONS_PER_SEC[LOCALE])

        relative_performance_ax.plot(tags,
                                     relative_performance,
                                     label=Legends.AVG_RELATIVE_PERFORMANCE[LOCALE],
                                     marker='o',
                                     color='blue')
        relative_performance_ax.set_ylabel(Legends.RELATIVE_PERFORMANCE[LOCALE])
        relative_performance_ax.set_ylim(bottom=0)

        if annotate:
            for rect in rects:
                height = rect.get_height()
                int_per_sec_ax.annotate(PlotHelpers.print_int_per_sec(height, int_per_sec_ax),
                                        xy=(rect.get_x() + rect.get_width() / 2, height),
                                        xytext=(0, 12.5),
                                        textcoords="offset points",
                                        ha='center',
                                        va='bottom')

            for xy in zip(tags, relative_performance):
                relative_performance_ax.annotate(text=locale.format_string('%.2f', xy[1]),
                                                 xy=xy,
                                                 textcoords='offset points',
                                                 xytext=(0, -20),
                                                 va='center',
                                                 ha='center',
                                                 color='blue')

        PlotHelpers.round_axes_up(int_per_sec_ax)
        PlotHelpers.round_axes_up(relative_performance_ax, max_y)

        fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), columnspacing=0, ncol=4,
                   bbox_transform=int_per_sec_ax.transAxes)
        plt.grid(linestyle=':')

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_interpolations_per_sec_with_trace_use(treatments: List[str],
                                                   int_per_sec: List[float],
                                                   trace_use: List[float],
                                                   filename_to_save: str = None,
                                                   show: bool = False):
        plt.close()

        fig, int_per_sec_ax = plt.subplots(figsize=(7, 5))
        trace_use_ax = int_per_sec_ax.twinx()

        # PlotHelpers.disable_top_border(int_per_sec_ax)
        # PlotHelpers.disable_top_border(trace_use_ax)

        int_per_sec_ax.bar(treatments, int_per_sec,
                           label=Legends.AVG_INTERPOLATIONS_PER_SEC[LOCALE],
                           color='lightgray')
        int_per_sec_ax.set_ylabel(Legends.INTERPOLATIONS_PER_SEC[LOCALE])

        trace_use_ax.plot(treatments, trace_use,
                          label=Legends.AVG_TRACE_USE[LOCALE],
                          marker='o',
                          color='black')
        trace_use_ax.set_ylabel(Legends.TRACE_USE[LOCALE])

        for xy in zip(treatments, trace_use):
            trace_use_ax.annotate(text=locale.format_string('%.2f', xy[1]),
                                  xy=xy,
                                  textcoords='offset points',
                                  xytext=(0, 10),
                                  va='center',
                                  ha='center',
                                  color='black')

        PlotHelpers.round_axes_up(int_per_sec_ax)
        PlotHelpers.round_axes_up(trace_use_ax, 100)

        fig.legend(loc='upper left', bbox_to_anchor=(0, 1), bbox_transform=int_per_sec_ax.transAxes)
        plt.grid(linestyle=':')

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_thread_benchmark_with_exec_time(thread_counts: List[str],
                                             execution_times: Dict[AwsInstance, Dict[str, List[float]]],
                                             filename_to_save: str = None,
                                             show: bool = False):
        plt.close()

        fig, exec_time_ax = plt.subplots(figsize=GraphSize.MIDDLE)

        PlotHelpers.disable_top_border(exec_time_ax)

        markers = 'o^sD'

        exec_time_ax.set_ylabel(Legends.SECONDS[LOCALE])
        exec_time_ax.set_xlabel(Legends.THREAD_COUNT[LOCALE])

        for index, (instance, execution_time_map) in enumerate(execution_times.items()):
            exec_time_ax.errorbar(x=thread_counts,
                                  y=execution_time_map[PlotHelpers.EXEC_TIME_THREADS_KEY],
                                  yerr=execution_time_map[PlotHelpers.EXEC_TIME_THREADS_STD_DEV_KEY],
                                  capsize=5,
                                  label=instance.name,
                                  marker=markers[index])

        # exec_time_ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.30), fancybox=True, shadow=True, ncol=8)

        PlotHelpers.round_axes_up(exec_time_ax)

        plt.grid(linestyle=':')

        fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.125), columnspacing=0, ncol=5,
                   bbox_transform=exec_time_ax.transAxes)

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_interpolation_per_sec_and_total_exec_time(data_map: Dict[AwsInstance, Dict[str, float]],
                                                       filename_to_save: str = None,
                                                       annotate: bool = False,
                                                       show: bool = False):
        plt.close()

        fig, int_per_sec_ax = plt.subplots(figsize=(18, 6))
        total_exec_ax = int_per_sec_ax.twinx()

        PlotHelpers.disable_top_border(int_per_sec_ax)
        PlotHelpers.disable_top_border(total_exec_ax)

        instance_names: List[str] = []
        int_per_sec: List[float] = []
        int_per_sec_std_dev: List[float] = []
        total_exec: List[float] = []
        total_exec_std_dev: List[float] = []

        for instance, data in data_map.items():
            instance_names.append(instance.name)
            int_per_sec.append(data[PlotHelpers.INTERPOLATION_PER_SEC_KEY])
            int_per_sec_std_dev.append(data[PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY])
            total_exec.append(data[PlotHelpers.EXEC_TIME_KEY])
            total_exec_std_dev.append(data[PlotHelpers.EXEC_TIME_STD_DEV_KEY])

        x = np.arange(len(instance_names))
        width = 0.450

        int_pec_sec_rects = int_per_sec_ax.bar(x - width / 2,
                                               int_per_sec,
                                               yerr=int_per_sec_std_dev,
                                               capsize=5,
                                               width=width,
                                               label=Legends.AVG_INTERPOLATIONS_PER_SEC[LOCALE],
                                               color='darkgray')
        int_per_sec_ax.set_ylabel(Legends.INTERPOLATIONS_PER_SEC_PER_GPU[LOCALE])
        int_per_sec_ax.set_xticks(x)
        int_per_sec_ax.set_xticklabels(instance_names)

        total_exec_rects = total_exec_ax.bar(x + width / 2,
                                             total_exec,
                                             yerr=total_exec_std_dev,
                                             capsize=5,
                                             width=width,
                                             label=Legends.AVG_TOTAL_EXEC_TIME[LOCALE],
                                             color='lightgray')
        total_exec_ax.set_ylabel(Legends.SECONDS[LOCALE])

        if annotate:
            for rect in int_pec_sec_rects:
                height = rect.get_height()
                int_per_sec_ax.annotate(PlotHelpers.print_int_per_sec(height, int_per_sec_ax),
                                        xy=(rect.get_x() + rect.get_width() / 2, height),
                                        xytext=(0, 7.5),
                                        textcoords="offset points",
                                        ha='center',
                                        va='bottom',
                                        zorder=1000)

            for instance, rect in zip(instance_names, total_exec_rects):
                height = rect.get_height()
                total_exec_ax.annotate(locale.format_string('%.2f', height),
                                       xy=(rect.get_x() + rect.get_width() / 2, height),
                                       xytext=(0, 7.5),
                                       textcoords="offset points",
                                       ha='center',
                                       va='bottom',
                                       path_effects=[pe.withStroke(linewidth=4, foreground="white")])

        fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5, bbox_transform=int_per_sec_ax.transAxes)

        PlotHelpers.round_axes_up(int_per_sec_ax)
        PlotHelpers.round_axes_up(total_exec_ax)

        plt.grid(linestyle=':')
        plt.xticks(fontsize=20)

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_exec_time(data_map: Dict[AwsInstance, Dict[str, float]],
                       filename_to_save: str = None,
                       annotate: bool = False,
                       show: bool = False):
        plt.close()

        fig, total_exec_ax = plt.subplots(figsize=GraphSize.MIDDLE)

        PlotHelpers.disable_top_border(total_exec_ax)

        instance_names = []
        total_exec = []
        total_exec_std_dev = []

        for instance, data in data_map.items():
            instance_names.append(instance.name)
            total_exec.append(data[PlotHelpers.EXEC_TIME_KEY])
            total_exec_std_dev.append(data[PlotHelpers.EXEC_TIME_STD_DEV_KEY])

        x = np.arange(len(instance_names))

        total_exec_rects = total_exec_ax.bar(x,
                                             total_exec,
                                             yerr=total_exec_std_dev,
                                             capsize=5,
                                             label=Legends.AVG_TOTAL_EXEC_TIME[LOCALE],
                                             color='lightgray')
        total_exec_ax.set_ylabel(Legends.SECONDS[LOCALE])
        total_exec_ax.set_xticks(x)
        total_exec_ax.set_xticklabels(instance_names)

        if annotate:
            for instance, rect in zip(instance_names, total_exec_rects):
                height = rect.get_height()
                total_exec_ax.annotate(locale.format_string('%.2f', height),
                                       xy=(rect.get_x() + rect.get_width() / 2, height),
                                       xytext=(0, 10.5),
                                       textcoords="offset points",
                                       ha='center',
                                       va='bottom',
                                       path_effects=[pe.withStroke(linewidth=4, foreground="white")])

        fig.legend(loc='upper right',
                   bbox_to_anchor=(1, 1),
                   bbox_transform=total_exec_ax.transAxes)

        PlotHelpers.round_axes_up(total_exec_ax)

        plt.grid(linestyle=':')
        plt.xticks(fontsize=20, rotation=30)

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_interpolation_per_sec_cuda_opencl(data_to_plot_cuda: Dict[AwsInstance, Dict[str, float]],
                                               data_to_plot_opencl: Dict[AwsInstance, Dict[str, float]],
                                               filename_to_save: str = None,
                                               annotate: bool = False,
                                               show: bool = False):

        plt.close()

        fig, int_per_sec_ax = plt.subplots(figsize=GraphSize.LARGE)

        PlotHelpers.disable_top_border(int_per_sec_ax)

        instance_names = []
        int_per_sec_cuda = []
        int_per_sec_std_dev_cuda = []
        int_per_sec_opencl = []
        int_per_sec_std_dev_opencl = []

        for instance, data in data_to_plot_cuda.items():
            instance_names.append(instance.name)
            int_per_sec_cuda.append(data_to_plot_cuda[instance][PlotHelpers.INTERPOLATION_PER_SEC_KEY])
            int_per_sec_std_dev_cuda.append(
                data_to_plot_cuda[instance][PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY])

            int_per_sec_opencl.append(data_to_plot_opencl[instance][PlotHelpers.INTERPOLATION_PER_SEC_KEY])
            int_per_sec_std_dev_opencl.append(
                data_to_plot_opencl[instance][PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY])

        x = np.arange(len(instance_names))
        width = 0.450

        int_pec_sec_cuda_rects = int_per_sec_ax.bar(x - width / 2,
                                                    int_per_sec_cuda,
                                                    yerr=int_per_sec_std_dev_cuda,
                                                    capsize=5,
                                                    width=width,
                                                    label=Legends.AVG_INTERPOLATIONS_PER_SEC[LOCALE] + ' - CUDA',
                                                    color='lightgray')

        int_per_sec_ax.set_ylabel(Legends.INTERPOLATIONS_PER_SEC_PER_GPU[LOCALE])
        int_per_sec_ax.set_xticks(x)
        int_per_sec_ax.set_xticklabels(instance_names)

        int_pec_sec_opencl_rects = int_per_sec_ax.bar(x + width / 2,
                                                      int_per_sec_opencl,
                                                      yerr=int_per_sec_std_dev_opencl,
                                                      capsize=5,
                                                      width=width,
                                                      label=Legends.AVG_INTERPOLATIONS_PER_SEC[LOCALE] + ' - OpenCL',
                                                      color='darkgray')

        if annotate:
            for index, rect in enumerate(int_pec_sec_cuda_rects):
                height = rect.get_height()
                int_per_sec_ax.annotate(PlotHelpers.print_int_per_sec(int_per_sec=height,
                                                                      ax=int_per_sec_ax),
                                        xy=(rect.get_x() + rect.get_width() * 2 / 5, height),
                                        xytext=(0, 3),
                                        textcoords="offset points",
                                        ha='center',
                                        va='bottom',
                                        zorder=1000)

            for index, rect in enumerate(int_pec_sec_opencl_rects):
                height = rect.get_height()
                int_per_sec_ax.annotate(PlotHelpers.print_int_per_sec(int_per_sec=height,
                                                                      ax=int_per_sec_ax),
                                        xy=(rect.get_x() + rect.get_width() * 3 / 5, height),
                                        xytext=(0, 3),
                                        textcoords="offset points",
                                        ha='center',
                                        va='bottom',
                                        path_effects=[pe.withStroke(linewidth=4, foreground="white")])

        fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5, bbox_transform=int_per_sec_ax.transAxes)

        PlotHelpers.round_axes_up(int_per_sec_ax)

        plt.grid(linestyle=':')
        plt.xticks(fontsize=20)

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_total_execution_time_cuda_opencl(data_to_plot_cuda: Dict,
                                              data_to_plot_opencl: Dict,
                                              filename_to_save: str = None,
                                              annotate: bool = False,
                                              show: bool = False):

        plt.close()

        fig, exec_time_ax = plt.subplots(figsize=(18, 6))

        instance_names = []
        exec_time_cuda = []
        exec_time_opencl = []
        exec_time_std_dev_cuda = []
        exec_time_std_dev_opencl = []

        for instance, data in data_to_plot_cuda.items():
            instance_names.append(instance.name)
            exec_time_cuda.append(data_to_plot_cuda[instance][PlotHelpers.EXEC_TIME_KEY])
            exec_time_std_dev_cuda.append(data_to_plot_cuda[instance][PlotHelpers.EXEC_TIME_STD_DEV_KEY])
            exec_time_opencl.append(data_to_plot_opencl[instance][PlotHelpers.EXEC_TIME_KEY])
            exec_time_std_dev_opencl.append(data_to_plot_opencl[instance][PlotHelpers.EXEC_TIME_STD_DEV_KEY])

        x = np.arange(len(instance_names))
        width = 0.450

        exec_time_cuda_rects = exec_time_ax.bar(x - width / 2,
                                                exec_time_cuda,
                                                yerr=exec_time_std_dev_cuda,
                                                capsize=5,
                                                width=width,
                                                label=Legends.AVG_TOTAL_EXEC_TIME[LOCALE] + ' - CUDA',
                                                color='black',
                                                ecolor='blue')

        exec_time_ax.set_ylabel(Legends.SECONDS[LOCALE])
        exec_time_ax.set_xticks(x)
        exec_time_ax.set_xticklabels(instance_names)

        exec_opencl_rects = exec_time_ax.bar(x + width / 2,
                                             exec_time_opencl,
                                             yerr=exec_time_std_dev_opencl,
                                             capsize=5,
                                             width=width,
                                             label=Legends.AVG_TOTAL_EXEC_TIME[LOCALE] + ' - OpenCL',
                                             color='lightgray')

        if annotate:
            for rect in exec_time_cuda_rects:
                height = rect.get_height()
                exec_time_ax.annotate(locale.format_string('%.2f', height),
                                      xy=(rect.get_x() + rect.get_width() / 2, height),
                                      xytext=(0, 3),
                                      textcoords="offset points",
                                      ha='center',
                                      va='bottom',
                                      zorder=1000)

            for rect in exec_opencl_rects:
                height = rect.get_height()
                exec_time_ax.annotate(locale.format_string('%.2f', height),
                                      xy=(rect.get_x() + rect.get_width() / 2, height),
                                      xytext=(0, 3),
                                      textcoords="offset points",
                                      ha='center',
                                      va='bottom',
                                      path_effects=[pe.withStroke(linewidth=4, foreground="white")])

        fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5, bbox_transform=exec_time_ax.transAxes)

        PlotHelpers.round_axes_up(exec_time_ax)

        plt.grid(linestyle=':')
        plt.xticks(fontsize=20)

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_cost_with_total_exec_time(data_to_plot: Dict[AwsInstance, Dict[str, float]],
                                       filename_to_save: str = None,
                                       annotate: bool = False,
                                       show: bool = False):
        plt.close()

        fig, total_exec_time_ax = plt.subplots(figsize=GraphSize.MIDDLE)
        cost_ax = total_exec_time_ax.twinx()

        node_counts: List[str] = []
        total_exec_times: List[float] = []
        total_exec_time_std_devs: List[float] = []
        costs: List[float] = []
        cost_std_devs: List[float] = []

        PlotHelpers.disable_top_border(total_exec_time_ax)
        PlotHelpers.disable_top_border(cost_ax)

        for instance, values in data_to_plot.items():
            node_counts.append('{}'.format(instance.node_count))
            total_exec_times.append(values.get(PlotHelpers.EXEC_TIME_KEY))
            total_exec_time_std_devs.append(values.get(PlotHelpers.EXEC_TIME_STD_DEV_KEY))
            costs.append(values.get(PlotHelpers.COST_KEY))
            cost_std_devs.append(values.get(PlotHelpers.COST_STD_DEV_KEY))

        total_exec_time_ax.errorbar(x=node_counts,
                                    y=total_exec_times,
                                    yerr=total_exec_time_std_devs,
                                    capsize=5,
                                    label=Legends.AVG_TOTAL_EXEC_TIME[LOCALE],
                                    marker='s',
                                    color='gray')

        total_exec_time_ax.set_ylabel(Legends.SECONDS[LOCALE])
        total_exec_time_ax.set_xlabel(Legends.NODE_COUNT[LOCALE])

        cost_ax.errorbar(x=node_counts,
                         y=costs,
                         yerr=cost_std_devs,
                         capsize=5,
                         label=Legends.COST[LOCALE],
                         marker='o',
                         color='black')

        cost_ax.set_ylabel(Legends.DOLLARS[LOCALE])
        cost_ax.set_ylim(bottom=0, top=1.1 * np.max(costs))

        if annotate:
            for xy in zip(node_counts, total_exec_times):
                total_exec_time_ax.annotate(locale.format_string('%.1f', xy[1]),
                                            xy=xy,
                                            textcoords='offset points',
                                            xytext=(0, -17.5),
                                            va='center',
                                            ha='center',
                                            color='gray',
                                            path_effects=[pe.withStroke(linewidth=4, foreground="white")])

            for xy in zip(node_counts, costs):
                cost_ax.annotate(text=locale.format_string('%.3f', xy[1]),
                                 xy=xy,
                                 textcoords='offset points',
                                 xytext=(0, 17.5),
                                 va='center',
                                 ha='center',
                                 color='black',
                                 path_effects=[pe.withStroke(linewidth=4, foreground="white")])

        PlotHelpers.round_axes_up(total_exec_time_ax)
        PlotHelpers.round_axes_up(cost_ax)

        fig.legend(loc='upper center',
                   bbox_to_anchor=(0.5, 1.15),
                   ncol=5,
                   columnspacing=1,
                   bbox_transform=total_exec_time_ax.transAxes)

        plt.grid(linestyle=':')

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_relative_performance(data_to_plot: Dict[AwsInstance, Dict[str, float]],
                                  filename_to_save: str = None,
                                  annotate: bool = False,
                                  show: bool = False):
        plt.close()

        fig, relative_perf_ax = plt.subplots(figsize=GraphSize.MIDDLE)

        PlotHelpers.disable_top_border(relative_perf_ax)

        node_counts: List[str] = []
        relative_perfs: List[float] = []
        relative_perf_std_devs: List[float] = []

        for instance, values in data_to_plot.items():
            node_counts.append('{}'.format(instance.node_count))
            relative_perfs.append(values.get(PlotHelpers.RELATIVE_PERF_KEY))
            relative_perf_std_devs.append(values.get(PlotHelpers.RELATIVE_PERF_STD_DEV_KEY))

        relative_perf_ax.errorbar(x=node_counts,
                                  y=relative_perfs,
                                  yerr=relative_perf_std_devs,
                                  capsize=5,
                                  label=Legends.AVG_RELATIVE_PERFORMANCE[LOCALE],
                                  marker='o',
                                  color='black')
        relative_perf_ax.set_ylabel(Legends.RELATIVE_PERFORMANCE[LOCALE])
        relative_perf_ax.set_xlabel(Legends.NODE_COUNT[LOCALE])

        if annotate:
            for xy in zip(node_counts, relative_perfs):
                relative_perf_ax.annotate(text=locale.format_string('%.2f', xy[1]),
                                          xy=xy,
                                          textcoords='offset points',
                                          xytext=(-25, 0) if xy[0] == '8' else (25, 0),
                                          va='center',
                                          ha='center',
                                          color='black',
                                          path_effects=[pe.withStroke(linewidth=4, foreground="white")])

        PlotHelpers.round_axes_up(relative_perf_ax)

        relative_perf_ax.legend(loc='upper left')

        plt.grid(linestyle=':')

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_interpolation_per_sec(instances: List[AwsInstance],
                                   data_to_plot: Dict[AwsInstance, Dict[Implementation, Dict[str, float]]],
                                   implementations: List[Implementation],
                                   filename_to_save: str = None,
                                   annotate: bool = False,
                                   show: bool = False):
        plt.close()

        instance_names: List[str] = [instance.name for instance in instances]

        colors = ['lightgray', 'darkgray', 'black']
        fig, int_per_sec_ax = plt.subplots(figsize=GraphSize.MIDDLE)

        PlotHelpers.disable_top_border(int_per_sec_ax)

        data_size = len(implementations)
        x = np.arange(len(instance_names))
        width = 0.95 / data_size

        for index, impl in enumerate(implementations):
            int_per_sec_rates = [data_to_plot[instance][impl][PlotHelpers.INTERPOLATION_PER_SEC_KEY]
                                 for instance in instances]
            int_per_sec_dev_stds = [data_to_plot[instance][impl][PlotHelpers.INTERPOLATION_PER_SEC_STD_DEV_KEY]
                                    for instance in instances]

            x_offset = (index - data_size / 2) * width + width / 2

            int_pec_sec_rects = int_per_sec_ax.bar(x + x_offset,
                                                   int_per_sec_rates,
                                                   yerr=int_per_sec_dev_stds,
                                                   capsize=5,
                                                   width=width,
                                                   label=impl.tag,
                                                   color=colors[index])

            if annotate:
                for rect in int_pec_sec_rects:
                    height = rect.get_height()
                    if height > 0:
                        int_per_sec_ax.annotate(PlotHelpers.print_int_per_sec(height, int_per_sec_ax),
                                                xy=(rect.get_x() + rect.get_width() / 2, height),
                                                xytext=(0, 4.5),
                                                textcoords="offset points",
                                                ha='center',
                                                va='bottom',
                                                color='black',
                                                path_effects=[pe.withStroke(linewidth=4, foreground="white")])

        int_per_sec_ax.set_ylabel(Legends.INTERPOLATIONS_PER_SEC_PER_GPU[LOCALE])
        int_per_sec_ax.set_xticks(x)
        int_per_sec_ax.set_xticklabels(instance_names)

        PlotHelpers.round_axes_up(int_per_sec_ax)

        plt.grid(linestyle=':')
        fig.legend(loc='upper left', bbox_to_anchor=(0, 1), bbox_transform=int_per_sec_ax.transAxes)

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_execution_time_with_relative_performance(instances: List[AwsInstance],
                                                      data_to_plot: Dict[
                                                          AwsInstance, Dict[Implementation, Dict[str, float]]],
                                                      implementations: List[Implementation],
                                                      our_impl: Implementation,
                                                      filename_to_save: str = None,
                                                      annotate: bool = False,
                                                      show: bool = False):
        plt.close()

        colors = ['lightgray', 'darkgray', 'black']
        fig, kernel_execution_times_ax = plt.subplots(figsize=GraphSize.MIDDLE)
        relative_performance_ax = kernel_execution_times_ax.twinx()

        PlotHelpers.disable_top_border(kernel_execution_times_ax)
        PlotHelpers.disable_top_border(relative_performance_ax)

        instance_names: List[str] = [instance.name for instance in instances]

        data_size = len(instance_names)
        x = np.arange(data_size)
        width = 1.2 / data_size

        for index, impl in enumerate(implementations):
            kernel_execution_times = [data_to_plot[instance][impl][PlotHelpers.KERNEL_EXEC_TIME_KEY]
                                      for instance in instances]
            kernel_execution_time_dev_stds = [data_to_plot[instance][impl][PlotHelpers.KERNEL_EXEC_TIME_STD_DEV_KEY]
                                              for instance in instances]

            x_offset = (index - data_size / 2) * width + width / 2

            int_pec_sec_rects = kernel_execution_times_ax.bar(x + x_offset,
                                                              kernel_execution_times,
                                                              yerr=kernel_execution_time_dev_stds,
                                                              capsize=5,
                                                              width=width,
                                                              label=impl.tag,
                                                              color=colors[index])

            if annotate:
                for rect in int_pec_sec_rects:
                    height = rect.get_height()
                    if height > 0:
                        kernel_execution_times_ax.annotate(locale.format_string('%.2f', height),
                                                           xy=(rect.get_x() + rect.get_width() / 2, height),
                                                           xytext=(0, 10),
                                                           textcoords="offset points",
                                                           ha='center',
                                                           va='bottom',
                                                           color='black',
                                                           path_effects=[
                                                               pe.withStroke(linewidth=4, foreground="white")])

        kernel_execution_times_ax.set_ylabel(Legends.SECONDS[LOCALE])
        kernel_execution_times_ax.set_xticks(x)
        kernel_execution_times_ax.set_xticklabels(instance_names)

        relative_performances = [data_to_plot[instance][our_impl][PlotHelpers.RELATIVE_PERF_KEY]
                                 for instance in instances]
        relative_performance_ax.plot(instance_names,
                                     relative_performances,
                                     marker='o',
                                     color='blue',
                                     label=Legends.AVG_RELATIVE_PERFORMANCE[LOCALE])
        relative_performance_ax.set_ylim(bottom=0)
        relative_performance_ax.set_ylabel(Legends.RELATIVE_PERFORMANCE[LOCALE])

        if annotate:
            for xy in zip(instance_names, relative_performances):
                relative_performance_ax.annotate(text=locale.format_string('%.2f', xy[1]),
                                                 xy=xy,
                                                 textcoords='offset points',
                                                 xytext=(0, 12.5),
                                                 va='center',
                                                 ha='center',
                                                 color='blue',
                                                 path_effects=[pe.withStroke(linewidth=4, foreground="white")])

        PlotHelpers.round_axes_up(kernel_execution_times_ax)
        PlotHelpers.round_axes_up(relative_performance_ax)

        plt.grid(linestyle=':')

        fig.legend(loc='upper center',
                   bbox_to_anchor=(0.5, 1.15),
                   fancybox=True,
                   shadow=True,
                   ncol=4,
                   columnspacing=0.5,
                   bbox_transform=kernel_execution_times_ax.transAxes)

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_execution_breakdown_stacked_bar(data_to_plot: Dict, labels: List[str], filename_to_save: str = None):
        plt.close()
        fig, execution_break_times_ax = plt.subplots(figsize=(18, 6))

        colors = ['lightblue', 'lightgreen', 'darkgray', 'black', 'lightgray']
        instance_names = []

        for instance in data_to_plot.keys():
            instance_names.append(instance.name)

        for idx, label in enumerate(labels):
            exec_data = []
            for breakdown_data in data_to_plot.values():
                exec_data.append(breakdown_data[idx])

            execution_break_times_ax.bar(instance_names, exec_data, label=label)

        PlotHelpers.round_axes_up(execution_break_times_ax)

        plt.grid(linestyle=':')

        fig.legend(loc='upper right',
                   bbox_to_anchor=(1, 1),
                   bbox_transform=execution_break_times_ax.transAxes)

        # plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)

    @staticmethod
    def plot_exec_time_de_greedy(instance_names: List[str],
                                 de_exec_times: List[float],
                                 de_exec_time_std_devs: List[float],
                                 greedy_exec_times: List[float],
                                 greedy_exec_time_std_devs: List[float],
                                 filename_to_save: str = None,
                                 annotate: bool = False,
                                 show: bool = False):
        plt.close()
        fig, execution_times_ax = plt.subplots(figsize=GraphSize.LARGE)

        PlotHelpers.disable_top_border(execution_times_ax)

        x = np.arange(len(instance_names))
        width = 0.450

        exec_time_de_rects = execution_times_ax.bar(x - width / 2,
                                                    de_exec_times,
                                                    yerr=de_exec_time_std_devs,
                                                    capsize=5,
                                                    width=width,
                                                    label=Legends.AVG_TOTAL_EXEC_TIME[LOCALE] + ' - ' + Legends.DE[
                                                        LOCALE],
                                                    color='lightgray')

        execution_times_ax.set_ylabel(Legends.SECONDS[LOCALE])
        execution_times_ax.set_xticks(x)
        execution_times_ax.set_xticklabels(instance_names)

        exec_de_rects = execution_times_ax.bar(x + width / 2,
                                               greedy_exec_times,
                                               yerr=greedy_exec_time_std_devs,
                                               capsize=5,
                                               width=width,
                                               label=Legends.AVG_TOTAL_EXEC_TIME[LOCALE] + ' - ' + Legends.GREEDY[
                                                   LOCALE],
                                               color='darkgray')

        if annotate:
            for rect in exec_time_de_rects:
                height = rect.get_height()
                execution_times_ax.annotate(locale.format_string('%.2f', height),
                                            xy=(rect.get_x() + rect.get_width() / 2, height),
                                            xytext=(0, 3),
                                            textcoords="offset points",
                                            ha='center',
                                            va='bottom',
                                            zorder=1000)

            for rect in exec_de_rects:
                height = rect.get_height()
                execution_times_ax.annotate(locale.format_string('%.2f', height),
                                            xy=(rect.get_x() + + rect.get_width() / 2, height),
                                            xytext=(0, 3),
                                            textcoords="offset points",
                                            ha='center',
                                            va='bottom',
                                            zorder=1000)

        PlotHelpers.round_axes_up(execution_times_ax)

        plt.grid(linestyle=':')

        fig.legend(loc='upper right',
                   bbox_to_anchor=(1, 1),
                   bbox_transform=execution_times_ax.transAxes)

        if show:
            plt.show()

        PlotHelpers.save_plot(fig, filename_to_save)
