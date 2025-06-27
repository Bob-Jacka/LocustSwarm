import unittest

from common.App import App
from common.Strategies.Context import StrategyEnum


class NegativeTests(unittest.TestCase):
    """
    Class for Negative tests
    """

    def test_should_not_create_app_entity(self):
        app = App()
        self.assertEqual(app, None)

    def test_should_not_return_runner(self):
        app = App()
        runner = app.get_runner()
        self.assertEqual(runner, None)

    def test_should_not_return_swarm(self):
        app = App(StrategyEnum.SPIKE_TEST)
        swarm = app.get_swarm()
        self.assertEqual(swarm, None)
        self.assertNotEqual(app, None)

    def test_should_not_proceed_locusts(self):
        app = App(StrategyEnum.SPIKE_TEST)
        self.assertRaises(
            Exception,
            app.get_swarm().proceed_locusts()
        )
        self.assertEqual(app, None)

    def test_should_throw_AppException(self):
        pass

    def test_should_throw_LocustException(self):
        pass

    def test_should_throw_StrategyExceptions(self):
        pass

    def test_should_throw_SwarmExceptions(self):
        pass
