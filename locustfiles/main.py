from common.App import (
    App
)
from common.Strategies.Context import StrategyEnum

page = 'https://deploy.blacked.team/slots/lost_town_new_visual/'

if __name__ == "__main__":
    app = App(StrategyEnum.PEAK)
    app.set_off_swarm_to_page(page)

    app.get_swarm().proceed_locusts(
        app_runner=app.get_runner(),
        locust_start_count=10,
        locust_spawn_rate=5,
    )
