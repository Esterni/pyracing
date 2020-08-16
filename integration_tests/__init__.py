import asyncio
import logging
import os
import sys
import unittest

from pyracing.client import Client


__all__ = [
    "IRacingIntegrationTest",
    "async_test",
]

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    datefmt="%Y-%m-%dT%H:%M:%S%Z",
    format="%(asctime)s [%(levelname)s] -- %(message)s"
)


def get_required_env(key: str) -> str:
    """
    Get an environment variable's value, raising an exception if it isn't set.
    """
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(
            f"Must set {key} environment variable to to run integration tests."
        )
    return value


IRACING_USERNAME = get_required_env("IRACING_USERNAME")
IRACING_PASSWORD = get_required_env("IRACING_PASSWORD")

# We create a singleton client that we use for all tests to avoid constantly
# re-authenticating. iRacing may see constant re-authentication as suspicious
# activity, we see the disadvantages of 1) using a singleton and 2) sharing
# state between tests are outweighed by being good citizens to the iRacing
# platform.
client = Client(
    username=IRACING_USERNAME,
    password=IRACING_PASSWORD,
)


def async_test(f):
    """
    Function that can be used as a decorator for tests of async functions.

    For example,

        class MyTest(unittests.TestCase):
            @async_test
            async def test_example(self):
                self.assertTrue(True)

    :param f: the function to wrap
    :return: the wrapped function

    >>> class MyTest(unittest.TestCase):
    ...     @async_test
    ...     async def test_example(self):
    ...         self.assertTrue(True)
    """
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)

    return wrapper


class IRacingIntegrationTest(unittest.TestCase):
    """
    Test service that runs against iRacing's server.
    """

    def setUp(self) -> None:
        self.client = Client(
            username=IRACING_USERNAME,
            password=IRACING_PASSWORD,
        )
