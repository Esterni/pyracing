import asyncio
import dotenv
import os
from pyracing import client as pyracing
from pyracing import constants
from pyracing.response_objects import career_stats, chart_data, iracing_data, upcoming_events, historical_data
import unittest

dotenv.load_dotenv()
client = pyracing.Client(os.getenv('IRACING_USERNAME'), os.getenv('IRACING_PASSWORD'))


def async_test(f):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)

    return wrapper


class ClientTest(unittest.TestCase):
    @async_test
    async def test_career_stats(self):
        response_list = await client.career_stats(499343)
        for career_stat in response_list:
            self.assertIsInstance(career_stat, career_stats.CareerStats)

    @async_test
    async def test_yearly_stats(self):
        response_list = await client.yearly_stats(499343)
        for yearly_stat in response_list:
            self.assertIsInstance(yearly_stat, career_stats.YearlyStats)

    @async_test
    async def test_last_races_stats(self):
        response_list = await client.last_races_stats(499343)
        for career_stat in response_list:
            self.assertIsInstance(career_stat, career_stats.LastRacesStats)

    @async_test
    async def test_current_seasons(self):
        response_list = await client.current_seasons()
        for season in response_list:
            self.assertIsInstance(season, iracing_data.Season)

    @async_test
    async def test_irating(self):
        response = await client.irating(499343, constants.Category.road.value)
        self.assertIsInstance(response, chart_data.ChartData)
        for irating in response.list:
            self.assertIsInstance(irating, chart_data.IRating)

    @async_test
    async def test_ttrating(self):
        response = await client.ttrating(499343, constants.Category.road.value)
        self.assertIsInstance(response, chart_data.ChartData)
        for ttrating in response.list:
            self.assertIsInstance(ttrating, chart_data.TTRating)

    @async_test
    async def test_license_class(self):
        response = await client.license_class(499343, constants.Category.road.value)
        self.assertIsInstance(response, chart_data.ChartData)
        for license_class in response.list:
            self.assertIsInstance(license_class, chart_data.LicenseClass)

    @async_test
    async def test_active_op_counts(self):
        response = await client.active_op_counts()
        for op_count in response:
            self.assertIsInstance(op_count, upcoming_events.ActiveOPCount)

    @async_test
    async def test_all_subsessions(self):
        response = await client.all_subsessions(33618467)
        for subsession_id in response:
            self.assertIsInstance(subsession_id, int)

    @async_test
    async def test_car_class(self):
        response = await client.car_class()
        self.assertIsInstance(response, iracing_data.CarClass)

    @async_test
    async def test_car_class_with_value(self):
        response = await client.car_class(1)
        self.assertIsInstance(response, iracing_data.CarClass)


if __name__ == '__main__':
    unittest.main()
