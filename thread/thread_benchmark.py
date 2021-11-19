from typing import List, Dict

from helpers.graph_helpers import GraphHelpers
from model.execution_data import Instances, AwsInstance


class ThreadBenchmark:

    THREAD_COUNT: List[str] = ['32', '64', '128', '256', '512', '1024']

    SIMPLE_SYNTHETIC_CMP_GREEDY_EXEC_TIME: Dict[AwsInstance, List[float]] = {
        Instances.GTX_TITAN: [
            [16.0941, 17.209, 18.1796, 18.0212],
            [16.6235, 13.9222, 14.2672, 14.1732],
            [20.1337, 18.6207, 19.2897, 19.3025],
            [19.9343, 19.1309, 19.3138, 19.3228],
            [20.0997, 18.7159, 19.2312, 19.2212],
            [20.5071, 19.3033, 19.3451, 19.3096]
        ],
        Instances.G4DN_X_LARGE: [
            [7.23815, 8.97167, 6.61072, 6.65964],
            [12.6375, 12.2058, 11.7549, 11.8387],
            [12.2335, 11.6145, 11.448, 11.5455],
            [11.2327, 10.6027, 10.6599, 10.6918],
            [11.0262, 10.3279, 10.4626, 10.2628],
            [12.8455, 12.4213, 12.5562]
        ],
        Instances.P2_X_LARGE: [
            [23.744, 23.812, 23.8982, 21.4328, 21.0844],
            [24.7094, 22.0718, 22.1973, 22.122, 22.2674],
            [32.3675, 29.6607, 29.7475, 29.8192, 29.8823],
            [32.121, 29.7266, 29.6252, 29.6406, 29.726],
            [31.724, 29.1666, 29.2896, 29.3521, 29.3199],
            [31.8684, 29.6051, 29.5272, 29.6409]
        ],
        Instances.P3_2X_LARGE: [
            [6.78796, 7.93556, 5.91527, 6.06395, 6.06806, 6.06311],
            [8.46048, 7.68194, 7.53013, 7.73606, 7.54856, 7.5622],
            [8.49343, 7.69223, 7.66541, 7.60357, 7.62645, 7.58494],
            [8.35984, 7.37844, 7.40908, 7.3886, 7.52543, 7.38147],
            [8.09374, 7.36729, 7.33761, 7.29728, 7.32779, 7.22125],
            [8.36102, 7.6699, 7.55315, 7.54598, 7.71295, 7.66589]
        ],
    }

    SIMPLE_SYNTHETIC_ZO_CRS_DE_EXEC_TIME: Dict[AwsInstance, List[float]] = {
        Instances.GTX_TITAN: [
            [341.715, 323.953, 340.544, 340.26],
            [331.479, 328.047, 330.086, 330.233],
            [342.258, 340.859, 339.709, 341.118],
            [345.527, 342.253, 342.258, 342.396],
            [351.051, 347.53, 350.496, 349.167],
            [357.724, 354.922, 357.327, 357.118]
        ],
        Instances.G4DN_X_LARGE: [
            [81.3376, 75.7886, 80.9322, 81.303],
            [121.286, 122.804, 122.866, 122.439],
            [127.265, 128.441, 128.283, 128.615],
            [112.002, 115.335, 115.414, 116.177],
            [104.488, 108.023, 109.377, 110.803],
            [132.471, 130.928, 131.198]],
        Instances.P2_X_LARGE: [
            [420.241, 414.424, 416.2, 417.424, 417.887],
            [405.961, 396.746, 401.289, 401.541, 402.45],
            [416.287, 419.247, 423.817, 424.162, 424.08],
            [418.592, 420.254, 424.694, 425.178, 425.07],
            [421.916, 426.532, 429.216, 429.281, 429.497],
            [433.632, 438.396, 438.56, 438.699]
        ],
        Instances.P3_2X_LARGE: [
            [63.6672, 63.1299, 63.1939, 63.3884, 63.2822, 63.2962],
            [62.2783, 61.4904, 61.8894, 61.7885, 61.711, 61.5458],
            [60.1591, 59.2268, 59.158, 59.3696, 59.0944, 59.1863],
            [56.4195, 55.4668, 55.2863, 55.4425, 55.3952, 55.4841],
            [54.4007, 52.7629, 52.9993, 52.7832, 52.9923, 53.0478],
            [53.0517, 51.8931, 51.6272, 51.7924, 52.0203, 51.6725]],
    }

    FOLD2000_CMP_GREEDY_EXEC_TIME: Dict[AwsInstance, List[float]] = {
        Instances.GTX_TITAN: [
            [66.3909, 69.4175, 69.3275],
            [50.4747, 50.9336, 50.8847],
            [47.8291, 47.8367, 47.8322],
            [47.5439, 47.7914, 47.7774],
            [48.1104, 48.2258, 48.1717],
            [49.4661, 49.4303, 49.4075]
        ],
        Instances.G4DN_X_LARGE: [
            [18.7215, 18.5032, 18.6396],
            [19.487, 20.2772, 19.9734, 19.6493],
            [19.4273, 19.9843, 19.9331, 19.4573],
            [19.3475, 19.7593, 19.7069, 19.2957],
            [19.673, 19.9355, 20.0539, 19.5368],
            [20.0688, 20.4536, 20.5633]
        ],
        Instances.P2_X_LARGE: [
            [91.7002, 89.1627, 89.1909],
            [71.1983, 69.4231, 70.7608, 70.7861, 70.5354],
            [91.8322, 99.1142, 99.6982, 99.6449, 99.7749],
            [91.3636, 98.6359, 99.132, 99.1338, 99.1457],
            [92.5415, 98.753, 99.2523, 99.2745, 99.2679],
            [94.3557, 102.303, 102.204, 102.282]
        ],
        Instances.P3_2X_LARGE: [
            [11.969, 10.9988, 10.9329, 10.963, 11.0149],
            [12.6473, 11.461, 11.4844, 11.4703, 11.5394, 11.5488],
            [12.1007, 11.1253, 11.0555, 10.9614, 11.0654, 11.0359],
            [12.0829, 11.1048, 11.0389, 11.0314, 11.0793, 11.1213],
            [12.1705, 11.1146, 11.0921, 11.1957, 11.2211, 11.2057],
            [12.2674, 11.3637, 11.2761, 11.3012, 11.3632, 11.3408]
        ],
    }

    FOLD2000_ZO_CRS_DE_EXEC_TIME: Dict[AwsInstance, List[List[float]]] = {
        Instances.GTX_TITAN: [
            [1246.84, 1282.33, 1284.78, 1283.1],
            [1137.46, 1155.06, 1157.01, 1157.5],
            [1086.3, 1089.69, 1088.99, 1089.82],
            [1132.63, 1144.68, 1145.89, 1146.24],
            [1222.44, 1241.66, 1242.72, 1242.18],
            [1390.95, 1415.17, 1414.54, 1420.51]
        ],
        Instances.G4DN_X_LARGE: [
            [338.474, 335.158, 337.557, 337.616],
            [346.377, 344.51, 345.615, 342.447],
            [347.229, 345.484, 347.19, 342.328],
            [357.454, 356.019, 357.923, 355.484],
            [361.448, 360.554, 361.896],
            [442.245, 436.933, 439.804]
        ],
        Instances.P2_X_LARGE: [
            [1566.81, 1573.95, 1572.78, 1574.89, 1575.45],
            [1382.43, 1371.68, 1392.77, 1393.75, 1394.84],
            [1397.74, 1388.18, 1417.39, 1420.51, 1418.62],
            [1436.84, 1430.53, 1457.22, 1457.42, 1459.83],
            [1533.14, 1559.7, 1560.55, 1561.32],
            [1645.02, 1676.3, 1677.38, 1677.58]
        ],
        Instances.P3_2X_LARGE: [
            [152.34, 150.91, 150.912, 150.961, 150.755, 150.937],
            [148.618, 146.85, 147.049, 146.769, 147.192, 146.871],
            [154.646, 152.917, 152.666, 152.937, 152.923, 152.943],
            [169.832, 168.281, 168.196, 167.981, 168.449, 167.928],
            [180.849, 178.912, 179.336, 179.152, 180.109, 179.085],
            [259.863, 258.451, 258.359, 258.186, 258.576]
        ],
    }

    @staticmethod
    def plot_thread_benchmark_for_simple_cmp_greedy():
        GraphHelpers.plot_thread_benchmark_with_exec_time(thread_counts=ThreadBenchmark.THREAD_COUNT,
                                                          execution_times=ThreadBenchmark.SIMPLE_SYNTHETIC_CMP_GREEDY_EXEC_TIME,
                                                          data_name='simple_synthetic',
                                                          model='cmp',
                                                          compute_method='greedy',
                                                          platform='cuda')

    @staticmethod
    def plot_thread_benchmark_for_simple_zocrs_de():
        GraphHelpers.plot_thread_benchmark_with_exec_time(thread_counts=ThreadBenchmark.THREAD_COUNT,
                                                          execution_times=ThreadBenchmark.SIMPLE_SYNTHETIC_ZO_CRS_DE_EXEC_TIME,
                                                          data_name='simple_synthetic',
                                                          model='zocrs',
                                                          compute_method='de',
                                                          platform='cuda')

    @staticmethod
    def plot_thread_benchmark_for_fold2000_cmp_greedy():
        GraphHelpers.plot_thread_benchmark_with_exec_time(thread_counts=ThreadBenchmark.THREAD_COUNT,
                                                          execution_times=ThreadBenchmark.FOLD2000_CMP_GREEDY_EXEC_TIME,
                                                          data_name='fold2000',
                                                          model='cmp',
                                                          compute_method='greedy',
                                                          platform='cuda')

    @staticmethod
    def plot_thread_benchmark_for_fold2000_zocrs_de():
        GraphHelpers.plot_thread_benchmark_with_exec_time(thread_counts=ThreadBenchmark.THREAD_COUNT,
                                                          execution_times=ThreadBenchmark.FOLD2000_ZO_CRS_DE_EXEC_TIME,
                                                          data_name='fold2000',
                                                          model='zocrs',
                                                          compute_method='de',
                                                          platform='cuda')

    @staticmethod
    def plot_all():
        ThreadBenchmark.plot_thread_benchmark_for_simple_cmp_greedy()
        ThreadBenchmark.plot_thread_benchmark_for_simple_zocrs_de()
        ThreadBenchmark.plot_thread_benchmark_for_fold2000_cmp_greedy()
        ThreadBenchmark.plot_thread_benchmark_for_fold2000_zocrs_de()
