from LocustSwarm.Strategies.Context import Strategy


class RampUp(Strategy):

    def __init__(self, __time_at_least: int = 5, __time_max: int = 10, __user_count_start: int = 5, __user_count_end: int = 100,
                 __strat_name: str = 'Peak load'):
        """
        Users: 5 → 100
        Duration: 5 – 10 min
        Goal: check degradation
        """
        self.____time_at_least = __time_at_least
        self.__time_max = __time_max
        self.__user_count_start = __user_count_start
        self.__user_count_end = __user_count_end
        self.__strat_name = __strat_name
        super().__init__(__time_at_least, __time_max, __user_count_start, __user_count_end, __strat_name)

    def get_time_at_least(self):
        return self.__time_at_least

    def get_time_max(self):
        return self.__time_max

    def get_user_count_start(self):
        return self.__user_count_start

    def get_user_count_end(self):
        return self.__user_count_end

    def get_strat_name(self):
        return self.__strat_name
