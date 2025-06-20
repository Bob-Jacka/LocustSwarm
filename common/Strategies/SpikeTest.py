from common.Strategies.Context import Strategy


class SpikeTest(Strategy):

    def __init__(self, time_at_least: int = 0.05, time_max: int = 0.05, user_count_start: int = 100, user_count_end: int = 100,
                 strat_name: str = 'Peak load'):
        """
        Users: 100
        Duration: 5 sec
        Goal: reaction to a sharp jump
        """
        super().__init__(time_at_least, time_max, user_count_start, user_count_end, strat_name)

    def do_algorithm(self):
        pass
