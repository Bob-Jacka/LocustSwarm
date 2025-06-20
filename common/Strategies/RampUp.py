from common.Strategies.Context import Strategy


class RampUp(Strategy):

    def __init__(self, time_at_least: int = 5, time_max: int = 10, user_count_start: int = 5, user_count_end: int = 100,
                 strat_name: str = 'Peak load'):
        """
        Users: 5 → 100
        Duration: 5 – 10 min
        Goal: check degradation
        """
        super().__init__(time_at_least, time_max, user_count_start, user_count_end, strat_name)

    def do_algorithm(self):
        pass
