from common.Strategies.Context import Strategy


class SustainLoad(Strategy):

    def __init__(self, time_at_least: int = 5, time_max: int = 10, user_count_start: int = 100, user_count_end: int = 200,
                 strat_name: str = 'Peak load'):
        """
        Users: 50 - 100
        Duration: 20 - 30 min
        Goal: identifying cumulative problems
        """
        super().__init__(time_at_least, time_max, user_count_start, user_count_end, strat_name)

    def do_algorithm(self):
        pass
