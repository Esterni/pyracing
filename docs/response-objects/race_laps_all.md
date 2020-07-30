# race_laps_all

## RaceLapsAll
| Attributes |  Type  |         Example         |
| :--------: | :----: | :---------------------: |
|  details   | object | See [Details](#details) |
|   driver   |  list  |  See [Driver](#driver)  |
|  lap_data  |  list  | See [LapData](#lapdata) |

## Details
|      Attributes      | Type  |                      Example                       |
| :------------------: | :---: | :------------------------------------------------: |
|         date         |  str  |                     2020-06-20                     |
|   date_unix_utc_ms   |  int  |                   1592683200000                    |
|    driver_changes    | bool  |                       False                        |
|      event_type      |  int  |                         5                          |
|   event_type_name    |  str  |                        Race                        |
|  laps_for_qual_avg   |  int  |                         2                          |
|  laps_for_solo_avg   |  int  |                         5                          |
|       official       |  int  |                         1                          |
|  private_session_id  |  int  |                         -1                         |
| private_session_name |  str  |                         ''                         |
|    race_panel_img    |  str  | 'member_images%2Fseries%2Fseriesid_260%2Flogo.jpg' |
|      race_week       |  int  |                         1                          |
|      season_id       |  int  |                        2866                        |
|     season_name      |  str  |    'iRacing+Grand+Prix+Series+-+2020+Season+3'     |
|  season_name_short   |  str  |                  '2020+Season+3'                   |
|     series_name      |  str  |            'iRacing+Grand+Prix+Series'             |
|  series_name_short   |  str  |            'iRacing+Grand+Prix+Series'             |
|      session_id      |  int  |                     132876167                      |
|    subsession_id     |  int  |                      33057472                      |
|        track         |  str  |              'Circuit+Park+Zandvoort'              |
|     track_config     |  str  |                    'Grand+Prix'                    |
|       track_id       |  int  |                        149                         |

## Driver
|   Attributes   | Type  |    Example     |
| :------------: | :---: | :------------: |
|    car_num     |  str  |      '9'       |
|    cust_id     |  int  |     425354     |
|  display_name  |  str  | 'Kent+Neilson' |
|     friend     |  int  |       1        |
|    group_id    |  int  |     425354     |
| helmet_color_1 |  str  |    '003dff'    |
| helmet_color_2 |  str  |    'ffffff'    |
| helmet_color_3 |  str  |    '0045ff'    |
| helmet_pattern |  int  |       66       |
|   incidents    |  int  |       0        |
|    lap_avg     |  int  |     755884     |
|  lap_best_num  |  int  |       23       |
| lap_best_time  |  int  |     741191     |
| license_color  |  str  |    '0153db'    |
|  points_champ  |  int  |      101       |
|   pos_finish   |  int  |       0        |
|   pos_start    |  int  |       0        |
|     watch      |  int  |       0        |

## LapData
| Attributes | Type  | Example |
| :--------: | :---: | :-----: |
|  car_num   |  str  |   '9'   |
|  cust_id   |  int  | 425354  |
|   flags    |  int  |    0    |
|  lap_num   |  int  |    0    |
|  time_ses  |  int  | 966667  |