import asyncio
import dotenv
import os
from pyracing import client as pyracing
from pyracing import constants
from pyracing.response_objects import career_stats, chart_data, iracing_data, \
    upcoming_events, historical_data, session_data
import unittest

dotenv.load_dotenv()
client = pyracing.Client(
    os.getenv('IRACING_USERNAME'),
    os.getenv('IRACING_PASSWORD')
    )


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
        response = await client.license_class(
            499343,
            constants.Category.road.value
            )
        self.assertIsInstance(response, chart_data.ChartData)
        for license_class in response.list:
            self.assertIsInstance(license_class, chart_data.LicenseClass)

    @async_test
    async def test_active_op_counts(self):
        response = await client.active_op_counts()
        for op_count in response:
            self.assertIsInstance(op_count, upcoming_events.OpenPractice)

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

    @async_test
    async def test_last_series(self):
        response = await client.last_series(499343)
        for last_series in response:
            self.assertIsInstance(last_series, career_stats.LastSeries)

    @async_test
    async def test_member_cars_driven(self):
        response = await client.member_cars_driven(499343)
        for car_id in response:
            self.assertIsInstance(car_id, int)

    @async_test
    async def test_member_subsession_id_from_session(self):
        response = await client.member_subsession_id_from_session(
            499343,
            134975301
            )
        self.assertIsInstance(response, int)

    @async_test
    async def test_driver_status(self):
        response = await client.driver_status(499343)
        self.assertIsInstance(response, iracing_data.DriverStatus)

    @async_test
    async def test_next_event(self):
        response = await client.next_event(228)
        self.assertIsInstance(response, upcoming_events.NextEvent)

    @async_test
    async def test_next_session_times(self):
        response = await client.next_session_times(2826)
        for session_time in response:
            self.assertIsInstance(
                session_time,
                upcoming_events.NextSessionTimes
                )

    @async_test
    async def test_personal_bests(self):
        response = await client.personal_bests(499343, 4)
        for personal_best in response:
            self.assertIsInstance(personal_best, career_stats.PersonalBests)

    @async_test
    async def test_private_results(self):
        response = await client.private_results(499343, 0, 1595792756654)
        for result in response:
            self.assertIsInstance(result, historical_data.PrivateResults)

    @async_test
    async def test_race_guide(self):
        response = await client.race_guide()
        for race_guide in response:
            self.assertIsInstance(race_guide, upcoming_events.RaceGuide)

    @async_test
    async def test_race_laps_all(self):
        response = await client.race_laps_all(33618467)
        self.assertIsInstance(response, session_data.RaceLapsAll)

    @async_test
    async def test_race_laps_driver(self):
        response = await client.race_laps_driver(499343, 33618467)
        self.assertIsInstance(response, session_data.RaceLapsDriver)

    @async_test
    async def test_season_from_session(self):
        response = await client.season_from_session(134975301)
        self.assertIsInstance(response, int)

    @async_test
    async def test_season_standings(self):
        response = await client.season_standings(2826)
        for standings in response:
            self.assertIsInstance(standings, historical_data.SeasonStandings)

    @async_test
    async def test_series_race_results(self):
        response = await client.series_race_results(2826)
        for standings in response:
            self.assertIsInstance(standings, historical_data.SeriesRaceResults)

    @async_test
    async def test_subsession_data(self):
        response = await client.subsession_data(33618467)
        self.assertIsInstance(response, session_data.SubSessionData)

    @async_test
    async def test_total_registered_all(self):
        response = await client.total_registered_all()
        for session in response:
            self.assertIsInstance(session, upcoming_events.TotalRegistered)

    @async_test
    async def test_world_records(self):
        response = await client.world_records(2019, 1, 1, 1)
        for record in response:
            self.assertIsInstance(record, historical_data.WorldRecords)

    @async_test
    async def test_event_results(self):
        response = await client.event_results(499343, 3)
        for result in response:
            self.assertIsInstance(result, historical_data.EventResults)


if __name__ == '__main__':
    unittest.main()
