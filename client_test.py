import asyncio
import dotenv
import os
from pyracing import client as pyracing
from pyracing import constants
from pyracing.responses.career_stats import CareerStats
from pyracing.responses.yearly_stats import YearlyStats
from pyracing.responses.last_races_stats import LastRaceStats
from pyracing.responses.season import Season
from pyracing.responses.chart_data.chart_data import ChartData
from pyracing.responses.chart_data.irating import IRating
from pyracing.responses.chart_data.ttrating import TTRating
from pyracing.responses.chart_data.license_class import LicenseClass
import unittest

dotenv.load_dotenv()


def async_test(f):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)

    return wrapper


async def get_client():
    return pyracing.Client(os.getenv('IRACING_USERNAME'), os.getenv('IRACING_PASSWORD'))


class ClientTest(unittest.TestCase):
    @async_test
    async def test_career_stats(self):
        client = await get_client()
        await client.authenticate()
        response_list = await client.career_stats(499343)
        for career_stat in response_list:
            self.assertIsInstance(career_stat, CareerStats)

    @async_test
    async def test_yearly_stats(self):
        client = await get_client()
        await client.authenticate()
        response_list = await client.yearly_stats(499343)
        for yearly_stat in response_list:
            self.assertIsInstance(yearly_stat, YearlyStats)

    @async_test
    async def test_last_races_stats(self):
        client = await get_client()
        await client.authenticate()
        response_list = await client.last_race_stats(499343)
        for career_stat in response_list:
            self.assertIsInstance(career_stat, LastRaceStats)

    @async_test
    async def test_current_seasons(self):
        client = await get_client()
        await client.authenticate()
        response_list = await client.current_seasons()
        for season in response_list:
            self.assertIsInstance(season, Season)

    @async_test
    async def test_get_irating(self):
        client = await get_client()
        await client.authenticate()
        response = await client.get_irating(constants.Category.road, 499343)
        self.assertIsInstance(response, ChartData)
        for irating in response.list:
            self.assertIsInstance(irating, IRating)

    @async_test
    async def test_get_ttrating(self):
        client = await get_client()
        await client.authenticate()
        response = await client.get_ttrating(constants.Category.road, 499343)
        self.assertIsInstance(response, ChartData)
        for ttrating in response.list:
            self.assertIsInstance(ttrating, TTRating)

    @async_test
    async def test_get_license_class(self):
        client = await get_client()
        await client.authenticate()
        response = await client.get_license_class(constants.Category.road, 499343)
        self.assertIsInstance(response, ChartData)
        for license_class in response.list:
            self.assertIsInstance(license_class, LicenseClass)


if __name__ == '__main__':
    unittest.main()
