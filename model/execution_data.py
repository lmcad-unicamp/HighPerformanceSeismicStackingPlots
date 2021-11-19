from abc import abstractmethod
from statistics import mean, stdev, StatisticsError
from typing import List


class AwsInstance:

    def __init__(self, name: str, cost_per_hour: float = None, gpu_count: int = 1, node_count: int = 1):
        self.__name = name
        self.__cost_per_hour = cost_per_hour
        self.__gpu_count = gpu_count
        self.__node_count = node_count

    @property
    def name(self) -> str:
        return self.__name

    @property
    def cost_per_hour(self) -> float:
        return self.__node_count * self.__cost_per_hour

    @property
    def gpu_count(self) -> int:
        return self.__gpu_count

    @property
    def node_count(self) -> int:
        return self.__node_count


class ExecutionData:

    def __init__(self,
                 test_id: str,
                 int_per_second: list,
                 total_execution_time: list = None,
                 kernel_execution_time: list = None,
                 instance_cost_per_hour: float = None):
        self.__test_id = test_id
        self.__int_per_second = int_per_second
        self.__total_execution_time = total_execution_time
        self.__kernel_execution_time = kernel_execution_time
        self.__instance_cost_per_hour = instance_cost_per_hour

    @property
    def total_execution_time(self) -> List[float]:
        return self.__total_execution_time

    @property
    def kernel_execution_time(self) -> List[float]:
        return self.__kernel_execution_time

    @property
    def avg_int_per_second(self) -> float:
        try:
            return mean(self.__int_per_second)
        except TypeError:
            return 0

    @property
    def std_dev_int_per_second(self) -> float:
        try:
            return stdev(self.__int_per_second)
        except StatisticsError:
            return 0

    @property
    def avg_total_execution_time(self) -> float:
        try:
            return mean(self.__total_execution_time)
        except TypeError:
            return 0

    @property
    def std_dev_total_execution_time(self) -> float:
        try:
            return stdev(self.__total_execution_time)
        except StatisticsError:
            return 0

    @property
    def avg_kernel_execution_time(self) -> float:
        try:
            return mean(self.__kernel_execution_time)
        except TypeError:
            return 0

    @property
    def std_kernel_execution_time(self) -> float:
        try:
            return stdev(self.__kernel_execution_time)
        except (StatisticsError, TypeError):
            return 0

    @property
    def avg_cost(self) -> float:
        try:
            return mean(self.__total_execution_time) * self.__instance_cost_per_hour / 3600.0
        except TypeError:
            return 0

    @property
    def std_dev_cost(self) -> float:
        try:
            __cost_per_hour = self.__instance_cost_per_hour / 3600.0
            return stdev([exec_time * __cost_per_hour for exec_time in self.__total_execution_time])
        except (StatisticsError, TypeError):
            return 0

    def relative_int_per_second(self, other: float) -> float:
        return self.avg_int_per_second / other

    def avg_relative_total_execution_time(self, others: List[float]) -> float:
        return mean(others) / mean(self.__total_execution_time)

    def std_dev_relative_total_execution_time(self, others: List[float]) -> float:
        try:
            return stdev([other / execution_time for (other, execution_time) in zip(others, self.__total_execution_time)])
        except (StatisticsError, TypeError):
            return 0

    def relative_kernel_execution_time(self, other: float) -> float:
        try:
            return other / self.avg_kernel_execution_time
        except ZeroDivisionError:
            return 0


class DummyExecutionData(ExecutionData):

    def __init__(self): pass

    @property
    def total_execution_time(self) -> List[float]:
        return 0

    @property
    def kernel_execution_time(self) -> List[float]:
        return 0

    @property
    def avg_int_per_second(self) -> float:
        return 0

    @property
    def std_dev_int_per_second(self) -> float:
        return 0

    @property
    def avg_total_execution_time(self) -> float:
        return 0

    @property
    def std_dev_total_execution_time(self) -> float:
        return 0

    @property
    def avg_kernel_execution_time(self) -> float:
        return 0

    @property
    def std_kernel_execution_time(self) -> float:
        return 0

    @property
    def avg_cost(self) -> float:
        return 0

    @property
    def std_dev_cost(self) -> float:
        return 0

    def relative_int_per_second(self, other: float) -> float:
        return 0

    def avg_relative_total_execution_time(self, others: List[float]) -> float:
        return 0

    def std_dev_relative_total_execution_time(self, others: List[float]) -> float:
        return 0

    def relative_kernel_execution_time(self, other: float) -> float:
        return 0


class HeuristicData:
    def __init__(self, trace_efficiency: float, interpolations_per_sec: float):
        self.__trace_efficiency = trace_efficiency
        self.__interpolations_per_sec = interpolations_per_sec

    @property
    def interpolations_per_sec(self):
        return self.__interpolations_per_sec

    @property
    def trace_efficiency(self):
        return self.__trace_efficiency


