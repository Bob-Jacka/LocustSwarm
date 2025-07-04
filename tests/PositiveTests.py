import unittest

import common.App
from common.App import App
from common.BotLogger import BotLogger
from common.Strategies.Context import StrategyEnum


class PositiveTests(unittest.TestCase):
    """
    Class for Positive tests of the app
    """

    def test_should_create_app_entity_peak(self):
        app = App(StrategyEnum.PEAK)
        self.assertNotEqual(app, None)

    def test_should_return_runner_with_peak(self):
        app = App(StrategyEnum.PEAK)
        runner = app.get_runner()
        self.assertNotEqual(runner, None)
        self.assertNotEqual(app, None)

    def test_should_create_app_entity_ramp_up(self):
        app = App(StrategyEnum.RAMP_UP)
        self.assertNotEqual(app, None)

    def test_should_return_runner_with_ramp(self):
        app = App(StrategyEnum.RAMP_UP)
        runner = app.get_runner()
        self.assertNotEqual(runner, None)
        self.assertNotEqual(app, None)

    def test_should_create_app_entity_spike(self):
        app = App(StrategyEnum.SPIKE_TEST)
        self.assertNotEqual(app, None)

    def test_should_return_runner_with_spike(self):
        app = App(StrategyEnum.SPIKE_TEST)
        runner = app.get_runner()
        self.assertNotEqual(runner, None)
        self.assertNotEqual(app, None)

    def test_should_create_app_entity_sustain(self):
        app = App(StrategyEnum.SUSTAIN_LOAD)
        self.assertNotEqual(app, None)

    def test_should_return_runner_with_sustain(self):
        app = App(StrategyEnum.SUSTAIN_LOAD)
        runner = app.get_runner()
        self.assertNotEqual(runner, None)
        self.assertNotEqual(app, None)

    def test_should_open_web_ui(self):
        app = App(StrategyEnum.SUSTAIN_LOAD)
        with self.assertRaises(
                Exception,
                app.open_web_ui()
        ) as ex:
            exception = ex.exception
        self.assertEqual(exception, None)
        self.assertNotEqual(app, None)

    def test_should_create_swarm_thought_app_method_without_logger(self):
        test_page = 'https://yandex.ru/'
        app = App(StrategyEnum.PEAK)
        app.set_off_swarm_to_page(test_page, None)
        swarm = app.get_swarm()
        self.assertNotEqual(swarm, None)

    def test_should_create_swarm_thought_app_method_with_logger(self):
        test_page = 'https://yandex.ru/'
        app = App(StrategyEnum.PEAK)
        app.set_off_swarm_to_page(test_page, BotLogger('test_logger'))
        swarm = app.get_swarm()
        self.assertNotEqual(swarm, None)

    def test_should_proceed_locusts(self):
        test_page = 'https://yandex.ru/'
        app = App(StrategyEnum.PEAK)
        app.set_off_swarm_to_page(test_page, BotLogger('test_logger'))
        swarm = app.get_swarm()
        app.get_swarm().proceed_locusts(
            app_runner=app.get_runner(),
            locust_spawn_rate=5,
        )
        self.assertNotEqual(swarm, None)

    def test_should_proceed_locusts_without_app_loggers(self):
        test_page = 'https://yandex.ru/'
        app = App(StrategyEnum.PEAK)
        app.set_off_swarm_to_page(test_page, None)
        swarm = app.get_swarm()
        app.get_swarm().proceed_locusts(
            app_runner=app.get_runner(),
            locust_spawn_rate=5,
        )
        self.assertEqual(app.get_logger(), None)
        self.assertNotEqual(swarm, None)

    def test_should_proceed_locusts_with_logger(self):
        test_page = 'https://yandex.ru/'
        app = App(StrategyEnum.PEAK)
        app.set_off_swarm_to_page(test_page, None)
        swarm = app.get_swarm()
        app.get_swarm().proceed_locusts(
            app_runner=app.get_runner(),
            locust_spawn_rate=5,
            logger=BotLogger('Local proceed locusts logger')
        )
        self.assertNotEqual(app.get_logger(), None)
        self.assertNotEqual(swarm, None)

    def test_should_output_help(self):
        self.assertRaises(Exception, common.App.get_help())
