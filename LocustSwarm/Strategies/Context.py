from abc import (
    ABC,
    abstractmethod
)
from enum import Enum

from LocustSwarm.Exceptions.StrategyExceptions import StrategyExceptions


class StrategyEnum(Enum):
    """
    Allowed strategies of the app to use
    """

    PEAK = 'peak',  # peak load
    RAMP_UP = 'ramp-up'  # smooth increase
    SUSTAIN_LOAD = 'sustain-load'  # hold
    SPIKE_TEST = 'spike-test'  # impulse


class Strategy(ABC):
    """
    The Strategy interface declares operations LocustSwarm to all supported versions of some algorithm.
    A context uses this interface to invoke the algorithm defined by the Concrete Strategies.
    """

    def __init__(self,
                 __time_at_least: int = 0,
                 __time_max: int = 0,
                 __user_count_start: int = 0,
                 __user_count_end: int = 0,
                 __strat_name: str = ""):
        self.__time_at_least = __time_at_least
        self.__time_max = __time_max
        self.__user_count_start = __user_count_start
        self.__user_count_end = __user_count_end
        self.__strat_name = __strat_name

    @abstractmethod
    def get_time_at_least(self):
        try:
            return self.__time_at_least
        except Exception as e:
            raise StrategyExceptions(f'Error returning time at least from strategy - {e}.')

    @abstractmethod
    def get_time_max(self):
        try:
            return self.__time_max
        except Exception as e:
            raise StrategyExceptions(f'Error returning time max from strategy - {e}.')

    @abstractmethod
    def get_user_count_start(self):
        try:
            return self.__user_count_start
        except Exception as e:
            raise StrategyExceptions(f'Error returning user count start variable from strategy - {e}.')

    @abstractmethod
    def get_user_count_end(self):
        try:
            return self.__user_count_end
        except Exception as e:
            raise StrategyExceptions(f'Error returning user count end variable from strategy - {e}.')

    @abstractmethod
    def get_strat_name(self):
        try:
            return self.__strat_name
        except Exception as e:
            raise StrategyExceptions(f'Error returning strategy name variable from strategy - {e}.')


class Context:
    """
    The context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Typically, a Context accepts a strategy through a constructor, and also provides a setter to change it at runtime.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The context stores a reference to one of the Strategy objects.
        The context does not know the specific strategy class.
        It must work with all strategies through the Strategy interface.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Typically, the Context allows the Strategy object to be replaced at runtime.
        """
        self._strategy = strategy

    @strategy.getter
    def strategy(self):
        return self._strategy
