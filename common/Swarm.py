from os import PathLike

from common.Locust import (
    Locust,
    global_logger
)
from common.Strategies import Context


class Swarm:
    """
    ❝ I am the Swarm. Armies will be defeated. Planets will be consumed by fire.
    And eventually, on this planet, I will exact my revenge. I am the Queen of Blades. ❞

    StarCraft 2
    """

    def __init__(self, page_to_destroy: str | PathLike, env, strategy: Context):
        """
        Wrapper class for locust swarm to check web performance
        """
        self.__strategy_context = strategy
        self.locusts: list[Locust] = list()  # Users list
        self.page = page_to_destroy
        self.env = env

    def get_locusts(self):
        """
        Returns locusts list;
        :return: list with Locust entity
        """
        if self.locusts is None and len(self.locusts) != 0:
            return self.locusts
        else:
            global_logger.log('Trying to get locusts, but locusts are None or len is 0')

    def get_locust_count(self) -> int:
        """
        Return locusts count
        :return: int value
        """
        return len(self.locusts)

    def proceed_locusts(self, app_runner, locust_spawn_rate: int):
        """
        Main function for load test of the page
        :param locust_spawn_rate: spawn rate of the locusts
        :param app_runner: app runner
        :return: None
        """
        try:
            global_logger.log(f'Using {self.__strategy_context.strategy.strat_name} strategy from swarm.')
            start_locust_count = self.__strategy_context.strategy.user_count_start
            global_logger.log("App started work")
            user = Locust(self.page, env=self.env)
            self.locusts.append(user)
            global_logger.log('Locust added')
            app_runner.start(start_locust_count, spawn_rate=locust_spawn_rate)
            global_logger.log("App finished work")
        except Exception as e:
            global_logger.log(f'Error occurred in destroy_page - {e}')
            raise RuntimeError()

    def get_page(self):
        """
        Get method for page in swarm
        :return: page for destroy
        """
        if self.page is not None:
            return self.page
        else:
            global_logger.log('Page should not be None to get from swarm')

    def get_env(self):
        """
        Get method for env in swarm
        :return: env
        """
        if self.env is not None:
            return self.env
        else:
            global_logger.log('Env should not be None to get from swarm')
