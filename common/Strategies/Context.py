from abc import (
    ABC,
    abstractmethod
)
from enum import Enum


class StrategyEnum(Enum):
    """
    Allowed strategies of the app
    """

    PEAK = 'peak',  # peak load
    RAMP_UP = 'ramp-up'  # smooth increase
    SUSTAIN_LOAD = 'sustain-load'  # hold
    SPIKE_TEST = 'spike-test'  # impulse


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions of some algorithm.
    A context uses this interface to invoke the algorithm defined by the Concrete Strategies.
    """

    def __init__(self, time_at_least: int = 0, time_max: int = 0, user_count_start: int = 0, user_count_end: int = 0, strat_name: str = ""):
        self.time_at_least = time_at_least
        self.time_max = time_max
        self.user_count_start = user_count_start
        self.user_count_end = user_count_end
        self.strat_name = strat_name

    @abstractmethod
    def do_algorithm(self):
        """
        Do some chosen 'Locust' algorithm
        :return:
        """
        self.time_at_least = 0
        self.time_max = 0
        self.user_count_start = 0
        self.user_count_end = 0


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

    def do_strategy(self) -> None:
        """
        Instead of implementing multiple versions of an algorithm itself, the Context delegates some work to a Strategy object.
        """
        result = self._strategy.do_algorithm()
