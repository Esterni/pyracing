# race_guide
Data points returned from `Client.race_guide()`

## RaceGuide

|       Attributes        | Type  |                      Example                       |
| :---------------------: | :---: | :------------------------------------------------: |
|         cat_id          |  int  |                         1                          |
|        eligible         | bool  |                        True                        |
|          image          |  str  | 'member_images%2Fseries%2Fseriesid_116%2Flogo.jpg' |
| meets_participation_req |  int  |                         0                          |
|     season_schedule     | list  |             See [Schedule](#schedule)              |
|        series_id        |  int  |                        116                         |
|       series_name       |  str  |                  'Carburetor+Cup'                  |

## Schedule
|       Attributes       | Type  |      Example      |
| :--------------------: | :---: | :---------------: |
|     car_class_ids      | list  |       [50]        |
|      fixed_setup       | bool  |       True        |
|     license_class      |  int  |         1         |
|      multi_class       | bool  |       False       |
| open_practice_drivers  |  int  |         8         |
| open_practice_sessions |  int  |        10         |
|          race          | list  | See [Race](#race) |
|       season_id        |  int  |       2867        |
|   season_start_date    |  int  |   1591660800000   |

## Race
|       Attributes        | Type  |              Example               |
| :---------------------: | :---: | :--------------------------------: |
| earth_rotation_speedup  |  int  |                 1                  |
|       event_type        |  int  |                 5                  |
|       fog_density       |  int  |                 0                  |
|        humidity         |  int  |                 55                 |
|     race_lap_limit      |  int  |                 15                 |
| race_time_limit_minutes |  int  |                 -1                 |
|        race_week        |  int  |                 7                  |
|        reg_count        |  int  |                 6                  |
|      reg_count_pre      |  int  |                 0                  |
|       session_id        |  int  |             135216789              |
|     session_type_id     |  int  |                278                 |
|          skies          |  int  |                 1                  |
|   special_event_type    |  int  |                 0                  |
|     standing_start      | bool  |               False                |
|        temp_unit        |  int  |                 0                  |
|       temp_value        |  int  |                 78                 |
|        time_end         |  int  |           1596070831000            |
|       time_of_day       |  int  |                 9                  |
|       time_start        |  int  |           1596069900000            |
|     time_start_sim      |  str  |         2019-05-21+12%3A00         |
|          track          |  str  | %5BLegacy%5D+Pocono+Raceway+-+2009 |
|      track_config       |  str  |                Oval                |
|        track_id         |  int  |                136                 |
|  track_race_guide_img   |  str  |                 ''                 |
|     weather_initial     |  int  |                 0                  |
|     weather_ongoing     |  int  |                 0                  |
|      weather_type       |  int  |                 3                  |
|     wind_direction      |  int  |                 0                  |
|     wind_speed_unit     |  int  |                 0                  |
|    wind_speed_value     |  int  |                 2                  |
|     race_week_cars      | dict  |                 {}                 |
|     rubber_settings     | dict  |                 {}                 |