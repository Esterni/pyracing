# Which function for X data?

!!! Note "Background"
Every page on the iRacing Membersite receives its data, to be nicely displayed, from various URL endpoints in the form of `/GetSomeData` that is *usually* in JSON format.

The functions below interact with 1 endpoint each and use the provided arguments as the parameters in the URL query string that we've found it accepts. It is then mapped into a class object for ease of use. (More details here)

While some of these endpoints reveal data that can't be found anywhere else, others will return such little information that you might wonder why they exist at all. **Our primary goal is to provide accessibility to the data, not make sense of it..**

!!! Warning Error
    We do not currently offer error handling in the event of an invalid *input*. Data returned from iRacing is mapped into objects based on the specific dictionary key values that they give us. When a reponse is an empty dictionary (due to an invalid input to iRacing) you will recieve an error. We plan to modify this to return a None object with a warning instead so that the program won't crash.  

## Driver Data
Data returned from these methods require a driver (cust_id) to be included in the query parameters. A good example is `event_results()`. It can return all kinds of different race results, but only results that are related to a driver in question. For all results of a series, go to [series_race_results()](#series_race_results)

### career_stats()
Returns a driver’s career stats as seen on iRacing's [Career Profile](https://members.iracing.com/membersite/member/CareerStats.do).

| Args/Kwargs | Description                            |
| :---------- | :------------------------------------- |
| cust_id     | Which driver’s Career Stats to return. |


### driver_stats()
Returns a list of drivers that match the given parameters. This is the backend source for iRacing's [Driver Stats Page](https://members.iracing.com/membersite/member/DriverLookup.do).

This method provides functionality that the iRacing page does not. It search drivers by name. It is arguably the easiest method to obtain driver information.

| Args/Kwargs                                            | Description                                                                                                                                                    |
| :----------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| search=`'null'`                                        | Useful for looking up a specific driver. (e.g. `'John Smitherson5'`) <br> Also accepts partial names to return all matching drivers.                           |
| country=`'null'`                                       | Return only drivers from a given country. Accepted values can be found in the `CountryCode` enum from the `constants` module for convienence.                  |
| category=Category.road.value                           | Selects the race discipline.<br>(The `Category` enum is from the `constants` module) <br>                                                                      |
| class_low=None<br>class_high=None                      | Filters results by the driver's License Class.                                                                                                                 |
| irating_low=None<br>irating_high=None                  | Filters results by the driver's iRating.                                                                                                                       |
| ttrating_low=None<br>ttrating_high=None                | Filters results by the driver's ttRating.                                                                                                                      |
| starts_avg_low=None<br>starts_avg_high=None            | Filters results by the driver's average starting position.                                                                                                     |
| finish_avg_low=None<br>finish_avg_high=None            | Filters results by the driver's average finish position.                                                                                                       |
| points_avg_low=None<br>points_avg_high=None            | Filters results by the driver's average champ points awarded.                                                                                                  |
| inc_avg_low=None<br>inc_avg_high=None                  | Filters results by the driver's average incidents per race.                                                                                                    |
| num_results_low=1<br>num_results_high=25               | The first result of the query to return and the last result of the query to return.                                                                            |
| sort=Sort.irating.value<br>order=Sort.descending.value | How to sort and order the data. The default is to sort the data with the most recent race as the first result. The `Sort` enum is from the `constants` module. |
| active=1                                               | *Should* let you see non-active drivers with `0`, but appears that iRacing does not allow it.                                                                  |
| friend=None<br>watched=None<br>recent=None             | Accepts a `cust_id` to filter results to friend, watched, or recent.<br> **!Note: Only works for the currently logged in members `cust_id`.**                  |
| cust_id=None                                           | Does not affect returned data                                                                                                                                  |

### driver_status()
Returns friends list for the person logged in. (gold star for least useful)

| Args/Kwargs   | Description                                                                                                                                                                              |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cust_id=None  | Returns the status info of the provided cust_id. If logged in while also providing **your** custid, it will also return the status info of your friends and studied/blacklisted drivers. |
| friends=1     | Toggles display of friends in results.                                                                                                                                                   |
| studied=1     | Toggles display of studied drivers in results.                                                                                                                                           |
| blacklisted=1 | Toggles display of blacklisted drivers in results.                                                                                                                                       |

### event_results()
Returns a list of results that the driver has participated in. This is the backend data for iRacing's [My Series Results](https://members.iracing.com/membersite/member/results.jsp). Contains the summary information about the results of the event. For detailed information about a specific session, see: [subsession_data()](#subsession_data).

| Args/Kwargs                                                                                                         | Description                                                                                                                                                                                                                 |
| :------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cust_id                                                                                                             | Which driver's events to return.                                                                                                                                                                                            |
| quarter                                                                                                             | Which quarter/season of the year to return data from.                                                                                                                                                                       |
| show_races=1<br>show_quals=None<br>show_tts=None<br>show_ops=None                                                   | A value of 1 includes the session type in the return.<br>A value of None excludes the session type from the results.                                                                                                        |
| show_official=1<br>show_unofficial=None                                                                             | Toggles official/non-official sessions  with values of `1` or `None`.                                                                                                                                                       |
| show_rookie=1<br>show_class_d=1<br>show_class_c=1<br>show_class_b=1<br>show_class_a=1<br>show_pro=1<br>show_prowc=1 | Filters results by the license class that a series requires. Setting only `show_class_a` to 1 for the road category will only display results from the iGPS series, as that is the only series with an A class requirement. |
| result_num_low=1<br>result_num_high=25                                                                              | First result of the data to return.<br> Last result of the data to return.                                                                                                                                                  |
| sort=Sort.start_time.value<br>order=Sort.descending.value                                                           | How to sort and order the data. The default is to sort the data with the most recent race as the first result. The `Sort` enum is from the `constants` module.                                                              |
| data_format='json'                                                                                                  | Other values are currently unknown.                                                                                                                                                                                         |
| category=Category.road.value                                                                                        | Which category of race discipline to return. The `Category` enum is from the `constants` module.                                                                                                                            |
| year=datetime.today().year                                                                                          | Which year to query. The default sets to the current years data.                                                                                                                                                            |
| race_week=None                                                                                                      | Which raceweek of the quarter/season to query.                                                                                                                                                                              |
| track_id=None<br>car_class=None<br>car_id=None                                                                      | Allows to filter results to a specific track, car class, car, or a combination of all three.                                                                                                                                |
| start_low=None<br>start_high=None                                                                                   | Filters results by the driver's starting position.                                                                                                                                                                          |
| finish_low=None<br>finish_high=None                                                                                 | Filters results by the driver's finish position.                                                                                                                                                                            |
| incidents_low=None<br>incidents_high=None                                                                           | Filters results by the driver's number of incidents.                                                                                                                                                                        |
| points_champ_low=None<br>points_champ_high=None                                                                     | Filters results by driver's champ points awarded.                                                                                                                                                                           |

### irating()
Utilizes the `stats_chart()` method to return a list of iRating values. Used in the membersite's [Career Profile](https://members.iracing.com/membersite/member/CareerStats.do) charts.
Accessing irating.current() will give the most recent irating of a user.

| Args/Kwargs | Description                                                                                |
| :---------- | :----------------------------------------------------------------------------------------- |
| cust_id     | Which driver’s irating to return.                                                          |
| category    | Selects the race discipline. The `Category` enum from `constants` module can be used here. |


### last_races_stats()
Returns a stat summary for the driver's last 10 races; used in the membersite's [Career Profile](https://members.iracing.com/membersite/member/CareerStats.do) "Last 10 Races" table.

| Args/Kwargs | Description                     |
| :---------- | :------------------------------ |
| cust_id     | Which driver’s races to return. |


### last_series()
Returns a summary of stats about a driver's last 3 series; Used in the membersite's [Career Profile](https://members.iracing.com/membersite/member/CareerStats.do) "Last 3 Series" table.

| Args/Kwargs | Description                      |
| :---------- | :------------------------------- |
| cust_id     | Which driver’s series to return. |

### license_class()
Utilizes the `stats_chart()` method to return a list of license values; Used in the membersite's [Career Profile](https://members.iracing.com/membersite/member/CareerStats.do) charts.
See the LicenseClass class for how to further use this data. (Link to page coming soon...)

| Args/Kwargs | Description                                                                                |
| :---------- | :----------------------------------------------------------------------------------------- |
| cust_id     | Which driver’s stats to return.                                                            |
| category    | Selects the race discipline. The `Category` enum from `constants` module can be used here. |

### member_cars_driven()
Returns which cars (list of `car_id`s) the member has driven.

| Args/Kwargs | Description                                    |
| :---------- | :--------------------------------------------- |
| cust_id     | Which member to search for their car's driven. |


### member_division()
Returns which division the driver was in for the specified season_id. ("was" because a season_id can be a season that has concluded)

| Args/Kwargs | Description                                      |
| :---------- | :----------------------------------------------- |
| cust_id     | Which member's division to return.               |
| season_id   | Which season to check for the driver's division. |


### member_subsession_id_from_session()
Returns which subsession_id that a member was in from a given session_id. This might be useful when you you know the session_id before the race session were split into subsessions, but otherwise subsession is usually included for the driver in other queries.

| Args/Kwargs | Description                                           |
| :---------- | :---------------------------------------------------- |
| cust_id     | Which member's `subsession_id` to return.             |
| session_id  | Which session to look in for the driver's subsession. |


### personal_bests()
Returns the drivers best laptimes for the given car, as seen on the /CareerStats page.

| Args/Kwargs | Description                                    |
| :---------- | :--------------------------------------------- |
| cust_id     | Which driver’s laptimes to return.             |
| car_id      | Which car's laptimes to return for the driver. |


### race_laps_driver()
Returns data for all laps completed of a single driver. sim_sess_id specifies the laps from practice, qual, or race.

| Args/Kwargs                                    | Description                                                                                                                                    |
| :--------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| cust_id                                        | Which driver’s lap data to return.                                                                                                             |
| subsession_id                                  | Which subsession's data to return.                                                                                                             |
| sim_session_type=<br>SimSessionType.race.value | Which segment of a race session to return results for. (Practice, Qualify, Race)<br> The `SimSessionType` enum is from the `constants` module. |


### stats_chart()
Returns a list in the form of `time:value` for the race category specified.

| Args/Kwargs | Description                                                                                                                            |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| cust_id     | Which driver’s chart to return.                                                                                                        |
| category    | Which race category to return. The `Category` enum from the `constants` module provides available values.                              |
| chart_type  | Type of chart to return. (iRating, ttRating, and License Class) The `ChartType` enum from the `constants` module provides easy access. |


### ttrating()
Utilizes the stats_chart class to return a list of ttrating values that are used in the /CareerStats charts.

| Args/Kwargs | Description                                                                                |
| :---------- | :----------------------------------------------------------------------------------------- |
| cust_id     | Which driver’s ttrating to return.                                                         |
| category    | Selects the race discipline. The `Category` enum from `constants` module can be used here. |


### yearly_stats()
Returns the breakdown of career stats by year, as seen on the driver profile page.

| Args/Kwargs | Description                            |
| :---------- | :------------------------------------- |
| cust_id     | Which driver’s Yearly Stats to return. |

## Series Data
Data returned from these methods return information about a series.

!!! note
    On the topic of `series_id` and `season_id`:

    `series_id` refers to the specific configuration for a series that does not change. e.g. The "Advanced Mazda MX-5 Cup Series" has a series id of 231. It refers to the car, license, caution types, incident limits, and grid size.

    `season_id` refers to time period that a series will be active with a given track configuration. It is used to hold all the stats and races for a specific series during a season. The series referenced above had a season id of 2846 for the year 2020 quarter 3.


### active_op_counts()
Returns a list of 'Open Practice' sessions that are currently active. By default only sessions with registered drivers are included. Use include_empty flag to see all sessions.

| Args/Kwargs       | Description                                       |
| :---------------- | :------------------------------------------------ |
| count_max=250     | Sets the max number of results to return.         |
| include_empty='n' | Set to `'y'` if empty results should be included. |
| cust_id=None      | Unknown purpose.                                  |


### next_event()
Returns the next event for a series, from the requested time.

| Args/Kwargs                     | Description                                                                                                                               |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------- |
| series_id                       | Which series to return the next event for.                                                                                                |
| event_type=EventType.race.value | Which event_type (Race, Practice) to return results for. The `EventType` enum is from the `constants` module.                             |
| date=now_five_min_floor()       | Default is to use the same time format that iRacing's Race Guide uses, which is the current time rounded down the previous 5 minute mark. |


### next_session_times()
Returns the next 5 sessions with all of their attributes: start time, registered drivers, session parameters, etc.

| Args/Kwargs | Description                              |
| :---------- | :--------------------------------------- |
| season_id   | Which season to return the sessions for. |


### season_standings()
Returns the championship point standings of a series. This is the same data found in /statsseries.jsp.

| Args/Kwargs                                                 | Description                                                                                                                                                        |
| :---------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| season_id                                                   | Which season's champ points to return.                                                                                                                             |
| race_week=None                                              | Which race_week of the season to return.                                                                                                                           |
| car_class_id=None                                           | Filters point standings to a specific car class.                                                                                                                   |
| club_id=None                                                | Filters point standings to a specific club.                                                                                                                        |
| division=None                                               | Filters point standings to a specific division.                                                                                                                    |
| result_num_low=1<br>result_num_high=25                      | The first result of the query to return and the last result of the query to return.                                                                                |
| sort=Sort.champ_points.value<br>order=Sort.descending.value | How to sort and order the data. The default is to sort the data with the most recent race as the first result. <br>The `Sort` enum is from the `constants` module. |

### series_race_results()
Returns summary info for the specified season_id and race_week. Results are restricted to a single week per query.

| Args/Kwargs | Description                                                                                              |
| :---------- | :------------------------------------------------------------------------------------------------------- |
| season_id   | Which season's results to return.                                                                        |
| race_week=1 | Which week of the season to return. iRacing restricts this endpoint to querying a single week at a time. |


### team_standings()
(**Not finished**) Returns championship point standings of Teams.

| Args/Kwargs    | Description                                                      |
| :------------- | :--------------------------------------------------------------- |
| season_id      | Which season's standings to return.                              |
| car_class_id   | Which car class to return data for. (Required to select 1 class) |
| car_id=None    | Filters results to a specific car.                               |
| race_week=None | Filters results to a specific race week.                         |

## Session Data

### all_subsessions()
Returns subsession IDs for any additional race splits to the one provided.

| Args/Kwargs   | Description                                                    |
| :------------ | :------------------------------------------------------------- |
| subsession_id | Which subsession to return the related `subsession_id`(s) for. |

### private_results()
Returns private sessions that the driver has participated in.

| Args/Kwargs                                                | Description                                                                                                                                          |
| :--------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| cust_id                                                    | Which driver’s hosted sessions to return.                                                                                                            |
| time_start_lower<br>time_start_upper                       | Filters results to between these times.<br>**Note**: Both fields are required for this endpoint to return data.                                      |
| lower_bound=1<br>upper_bound=25                            | The first result of the query to return and the last result of the query to return.                                                                  |
| sort=Sort.session_name.value<br>order=Sort.ascending.value | How to sort and order the data. The default is to sort the data alphabetically by `session_name`.<br>The `Sort` enum is from the `constants` module. |

### race_guide()
Returns all data used by the race guide page for the active seasons. Filters are identical to those found when visiting the race guide with a browser.


| Args/Kwargs                                                                                                       | Description                                                                                                                                                |
| :---------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rookie=None<br>class_d=None<br>class_c=None<br>class_b=None<br>class_a=None<br>class_pro=None<br>class_prowc=None | **Filters for license classes.** <br>Setting to `0` will filter results to exclude series requiring that license.<br>Any combination is allowed.           |
| oval=None<br>road=None<br>dirt_oval=None<br>dirt_road=None                                                        | **Filters for race categories.**<br> Setting to `0` will filter results to exclude the category from being returned.<br>Any combination is allowed.        |
| fixed_setup=None                                                                                                  | Set to `1` to display only fixed setup sessions. (None displays both. There is not an option to display only open setups)                                  |
| multiclass=None                                                                                                   | Set to `1` to display only multiclass sessions                                                                                                             |
| meets_mpr=None                                                                                                    | Set to `1` to display races that meet your MPR. (Restricted to loggedin member)                                                                            |
| populated=None                                                                                                    | Set to `1` to display only populated sessions.                                                                                                             |
| eligible=None                                                                                                     | Set to `1` to dispaly only the series you are eligible for. (Restricted to logged in member)                                                               |
| official=None                                                                                                     | Set to `1` to return only official race sessions.                                                                                                          |
| time=now_five_min_floor()                                                                                         | The Race Guide uses the current time (in unix milliseconds) rounded down the previous 5 minute mark as the default value. A time in the future is allowed. |


### race_laps_all()
Returns information about all laps of a race for *every* driver. The class of car can be set for multiclass races. To specify laps of a single driver, use race_laps_driver().

| Args/Kwargs                                    | Description                                                                                                                                    |
| :--------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| subsession_id                                  | Which subsession to return lap information for.                                                                                                |
| car_class_id=None                              | For multiclass races, you can specify to return the lap data for a single class.                                                               |
| sim_session_type=<br>SimSessionType.race.value | Which segment of a race session to return results for. (Practice, Qualify, Race)<br> The `SimSessionType` enum is from the `constants` module. |

### season_from_session()
Returns a single `season_id` that the `session_id` was for.

| Args/Kwargs | Description                                    |
| :---------- | :--------------------------------------------- |
| session_id  | Which `session_id` to return a `season_id` for |

### subsession_data()
Returns extensive data about a session. This endpoint contains unique datapoints that are unavailable elsewhere. <br>**!Note:** The segments of a session are not seperated (Practice, Qualify, Race). Results for each driver for each segment are listed concurrently. e.g If 25 drivers participate, there will be 75 `Driver` objects returned. 25 for each session segment.

| Args/Kwargs   | Description                        |
| :------------ | :--------------------------------- |
| subsession_id | Which subsession's data to return. |

### total_registered_all()
Broken at the moment
~~Returns a list of every upcoming session and the number of drivers that have registered. This data is used in the small text next to each series name in /Series.do that shows number of registered drivers for that series.~~

| Args/Kwargs | Description |
| :---------- | :---------- |


## Global Data


### car_class_by_id()
Returns a `CarClass` object from the given `car_class_id`.

| Args/Kwargs    | Description                                                                                                                                                                                                                                                       |
| :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| car_class_id=0 | Which car_class to retrieve. The default value of `0` returns a unique CarClass: `HostedAllCarsClass`.<br> Instead of returning `car` objects in the `cars_in_class` attribute, `HostedAllCarsClass` is a list of all CarClasses with attributes "name" and "id". |


### current_seasons()
Returns a Season object for every season.

| Args/Kwargs   | Description                                                        |
| :------------ | :----------------------------------------------------------------- |
| only_active=1 | Set to `0` to include all previous seasons *and* currently active. |
| kwargs        | See table below for available boolean kwargs.                      |

*Setting any of these to `=False` will hide that field in the   returned data*
<table>
<tr>
    <td>series_short_name</td>
    <td>cat_id</td>
    <td>season_id</td>
    <td>year</td>
</tr>
<tr>
    <td>quarter</td>
    <td>series_id</td>
    <td>active</td>
    <td>license_eligible</td>
</tr>
<tr>
    <td> only_active </td>
    <td> is_lite </td>
    <td> car_classes </td>
    <td> tracks </td>
</tr>
<tr>
    <td>start</td>
    <td>end</td>
    <td>cars</td>
    <td>race_week</td>
</tr>
<tr>
    <td>category</td>
    <td>series_lic_group_id</td>
    <td>car_id</td>
    <td></td>
</tr>

</table>

### world_records()
Returns laptimes with the requested paramaters. Filters can also be seen on the /worldrecords.jsp page on the membersite.

| Args/Kwargs  | Description                                                               |
| :----------- | :------------------------------------------------------------------------ |
| year         | Which year to return lap records for.                                     |
| quarter      | Which quarter/season to return lap records for.                           |
| car_id       | Which car to return lap records for.                                      |
| track_id     | Which track to return lap records for.                                    |
| cust_id=None | Only works if cust_id matches the logged in user. Otherwise does nothing. |
