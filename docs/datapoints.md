# Data Points


## Driver Profile Stats

### CareerStats


Data points returned from [`Client.career_stats()`](methods.md#career_stats)

|   Attributes   | Type  | Example |
| :------------: | :---: | :-----: |
|    category    |  str  | 'Road'  |
| incidents_avg  | float |  5.19   |
|      laps      |  int  |  4818   |
|    laps_led    |  int  |   101   |
| laps_led_pcnt  | float |   2.1   |
|   points_avg   |  int  |   47    |
|  points_club   |  int  |  1478   |
|     poles      |  int  |    3    |
| pos_finish_avg |  int  |   10    |
| pos_start_avg  |  int  |   10    |
|     starts     |  int  |   282   |
|   top_5_pcnt   | float |  25.89  |
|     top_5s     |  int  |   73    |
|    win_pcnt    | float |  1.77   |
|      wins      |  int  |    5    |

### YearlyStats

Data points returned from [`Client.yearly_stats()`](methods.md#yearly_stats)

|   Attributes   | Type  | Example |
| :------------: | :---: | :-----: |
|    category    |  str  | 'Road'  |
| incidents_avg  | float |  5.19   |
|      laps      |  int  |  4818   |
|    laps_led    |  int  |   101   |
| laps_led_pcnt  | float |   2.1   |
|   points_avg   |  int  |   47    |
|  points_club   |  int  |  1502   |
|     poles      |  int  |    3    |
| pos_finish_avg |  int  |   10    |
| pos_start_avg  |  int  |   10    |
|     starts     |  int  |   282   |
|   top_5_pcnt   | float |  25.89  |
|     top_5s     |  int  |   73    |
|    win_pcnt    | float |  1.77   |
|      wins      |  int  |    5    |
|      year      |  str  | '2020'  |

### LastRacesStats

Data points returned from [`Client.last_races_stats()`](methods.md#last_races_stats)

|    Attributes     | Type  |           Example            |
| :---------------: | :---: | :--------------------------: |
|       date        |  str  |         '2020-07-25'         |
|     incidents     |  int  |              16              |
|     laps_led      |  int  |              0               |
|   points_champ    |  int  |              43              |
|    points_club    |  int  |              0               |
|    pos_finish     |  int  |              15              |
|     pos_start     |  int  |              13              |
|     season_id     |  int  |             2866             |
|     series_id     |  int  |             260              |
| strength_of_field |  int  |             1558             |
|   subsession_id   |  int  |           33616345           |
|       time        |  int  |        1595707200000         |
|       track       |  str  | 'Autódromo José Carlos Pace' |
|  winner_cust_id   |  int  |            19126             |
|  winner_laps_led  |  int  |              20              |
|    winner_name    |  str  |        'Charlie Bass'        |

### LastSeries

Data points returned from [`Client.last_series()`](methods.md#last_series)

|    Attributes     | Type  |                   Example                   |
| :---------------: | :---: | :-----------------------------------------: |
|   car_class_id    |  int  |                     30                      |
|     division      |  int  |                      2                      |
|     incidents     |  int  |                     102                     |
|       laps        |  int  |                     560                     |
|     laps_led      |  int  |                     25                      |
|   points_champ    |  int  |                     434                     |
|    points_club    |  int  |                     434                     |
|  pos_finish_avg   |  int  |                      9                      |
|   pos_start_avg   |  int  |                      7                      |
|     season_id     |  int  |                    2866                     |
|    season_name    |  str  | 'iRacing Grand Prix Series - 2020 Season 3' |
| season_name_short |  str  |               '2020 Season 3'               |
|      series       |  str  |         'iRacing Grand Prix Series'         |
|     series_id     |  int  |                     260                     |
| series_name_short |  str  |         'iRacing Grand Prix Series'         |
|    series_rank    |  int  |                     31                      |
|      starts       |  int  |                     18                      |
|      top_5s       |  int  |                      8                      |
|       weeks       |  int  |                      6                      |

### PersonalBests

Data points returned from [`Client.personal_bests()`](methods.md#personal_bests)

|  Attributes  | Type  |                    Example                     |
| :----------: | :---: | :--------------------------------------------: |
|  event_type  |  str  |                   'Practice'                   |
|   lap_best   |  str  |                   '1:24.927'                   |
| track_config |  str  |                  'Grand Prix'                  |
|   track_id   |  int  |                      266                       |
|  track_name  |  str  | 'Autodromo Internazionale Enzo e Dino Ferrari' |

## Historical

### DriverStats

Data points returned from [`Client.driver_stats()`](methods.md#driver_stats)

|     Attributes     | Type  |      Example      |
| :----------------: | :---: | :---------------: |
|      club_id       |  int  |        33         |
|     club_name      |  str  |    'Northwest'    |
|    club_points     |  int  |       1478        |
|    country_code    |  str  |       'US'        |
|      cust_id       |  int  |      435144       |
|    display_name    |  str  | 'Jacob Anderson7' |
|   field_size_avg   |  int  |        20         |
|    group_letter    |  str  |        'A'        |
|     group_name     |  str  |     'Class A'     |
|    helm_color_1    |  str  |     '111111'      |
|    helm_color_2    |  str  |     '65b82f'      |
|    helm_color_3    |  str  |     '172c59'      |
|   helm_face_type   |  int  |         0         |
|  helm_helmet_type  |  int  |         0         |
|    helm_pattern    |  int  |        65         |
|   incidents_avg    | float |       5.19        |
|      irating       |  int  |       2057        |
|    irating_rank    |  int  |       14234       |
|        laps        |  int  |       4818        |
|      laps_led      |  int  |        101        |
|   license_class    |  str  |     'A 3.20'      |
|  license_class_id  |  int  |         5         |
| license_class_rank |  int  |       13931       |
|   license_level    |  int  |        19         |
|       points       |  int  |       13124       |
|     points_avg     |  int  |        47         |
|   pos_finish_avg   |  int  |        10         |
|   pos_start_avg    |  int  |        10         |
|        rank        |  int  |       5581        |
|       region       |  str  |    'Region 4'     |
|        row         |  str  |        '1'        |
|       starts       |  int  |        282        |
|     sub_level      |  int  |        320        |
|   top_25_percent   |  int  |        56         |
|      ttrating      |  int  |       1378        |
|   ttrating_rank    |  int  |       10484       |
|        wins        |  int  |         5         |

### EventResults

Data points returned from [`Client.event_results()`](methods.md#event_results)

|      Attributes      | Type  |      Example      |
| :------------------: | :---: | :---------------: |
|     car_class_id     |  int  |        30         |
|        car_id        |  int  |        33         |
|     category_id      |  int  |         2         |
|       cust_id        |  int  |      435144       |
|      date_start      |  str  |   '2020.06.20'    |
|     display_name     |  str  | 'Jacob Anderson7' |
|      event_type      |  int  |         5         |
|      group_name      |  str  |     'Class A'     |
|     helm_color_1     |  str  |     '111111'      |
|     helm_color_2     |  str  |     '65b82f'      |
|     helm_color_3     |  str  |     '172c59'      |
|  helm_license_level  |  int  |        19         |
|     helm_pattern     |  int  |        65         |
|      incidents       |  int  |         3         |
|       lap_best       |  str  |    '1:14.971'     |
| lap_best_subsession  |  str  |    '1:14.119'     |
|    lap_qual_best     |  str  |     '00.000'      |
|    license_group     |  int  |         5         |
|   official_session   |  int  |         1         |
|     points_champ     |  int  |        41         |
|  points_champ_sort   |  int  |        41         |
|     points_club      |  int  |         0         |
|   points_club_sort   |  int  |         0         |
|   points_drop_race   |  int  |         1         |
|      pos_finish      |  int  |        11         |
|      pos_start       |  int  |         4         |
|      race_week       |  int  |         1         |
|     rank_session     |  int  |         1         |
|      row_number      |  int  |        25         |
|      season_id       |  int  |       2866        |
|    season_quarter    |  int  |         3         |
|     season_year      |  int  |       2020        |
|      series_id       |  int  |        260        |
|      session_id      |  int  |     132876167     |
|  strength_of_field   |  int  |       1644        |
|    subsession_id     |  int  |     33057472      |
|    time_finished     |  int  |         0         |
|      time_start      |  str  |     '08:00pm'     |
|    time_start_raw    |  int  |   1592683200000   |
|       track_id       |  int  |        149        |
| winner_display_name  |  str  |  'Kent Neilson'   |
| winner_helm_color_1  |  str  |     '003dff'      |
| winner_helm_color_2  |  str  |     'ffffff'      |
| winner_helm_color_3  |  str  |     '0045ff'      |
| winner_helm_pattern  |  int  |        66         |
| winner_license_level |  int  |        20         |
|   winners_group_id   |  int  |      425354       |

### PrivateResults

Data points returned from [`Client.private_results()`](methods.md#private_results)

|        Attributes        | Type  |                                  Example                                   |
| :----------------------: | :---: | :------------------------------------------------------------------------: |
|       car_class_id       |  int  |                                     79                                     |
|         car_ids          |  str  |                                 72,117,118                                 |
|          cat_id          |  int  |                                     2                                      |
|         created          |  int  |                               1594267926000                                |
|       drivers_max        |  int  |                                     60                                     |
|      fast_tows_num       |  int  |                                     2                                      |
|       fixed_setup        |  int  |                                     0                                      |
|       fog_density        |  int  |                                     0                                      |
|   full_course_cautions   |  int  |                                     0                                      |
|      hardcore_level      |  int  |                                     0                                      |
|       host_cust_id       |  int  |                                   94043                                    |
|    host_display_name     |  str  |                               Nick Haeusler                                |
|   host_helmet_color_1    |  str  |                                   2A3795                                   |
|   host_helmet_color_2    |  str  |                                   060BDD                                   |
|   host_helmet_color_3    |  str  |                                   4D6BC7                                   |
|  host_helmet_face_type   |  int  |                                     0                                      |
| host_helmet_helmet_type  |  int  |                                     0                                      |
|   host_helmet_pattern    |  int  |                                     8                                      |
|    host_license_level    |  int  |                                     15                                     |
|         humidity         |  int  |                                     63                                     |
|        incidents         |  str  |                                    `''`                                    |
|          ir_max          |  int  |                                     -1                                     |
|          ir_min          |  int  |                                     -1                                     |
|         lap_best         |  str  |                                    `''`                                    |
|      lic_level_max       |  int  |                                     -1                                     |
|      lic_level_min       |  int  |                                     -1                                     |
|       lonequalify        |  int  |                                     0                                      |
|        multiclass        |  int  |                                     1                                      |
|    pct_fuel_fills_max    |  str  |            100,100,30,100,100,30,100,100,30,100,100,30,100,100             |
|        pos_finish        |  str  |                                    `''`                                    |
|     pos_finish_class     |  str  |                                    `''`                                    |
|        pos_start         |  str  |                                    `''`                                    |
|     pos_start_class      |  str  |                                    `''`                                    |
|     practice_length      |  int  |                                     90                                     |
|         private          |  int  |                                     0                                      |
|        qual_laps         |  int  |                                     0                                      |
|       qual_length        |  int  |                                     30                                     |
|   qual_setup_filenames   |  str  |                                    `''`                                    |
|      qual_setup_ids      |  str  |                                    `''`                                    |
|        race_laps         |  int  |                                    126                                     |
|       race_length        |  int  |                                    240                                     |
|   race_setup_filenames   |  str  |                                    `''`                                    |
|      race_setup_ids      |  str  |                                    `''`                                    |
|    race_time_finished    |  int  |                               1594390250000                                |
|         restarts         |  int  |                                     0                                      |
|      rolling_starts      |  int  |                                     0                                      |
|           row            |  int  |                                     1                                      |
|     session_fast_lap     |  int  |                                  1215599                                   |
|        session_id        |  int  |                                 134045275                                  |
|    session_id_private    |  int  |                                  1790911                                   |
|       session_name       |  str  |                         AOSC Round 1 - Silverstone                         |
|          skies           |  int  |                                     1                                      |
|      subsession_id       |  int  |                                  33375595                                  |
| subsession_time_finished |  int  |                               1594390551000                                |
|        temp_unit         |  int  |                                     1                                      |
|        temp_value        | float |                                 18.333334                                  |
|       time_of_day        |  int  |                                     0                                      |
|        time_start        |  int  |                               1594368005000                                |
|          track           |  str  |                            Silverstone Circuit                             |
|         track_id         |  int  |                                    341                                     |
|       weather_type       |  int  |                                     3                                      |
|     weight_penalties     |  str  |      0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0       |
|      wind_direction      |  int  |                                     6                                      |
|     wind_speed_unit      |  int  |                                     1                                      |
|     wind_speed_value     |  int  |                                     22                                     |
|   winner_display_name    |  str  |                          Logitech G Altus Esports                          |
|   winner_display_names   |  str  | Logitech G Altus Esports,Logitech G Altus Esports,Logitech G Altus Esports |
|     winner_group_id      |  int  |                                   -65804                                   |
|  winner_helmet_color_1   |  str  |                                   N%2FA                                    |
|  winner_helmet_color_2   |  str  |                                   N%2FA                                    |
|  winner_helmet_color_3   |  str  |                                   N%2FA                                    |
|  winner_helmet_pattern   |  int  |                                     -1                                     |
|   winner_license_level   |  int  |                                     -1                                     |

### SeasonStandings

Data points returned from [`Client.season_standings()`](methods.md#season_standings)

|    Attributes     | Type  |     Example      |
| :---------------: | :---: | :--------------: |
|      club_id      |  int  |        36        |
|     club_name     |  str  |    'UK and I'    |
|      country      |  str  | 'United Kingdom' |
|   country_code    |  str  |       'GB'       |
|   country_name    |  str  | 'United Kingdom' |
|      cust_id      |  int  |      55441       |
|   display_name    |  str  |  'Mark Ussher'   |
|     division      |  int  |        0         |
|      dropped      |  int  |        0         |
|   helm_color_1    |  str  |     '0116bf'     |
|   helm_color_2    |  str  |     'ffffff'     |
|   helm_color_3    |  str  |     '46b8f4'     |
|   helm_pattern    |  int  |        14        |
|     incidents     |  int  |        65        |
|      irating      |  int  |       5619       |
|       laps        |  int  |       613        |
|     laps_led      |  int  |       308        |
| license_level_max |  int  |        20        |
|      points       |  int  |       1212       |
|       poles       |  int  |        9         |
|        pos        |  int  |        1         |
|  pos_finish_avg   |  int  |        6         |
|   pos_start_avg   |  int  |        3         |
|       rank        |  int  |        1         |
|        row        |  int  |        1         |
|      starts       |  int  |        16        |
|     sub_level     |  str  |      '4.87'      |
|     top_fives     |  int  |        12        |
|       week        |  int  |        0         |
|       wins        |  int  |        7         |

### SeriesRaceResults

Data points returned from [`Client.series_race_results()`](methods.md#series_race_results)

|    Attributes     | Type  |    Example    |
| :---------------: | :---: | :-----------: |
|   car_class_id    |  int  |      30       |
|     official      |  int  |       0       |
|    session_id     |  int  |   132171426   |
|   size_of_field   |  int  |       2       |
| strength_of_field |  int  |     1552      |
|   subsession_id   |  int  |   32855187    |
|    time_start     |  int  | 1591668000000 |
|     track_id      |  int  |      163      |

### WorldRecord

Data points returned from [`Client.world_records()`](methods.md#world_records)

|       Attributes       | Type  |      Example       |
| :--------------------: | :---: | :----------------: |
|         car_id         |  int  |         33         |
|         cat_id         |  int  |         2          |
|        category        |  str  |       'Road'       |
|        club_id         |  int  |         41         |
|       club_name        |  str  |      'Italy'       |
|      country_code      |  str  |        'IT'        |
|        cust_id         |  int  |       297304       |
|      display_name      |  str  | 'Marco Sanfilippo' |
|      helm_color_1      |  str  |      'D4AF37'      |
|      helm_color_2      |  str  |      'FFFFFF'      |
|      helm_color_3      |  str  |      '000000'      |
|      helm_pattern      |  int  |         64         |
|        irating         |  int  |        4693        |
|     license_class      |  str  |      'A 4.99'      |
|    license_class_id    |  int  |         5          |
|     license_level      |  int  |         20         |
|        practice        |  str  |     '1:08.065'     |
|  practice_start_time   |  int  |   1563628621000    |
| practice_subsession_id |  int  |      27864149      |
|        qualify         |  str  |     '1:08.252'     |
| qualify_subsession_id  |  int  |      27864491      |
|   qualify_time_start   |  int  |   1563631200000    |
|          race          |  str  |     '1:08.675'     |
|    race_start_time     |  int  |   1563631200000    |
|   race_subsession_id   |  int  |      27864491      |
|         region         |  str  |     'Region 6'     |
|          row           |  int  |         1          |
|     season_quarter     |  str  |        '3'         |
|      season_year       |  str  |       '2019'       |
|       sub_level        |  int  |        499         |
|       timetrial        |  str  |         ''         |
|        track_id        |  int  |        319         |
|     tt_start_time      |  int  |         0          |
|    tt_subsession_id    |  int  |         ''         |
|        ttrating        |  int  |        1350        |

## iRacing Data

### Season

Data points returned from [`Client.current_seasons()`](methods.md#current_seasons)

|     Attributes      | Type  |                Example                |
| :-----------------: | :---: | :-----------------------------------: |
|       active        | bool  |                 True                  |
|       cat_id        |  int  |                   2                   |
|      category       |  int  |                   2                   |
|      date_end       |  int  |             1599523200000             |
|     date_start      |  int  |             1591660800000             |
|       is_lite       | bool  |                 False                 |
|  license_eligible   | bool  |                 True                  |
|      race_week      |  int  |                   8                   |
|      season_id      |  int  |                 2846                  |
|   season_quarter    |  int  |                   3                   |
|     season_year     |  int  |                 2020                  |
|      series_id      |  int  |                  231                  |
| series_lic_group_id |  int  |                   3                   |
|  series_name_short  |  str  |   'Advanced Mazda MX-5 Cup Series'    |
|        cars         | list  |      See [SeasonCar](#seasoncar)      |
|       tracks        | list  |          See [Track](#track)          |
|     car_classes     | list  | See [SeasonCarClass](#seasoncarclass) |

#### SeasonCar

| Attribute  | Type  |         Example         |
| :--------: | :---: | :---------------------: |
|     id     |  int  |           67            |
|    name    |  str  | 'Global Mazda MX-5 Cup' |
| name_lower |  str  | 'global mazda mx-5 cup' |
|   pkg_id   |  int  |           182           |
|    sku     |  int  |          10394          |

#### Track

|  Attribute  | Type  |        Example         |
| :---------: | :---: | :--------------------: |
|    name     |  str  | 'Brands Hatch Circuit' |
| name_lower  |  str  | 'brands hatch circuit' |
|   pkg_id    |  int  |           91           |
|  priority   |  int  |           1            |
|  race_week  |  int  |           7            |
| time_of_day |  int  |           2            |
|   config    |  str  |      'Grand Prix'      |

#### SeasonCarClass

!!! Note "v0.1.0 Name Differences"
    In v0.1.0 the names are `custid`, `lowername`, and `shortname`.  
    In future releases they are updated to `cust_id`, `name_lower`, and `name_short`.

|     Attribute     | Type  |        Example        |
| :---------------: | :---: | :-------------------: |
|      cust_id      |  int  |           0           |
|        id         |  int  |          74           |
|    name_lower     |  str  | 'mazda mx-5 cup 2016' |
|       name        |  str  | 'Mazda MX-5 Cup 2016' |
|     rel_speed     |  int  |          33           |
|    name_short     |  str  |    'MX5 Cup 2016'     |
|       cars        | list  |    See [Car](#car)    |
| tire_sets_dry_max |  int  |           0           |

##### Car

| Attribute | Type  |         Example         |
| :-------: | :---: | :---------------------: |
|    id     |  int  |           67            |
|   name    |  str  | 'Global Mazda MX-5 Cup' |

### CarClass

Data points returned from [`Client.car_class()`](methods.md#car_class)

| Attributes | Type  |          Example          |
| :--------: | :---: | :-----------------------: |
|  cust_id   |  int  |             0             |
|     id     |  int  |             1             |
| name_lower |  str  | 'skip barber race series' |
|    name    |  str  | 'Skip Barber Race Series' |
| rel_speed  |  int  |            40             |
| name_short |  str  |          'SBRS'           |
|    cars    | list  |      See [Car](#car)      |


## Upcoming

### OpenPractice

Data points returned from [`Client.active_op_counts()`](methods.md#active_op_counts)

|       Attributes       | Type  |            Example            |
| :--------------------: | :---: | :---------------------------: |
|      allow_entry       |  str  |             true              |
|       cars_left        |  str  |              10               |
|         cat_id         |  int  |               2               |
|      count_group       |  int  |              54               |
|    count_registered    |  str  |             74:53             |
|      count_total       |  int  |              54               |
| driver_change_param_1  |  int  |               0               |
| driver_change_param_2  |  int  |               0               |
|   driver_change_rule   |  int  |               0               |
|     driver_changes     |  int  |               0               |
|   drivers_connected    |  str  |              42               |
|   drivers_registered   |  str  |              54               |
| earth_rotation_speedup |  int  |               1               |
|        farm_id         |  str  |              11               |
|      fog_density       |  int  |               0               |
|        humidity        |  int  |              55               |
|     leave_marbles      |  int  |               0               |
|          pits          |  str  |             49/60             |
|      pits_in_use       |  int  |              49               |
|       pits_total       |  int  |              60               |
|     race_panel_img     |  str  |     seriesid_139/logo.jpg     |
|    rubber_practice     |  str  |             `''`              |
|     rubber_qualify     |  str  |             `''`              |
|      rubber_race       |  str  |             `''`              |
|     rubber_warmup      |  str  |             `''`              |
|       season_id        |  int  |             2823              |
|      series_abbrv      |  str  |             FGMMC             |
|       series_id        |  int  |              139              |
|      series_name       |  str  | Fanatec Global Mazda MX-5 Cup |
|       session_id       |  int  |           135263060           |
|         skies          |  int  |               1               |
|     subsession_id      |  int  |           33693275            |
|    team_drivers_max    |  int  |               1               |
|    team_drivers_min    |  int  |               1               |
|       temp_unit        |  int  |               0               |
|       temp_value       |  int  |              78               |
|      time_of_day       |  int  |               0               |
|       time_start       |  str  |             00:50             |
|     time_start_sim     |  str  |       2019-05-20 14:05        |
|      total_groups      |  int  |              54               |
|      track_config      |  str  |             Short             |
|        track_id        |  int  |              167              |
|       track_name       |  str  | Okayama International Circuit |
|    weather_initial     |  int  |               0               |
|    weather_ongoing     |  int  |               0               |
|      weather_type      |  int  |               3               |
|     wind_direction     |  int  |               0               |
|    wind_speed_unit     |  int  |               0               |
|    wind_speed_value    |  int  |               2               |


### NextEvent

Data points returned from [`Client.next_event()`](methods.md#next_event)

|  Attributes  |       Type        |       Example       |
| :----------: | :---------------: | :-----------------: |
| driver_count |        int        |         10          |
|  season_id   |        int        |        2844         |
|  session_id  |        int        |      135215452      |
|  time_start  | datetime.datetime | 2020-07-30 00:15:00 |

### NextSessionTimes

Data points returned from [`Client.next_session_times()`](methods.md#next_session_times)

|       Attributes       |       Type        |                                               Example                                                |
| :--------------------: | :---------------: | :--------------------------------------------------------------------------------------------------: |
| earth_rotation_speedup |        int        |                                                  0                                                   |
|     event_type_id      |        int        |                                                  4                                                   |
|      fog_density       |        int        |                                                  0                                                   |
|      group_count       |        int        |                                                  0                                                   |
|        humidity        |        int        |                                                  55                                                  |
|     leave_marbles      |        int        |                                                  1                                                   |
|     max_to_display     |        int        |                                                  5                                                   |
|       race_week        |        int        |                                                  7                                                   |
|     race_week_cars     |       dict        | {'33': {'maxPctFuelFill': 67, 'weightPenaltyKG': '', 'max_dry_tire_sets': '', 'powerAdjustPct': ''}} |
|       reg_count        |        int        |                                                  0                                                   |
|    rubber_practice     |        str        |                                                 `''`                                                 |
|     rubber_qualify     |        str        |                                                 `''`                                                 |
|      rubber_race       |        str        |                                                 `''`                                                 |
|     rubber_warmup      |        str        |                                                 `''`                                                 |
|       season_id        |        int        |                                                 2866                                                 |
|       session_id       |        int        |                                              135261628                                               |
|         skies          |        int        |                                                  1                                                   |
|   special_event_type   |        int        |                                                  0                                                   |
|       temp_unit        |        int        |                                                  0                                                   |
|       temp_value       |        int        |                                                  78                                                  |
|      time_of_day       |        int        |                                                  1                                                   |
|       time_start       | datetime.datetime |                                         2020-07-30 18:52:00                                          |
|     time_start_sim     |        str        |                                           2020-08-01 08:20                                           |
|      total_count       |        int        |                                                  0                                                   |
|      total_groups      |        int        |                                                  0                                                   |
|        track_id        |        int        |                                                 319                                                  |
|    weather_initial     |        int        |                                                  0                                                   |
|    weather_ongoing     |        int        |                                                  0                                                   |
|      weather_type      |        int        |                                                  0                                                   |
|     wind_direction     |        int        |                                                  0                                                   |
|    wind_speed_unit     |        int        |                                                  0                                                   |
|    wind_speed_value    |        int        |                                                  2                                                   |

### RaceGuide

Data points returned from [`Client.race_guide()`](methods.md#race_guide)

|       Attributes        | Type  |                   Example                    |
| :---------------------: | :---: | :------------------------------------------: |
|         cat_id          |  int  |                      1                       |
|        eligible         | bool  |                     True                     |
|          image          |  str  | 'member_images/series/seriesid_116/logo.jpg' |
| meets_participation_req |  int  |                      0                       |
|     season_schedule     | list  |          See [Schedule](#schedule)           |
|        series_id        |  int  |                     116                      |
|       series_name       |  str  |               'Carburetor Cup'               |

#### Schedule

|       Attributes       |   Type   |       Example       |
| :--------------------: | :------: | :-----------------: |
|     car_class_ids      |   list   |        [50]         |
|      fixed_setup       |   bool   |        True         |
|     license_class      |   int    |          1          |
|      multi_class       |   bool   |        False        |
| open_practice_drivers  |   int    |          8          |
| open_practice_sessions |   int    |         10          |
|          race          |   list   |  See [Race](#race)  |
|       season_id        |   int    |        2867         |
|   season_start_date    | datetime | 2020-06-09 00:00:00 |

##### Race

|       Attributes        |       Type        |             Example              |
| :---------------------: | :---------------: | :------------------------------: |
| earth_rotation_speedup  |        int        |                1                 |
|       event_type        |        int        |                5                 |
|       fog_density       |        int        |                0                 |
|        humidity         |        int        |                55                |
|     race_lap_limit      |        int        |                15                |
| race_time_limit_minutes |        int        |                -1                |
|        race_week        |        int        |                7                 |
|        reg_count        |        int        |                6                 |
|      reg_count_pre      |        int        |                0                 |
|       session_id        |        int        |            135216789             |
|     session_type_id     |        int        |               278                |
|          skies          |        int        |                1                 |
|   special_event_type    |        int        |                0                 |
|     standing_start      |       bool        |              False               |
|        temp_unit        |        int        |                0                 |
|       temp_value        |        int        |                78                |
|        time_end         | datetime.datetime |       2020-07-30 19:00:31        |
|       time_of_day       |        int        |                9                 |
|       time_start        | datetime.datetime |       2020-07-30 18:45:00        |
|     time_start_sim      |        str        |         2019-05-21 12:00         |
|          track          |        str        | '[Legacy] Pocono Raceway - 2009' |
|      track_config       |        str        |              'Oval'              |
|        track_id         |        int        |               136                |
|  track_race_guide_img   |        str        |                ''                |
|     weather_initial     |        int        |                0                 |
|     weather_ongoing     |        int        |                0                 |
|      weather_type       |        int        |                3                 |
|     wind_direction      |        int        |                0                 |
|     wind_speed_unit     |        int        |                0                 |
|    wind_speed_value     |        int        |                2                 |
|     race_week_cars      |       dict        |                {}                |
|     rubber_settings     |       dict        |                {}                |

## Session Data

### SubSessionData

Data points returned from [`Client.subsession_data()`](methods.md#subsession_data)

|       Attributes        | Type  |                   Example                   |
| :---------------------: | :---: | :-----------------------------------------: |
|         cat_id          |  int  |                      1                      |
|      caution_laps       |  int  |                     18                      |
|      caution_type       |  int  |                      3                      |
|        cautions         |  int  |                      6                      |
|      corners_total      |  int  |                      4                      |
|  driver_change_param_1  |  int  |                     -1                      |
|  driver_change_param_2  |  int  |                     -1                      |
|   driver_change_rule    |  int  |                      0                      |
|     driver_changes      |  int  |                      0                      |
|       event_type        |  int  |                      5                      |
|       fog_density       |  int  |                      0                      |
|        humidity         |  int  |                     55                      |
|         lap_avg         |  int  |                   696237                    |
|     laps_completed      |  int  |                     50                      |
|    laps_for_qual_avg    |  int  |                      2                      |
|    laps_for_solo_avg    |  int  |                     10                      |
|      lead_changes       |  int  |                      3                      |
|        league_id        |  str  |                    `''`                     |
|    league_season_id     |  str  |                    `''`                     |
|      leave_marbles      |  int  |                      1                      |
|        max_weeks        |  int  |                     13                      |
|       points_type       |  str  |                    race                     |
|   private_session_id    |  int  |                     -1                      |
|        race_week        |  int  |                      7                      |
|     reserve_status      |  str  |                    `''`                     |
|     rubber_practice     |  int  |                     -1                      |
|     rubber_qualify      |  int  |                     -1                      |
|       rubber_race       |  int  |                     -1                      |
|      rubber_warmup      |  int  |                     -1                      |
|        season_id        |  int  |                    2844                     |
|       season_name       |  str  | INDYCAR Series - Oval - 2020 Season 3 Fixed |
|    season_name_short    |  str  |             2020 Season 3 Fixed             |
|     season_quarter      |  int  |                      3                      |
|       season_year       |  int  |                    2020                     |
|        series_id        |  int  |                     165                     |
|       series_name       |  str  |        IndyCar Series - Oval - Fixed        |
|    series_name_short    |  str  |        IndyCar Series - Oval - Fixed        |
|       session_id        |  int  |                  135205454                  |
|      session_name       |  str  |                    `''`                     |
|      sim_ses_type       |  int  |                      3                      |
|          skies          |  int  |                      1                      |
|   special_event_type    |  int  |                     -1                      |
| special_event_type_text |  str  |                    `''`                     |
|    strength_of_field    |  int  |                    1517                     |
|      subsession_id      |  int  |                  33679352                   |
|    team_drivers_max     |  int  |                      1                      |
|    team_drivers_min     |  int  |                      1                      |
|        temp_unit        |  int  |                      0                      |
|       temp_value        |  int  |                     78                      |
|       time_of_day       |  int  |                      2                      |
|       time_start        |  str  |             2020-07-29 20:15:00             |
|     time_start_sim      |  str  |              2020-07-14 15:05               |
|          track          |  str  |               Pocono Raceway                |
|      track_config       |  str  |                     N/A                     |
|        track_id         |  int  |                     277                     |
|     weather_initial     |  int  |                      0                      |
|     weather_ongoing     |  int  |                      0                      |
|      weather_type       |  int  |                      3                      |
|     wind_direction      |  int  |                      0                      |
|     wind_speed_unit     |  int  |                      0                      |
|    wind_speed_value     |  int  |                      2                      |
|         drivers         | list  |            See [Driver](#driver)            |

#### Driver

|      Attributes      | Type  |     Example     |
| :------------------: | :---: | :-------------: |
|     car_class_id     |  int  |       117       |
|    car_class_name    |  str  |  Dallara IR18   |
| car_class_name_short |  str  |  Dallara IR18   |
|     car_color_1      |  str  |     ffffff      |
|     car_color_2      |  str  |     cccccc      |
|     car_color_3      |  str  |     666666      |
|        car_id        |  int  |       99        |
|       car_num        |  str  |       23        |
|     car_num_font     |  int  |        0        |
|    car_num_slant     |  int  |        0        |
|  car_number_color_1  |  str  |     ffffff      |
|  car_number_color_2  |  str  |     cccccc      |
|  car_number_color_3  |  str  |     666666      |
|     car_pattern      |  int  |        0        |
|    car_sponser_1     |  int  |        0        |
|    car_sponser_2     |  int  |        0        |
|       club_id        |  int  |       17        |
|      club_name       |  str  |    Virginias    |
|   club_name_short    |  str  |    Virginias    |
|     club_points      |  int  |        0        |
|       cpi_new        | float |   18.8930492    |
|       cpi_old        | float |   19.7769318    |
|       cust_id        |  int  |     383175      |
|     damage_model     |  int  |        0        |
|     display_name     |  str  |  Joseph Lester  |
|       division       |  int  |        3        |
|    division_name     |  str  | Bronze Division |
|      drop_race       |  int  |        0        |
|   event_type_name    |  str  |      Race       |
|       group_id       |  int  |     383175      |
|     heat_info_id     |  int  |       -1        |
|     helm_color_1     |  str  |     ffffff      |
|     helm_color_2     |  str  |     fc1406      |
|     helm_color_3     |  str  |     06baf5      |
|     helm_pattern     |  int  |        2        |
|       host_id        |  str  |      `''`       |
|      incidents       |  int  |        0        |
|       interval       |  int  |        0        |
|    interval_class    |  int  |        0        |
|     irating_new      |  int  |      1280       |
|     irating_old      |  int  |      1316       |
|       lap_avg        |  int  |     432343      |
|       lap_best       |  int  |     432343      |
|      lap_best_n      |  int  |        1        |
|    lap_qual_best     |  int  |       -1        |
|   lap_qual_best_at   |  int  |        0        |
|   lap_qual_best_n    |  int  |       -1        |
|  lap_qual_best_time  |  int  |       -1        |
|   laps_best_n_num    |  int  |       -1        |
|   laps_best_n_time   |  int  |       -1        |
|      laps_comp       |  int  |        1        |
|       laps_led       |  int  |        0        |
|    laps_opt_comp     |  int  |        0        |
|    league_points     |  str  |      `''`       |
|   license_category   |  str  |      Oval       |
| license_change_oval  |  int  |       -1        |
| license_change_road  |  int  |       -1        |
|    license_class     |  int  |        3        |
|  license_level_new   |  int  |       13        |
|  license_level_old   |  int  |       13        |
|      multiplier      |  int  |        1        |
|       official       |  int  |        1        |
|  pct_fuel_fill_max   |  int  |       -1        |
|     points_champ     |  int  |        0        |
|   points_champ_agg   |  int  |       24        |
|         pos          |  int  |        0        |
|      pos_finish      |  int  |        0        |
|   pos_finish_class   |  int  |        0        |
|      pos_start       |  int  |       -1        |
|      reason_out      |  str  |     Running     |
|    reason_out_id     |  int  |        0        |
|   restrict_results   |  str  |      `''`       |
|     sim_ses_name     |  str  |    PRACTICE     |
|     sim_ses_num      |  int  |       -2        |
|  sim_ses_type_name   |  str  |  Open Practice  |
|    sub_level_new     |  int  |       126       |
|    sub_level_old     |  int  |       133       |
|     suit_color_1     |  str  |     ffffff      |
|     suit_color_2     |  str  |     fc1406      |
|     suit_color_3     |  str  |     059fff      |
|     suit_pattern     |  int  |        1        |
|  time_session_start  |  int  |  1596053700000  |
|     track_cat_id     |  int  |        1        |
|    track_category    |  str  |      Oval       |
|     ttrating_new     |  int  |      1362       |
|     ttrating_old     |  int  |      1362       |
|    vehicle_key_id    |  int  |      5203       |
|  weight_penalty_kg   |  int  |       -1        |
|     wheel_chrome     |  int  |       -1        |
|     wheel_color      |  str  |       N/A       |

### RaceLapsAll
Data points returned from [`Client.race_laps_all()`](methods.md#race_laps_all)

| Attributes |  Type  |         Example         |
| :--------: | :----: | :---------------------: |
|  details   | object | See [Details](#details) |
|   driver   |  list  |  See [Driver](#driver)  |
|    laps    |  list  | See [LapData](#lapdata) |

#### Details
|      Attributes      | Type  |                  Example                   |
| :------------------: | :---: | :----------------------------------------: |
|         date         |  str  |                 2020-06-20                 |
|   date_unix_utc_ms   |  int  |               1592683200000                |
|    driver_changes    | bool  |                   False                    |
|      event_type      |  int  |                     5                      |
|   event_type_name    |  str  |                    Race                    |
|  laps_for_qual_avg   |  int  |                     2                      |
|  laps_for_solo_avg   |  int  |                     5                      |
|       official       |  int  |                     1                      |
|  private_session_id  |  int  |                     -1                     |
| private_session_name |  str  |                    `''`                    |
|    race_panel_img    |  str  | member_images/series/seriesid_260/logo.jpg |
|      race_week       |  int  |                     1                      |
|      season_id       |  int  |                    2866                    |
|     season_name      |  str  | iRacing Grand Prix Series - 2020 Season 3  |
|  season_name_short   |  str  |               2020 Season 3                |
|     series_name      |  str  |         iRacing Grand Prix Series          |
|  series_name_short   |  str  |         iRacing Grand Prix Series          |
|      session_id      |  int  |                 132876167                  |
|    subsession_id     |  int  |                  33057472                  |
|        track         |  str  |           Circuit Park Zandvoort           |
|     track_config     |  str  |                 Grand Prix                 |
|       track_id       |  int  |                    149                     |

#### Driver
|   Attributes   | Type  |   Example    |
| :------------: | :---: | :----------: |
|    car_num     |  str  |      9       |
|    cust_id     |  int  |    425354    |
|  display_name  |  str  | Kent Neilson |
|     friend     |  int  |      1       |
|    group_id    |  int  |    425354    |
| helmet_color_1 |  str  |    003dff    |
| helmet_color_2 |  str  |    ffffff    |
| helmet_color_3 |  str  |    0045ff    |
| helmet_pattern |  int  |      66      |
|   incidents    |  int  |      0       |
|    lap_avg     |  int  |    755884    |
|  lap_best_num  |  int  |      23      |
| lap_best_time  |  int  |    741191    |
| license_color  |  str  |    0153db    |
|  points_champ  |  int  |     101      |
|   pos_finish   |  int  |      0       |
|   pos_start    |  int  |      0       |
|     watch      |  int  |      0       |

#### LapData
| Attributes | Type  | Example |
| :--------: | :---: | :-----: |
|  car_num   |  str  |   '9'   |
|  cust_id   |  int  | 425354  |
|   flags    |  int  |    0    |
|  lap_num   |  int  |    0    |
|  time_ses  |  int  | 966667  |

### RaceLapsDriver

Data points returned from [`Client.race_laps_driver()`](methods.md#race_laps_driver)

| Attributes |  Type  |        Example        |
| :--------: | :----: | :-------------------: |
|  drivers   |  list  | See [Driver](#driver) |
|   header   | object | See [Header](#header) |
|    laps    |  list  |  See [Lap](#lapdata)  |

#### Driver
|    Attributes    | Type  |      Example      |
| :--------------: | :---: | :---------------: |
|     cust_id      |  int  |      435144       |
|   display_name   |  str  | 'Jacob Anderson7' |
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

#### Header
|    Attributes     | Type  |                  Example                  |
| :---------------: | :---: | :---------------------------------------: |
|    car_color_1    |  str  |                  111111                   |
|    car_color_2    |  str  |                  65b82f                   |
|    car_color_3    |  str  |                  172c59                   |
|      car_id       |  int  |                    33                     |
|      car_num      |  str  |                     4                     |
|    car_pattern    |  int  |                     1                     |
| date_unix_utc_ms  |  int  |               1595707200000               |
|    event_date     |  str  |                2020-07-25                 |
|    event_type     |  int  |                     5                     |
|  event_type_name  |  str  |                   Race                    |
|   laps_for_qual   |  int  |                     2                     |
|   laps_for_solo   |  int  |                     5                     |
|    season_name    |  str  | iRacing Grand Prix Series - 2020 Season 3 |
| season_name_short |  str  |               2020 Season 3               |
|    series_name    |  str  |         iRacing Grand Prix Series         |
| series_name_short |  str  |         iRacing Grand Prix Series         |
|    session_id     |  int  |                 134968003                 |
|   subsession_id   |  int  |                 33616345                  |
|   suit_color_1    |  str  |                  111111                   |
|   suit_color_2    |  str  |                  000000                   |
|   suit_color_3    |  str  |                  32713a                   |
|   suit_pattern    |  int  |                     1                     |
|     team_name     |  str  |                   `''`                    |
|   track_config    |  str  |                Grand Prix                 |
|     track_id      |  int  |                    212                    |
|    track_name     |  str  |        Autódromo José Carlos Pace         |

#### LapData
| Attributes | Type  | Example |
| :--------: | :---: | :-----: |
|  cust_id   |  int  | 435144  |
|   flags    |  int  |    0    |
|  lap_num   |  int  |    0    |
|  time_ses  |  int  | 1078620 |