class ExecutionBreakDownData:
    def __init__(self,
                 read_data: float,
                 write_data: float,
                 init_gpus: float,
                 compute_sembl: float,
                 copy_buffer: float):
        self.__read_data__ = read_data
        self.__write_data__ = write_data
        self.__init_gpus__ = init_gpus
        self.__compute_sembl__ = compute_sembl
        self.__copy_buffer__ = copy_buffer

    @property
    def read_data_sec(self) -> float:
        return self.__read_data__

    @property
    def write_data_sec(self) -> float:
        return self.__write_data__

    @property
    def init_gpus_sec(self) -> float:
        return self.__init_gpus__

    @property
    def compute_semblance_sec(self) -> float:
        return self.__compute_sembl__

    @property
    def copy_buffer_sec(self) -> float:
        return self.__copy_buffer__


class Implementation:
    CUDA = 'cuda'
    OPENCL = 'opencl'

    def __init__(self, impl_id: str, tag: str, platform: str):
        self.__impl_id = impl_id
        self.__tag = tag
        self.__platform = platform

    @property
    def impl_id(self) -> str:
        return self.__impl_id

    @property
    def tag(self) -> str:
        return self.__tag

    @property
    def platform(self) -> str:
        return self.__platform


class Implementations:
    CARDOSO_HERCULES = Implementation(impl_id='cardoso', tag='Cardoso, Hércules', platform=Implementation.CUDA)
    GIMENES_ET_AL = Implementation(impl_id='gimenes', tag='Gimenes et al.', platform=Implementation.CUDA)
    SOLUTION_V11 = Implementation(impl_id='v11', tag='v1.1', platform=Implementation.CUDA)
    SOLUTION_V20 = Implementation(impl_id='v20', tag='This work', platform=Implementation.CUDA)
    SOLUTION_V20_OPENCL = Implementation(impl_id='v20_opencl', tag='v2.0_opencl', platform=Implementation.OPENCL)


class Execution:

    @staticmethod
    @abstractmethod
    def compute_method() -> str: pass

    @staticmethod
    @abstractmethod
    def data_name() -> str: pass

    @staticmethod
    @abstractmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData: pass

    @staticmethod
    @abstractmethod
    def model() -> str: pass


class DummyExecution(Execution):

    @staticmethod
    def execution(instance: AwsInstance, impl: Implementation) -> ExecutionData:
        return DummyExecutionData()

    @staticmethod
    def compute_method() -> str:
        return 'dummy'

    @staticmethod
    def data_name() -> str:
        return 'dummy'

    @staticmethod
    def model() -> str:
        return 'dummy'


class Instances:
    GTX_TITAN = AwsInstance(name='GTX Titan')

    G4DN_X_LARGE = AwsInstance(name='g4dn.xlarge', cost_per_hour=0.526, gpu_count=1)
    G4DN_12X_LARGE = AwsInstance(name='g4dn.12xlarge', cost_per_hour=3.912, gpu_count=4)

    G4DN_X_LARGE_2 = AwsInstance(name='g4dn.xlarge', cost_per_hour=0.526, node_count=2)
    G4DN_X_LARGE_4 = AwsInstance(name='g4dn.xlarge', cost_per_hour=0.526, node_count=4)
    G4DN_X_LARGE_8 = AwsInstance(name='g4dn.xlarge', cost_per_hour=0.526, node_count=8)
    G4DN_X_LARGE_16 = AwsInstance(name='g4dn.xlarge', cost_per_hour=0.526, node_count=16)
    G4DN_X_LARGE_32 = AwsInstance(name='g4dn.xlarge', cost_per_hour=0.526, node_count=32)
    G4DN_X_LARGE_64 = AwsInstance(name='g4dn.xlarge', cost_per_hour=0.526, node_count=64)

    P2_X_LARGE = AwsInstance(name='p2.xlarge', cost_per_hour=0.9, gpu_count=1)
    P2_8X_LARGE = AwsInstance(name='p2.8xlarge', cost_per_hour=7.2, gpu_count=8)
    P2_16X_LARGE = AwsInstance(name='p2.16xlarge', cost_per_hour=14.4, gpu_count=16)

    P2_X_LARGE_2 = AwsInstance(name='p2.xlarge', cost_per_hour=0.9, node_count=2)
    P2_X_LARGE_4 = AwsInstance(name='p2.xlarge', cost_per_hour=0.9, node_count=4)
    P2_X_LARGE_8 = AwsInstance(name='p2.xlarge', cost_per_hour=0.9, node_count=8)
    P2_X_LARGE_16 = AwsInstance(name='p2.xlarge', cost_per_hour=0.9, node_count=16)
    P2_X_LARGE_32 = AwsInstance(name='p2.xlarge', cost_per_hour=0.9, node_count=32)
    P2_X_LARGE_64 = AwsInstance(name='p2.xlarge', cost_per_hour=0.9, node_count=64)

    P3_2X_LARGE = AwsInstance(name='p3.2xlarge', cost_per_hour=3.06, gpu_count=1)
    P3_8X_LARGE = AwsInstance(name='p3.8xlarge', cost_per_hour=12.24, gpu_count=4)
