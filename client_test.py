import asyncio
import dotenv
import os
from pyracing import client as pyracing
from pyracing import constants
from pyracing.response_objects import career_stats
from pyracing.response_objects import chart_data
from pyracing.response_objects import iracing_data
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
            self.assertIsInstance(career_stat, career_stats.CareerStats)

    @async_test
    async def test_yearly_stats(self):
        client = await get_client()
        await client.authenticate()
        response_list = await client.yearly_stats(499343)
        for yearly_stat in response_list:
            self.assertIsInstance(yearly_stat, career_stats.YearlyStats)

    @async_test
    async def test_last_races_stats(self):
        client = await get_client()
        await client.authenticate()
        response_list = await client.last_races_stats(499343)
        for career_stat in response_list:
            self.assertIsInstance(career_stat, career_stats.LastRacesStats)

    @async_test
    async def test_current_seasons(self):
        client = await get_client()
        await client.authenticate()
        response_list = await client.current_seasons()
        for season in response_list:
            self.assertIsInstance(season, iracing_data.Season)

    @async_test
    async def test_get_irating(self):
        client = await get_client()
        await client.authenticate()
        response = await client.get_irating(constants.Category.road.value, 499343)
        self.assertIsInstance(response, chart_data.ChartData)
        for irating in response.list:
            self.assertIsInstance(irating, chart_data.IRating)

    @async_test
    async def test_get_ttrating(self):
        client = await get_client()
        await client.authenticate()
        response = await client.get_ttrating(constants.Category.road.value, 499343)
        self.assertIsInstance(response, chart_data.ChartData)
        for ttrating in response.list:
            self.assertIsInstance(ttrating, chart_data.TTRating)

    @async_test
    async def test_get_license_class(self):
        client = await get_client()
        await client.authenticate()
        response = await client.get_license_class(constants.Category.road.value, 499343)
        self.assertIsInstance(response, chart_data.ChartData)
        for license_class in response.list:
            self.assertIsInstance(license_class, chart_data.LicenseClass)


if __name__ == '__main__':
    unittest.main()
