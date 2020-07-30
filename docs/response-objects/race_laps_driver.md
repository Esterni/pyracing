# race_laps_driver
Data points returned from `Client.race_laps_driver()`


## RaceLapsDriver
| Attributes |  Type  |        Example        |
| :--------: | :----: | :-------------------: |
|  drivers   |  list  | See [Driver](#driver) |
|   header   | object | See [Header](#header) |
|  lap_data  |  list  |  See [Lap](#lapdata)  |

## Driver
|    Attributes    | Type  |      Example      |
| :--------------: | :---: | :---------------: |
|     cust_id      |  int  |      435144       |
|   display_name   |  str  | 'Jacob+Anderson7' |
|   helm_color_1   |  str  |     '111111'      |
|   helm_color_2   |  str  |     '65b82f'      |
|   helm_color_3   |  str  |     '172c59'      |
|   helm_pattern   |  int  |        65         |
|     lap_best     |  int  |      742635       |
|    lap_best_n    |  int  |         3         |
|  lap_qual_best   |  int  |        -1         |
| lap_qual_best_at |  int  |         0         |
| lap_qual_best_n  |  int  |        -1         |
| laps_n_best_num  |  int  |        -1         |
| laps_n_best_time |  int  |        -1         |
|  license_level   |  int  |        19         |

## Header
|    Attributes     | Type  |                   Example                   |
| :---------------: | :---: | :-----------------------------------------: |
|    car_color_1    |  str  |                  '111111'                   |
|    car_color_2    |  str  |                  '65b82f'                   |
|    car_color_3    |  str  |                  '172c59'                   |
|      car_id       |  int  |                     33                      |
|      car_num      |  str  |                     '4'                     |
|    car_pattern    |  int  |                      1                      |
| date_unix_utc_ms  |  int  |                1595707200000                |
|    event_date     |  str  |                '2020-07-25'                 |
|    event_type     |  int  |                      5                      |
|  event_type_name  |  str  |                   'Race'                    |
|   laps_for_qual   |  int  |                      2                      |
|   laps_for_solo   |  int  |                      5                      |
|    season_name    |  str  | 'iRacing+Grand+Prix+Series+-+2020+Season+3' |
| season_name_short |  str  |               '2020+Season+3'               |
|    series_name    |  str  |         'iRacing+Grand+Prix+Series'         |
| series_name_short |  str  |         'iRacing+Grand+Prix+Series'         |
|    session_id     |  int  |                  134968003                  |
|   subsession_id   |  int  |                  33616345                   |
|   suit_color_1    |  str  |                  '111111'                   |
|   suit_color_2    |  str  |                  '000000'                   |
|   suit_color_3    |  str  |                  '32713a'                   |
|   suit_pattern    |  int  |                      1                      |
|     team_name     |  str  |                     ''                      |
|   track_config    |  str  |                'Grand+Prix'                 |
|     track_id      |  int  |                     212                     |
|    track_name     |  str  |   'Aut%C3%B3dromo+Jos%C3%A9+Carlos+Pace'    |

## LapData
| Attributes | Type  | Example |
| :--------: | :---: | :-----: |
|  cust_id   |  int  | 435144  |
|   flags    |  int  |    0    |
|  lap_num   |  int  |    0    |
|  time_ses  |  int  | 1078620 |