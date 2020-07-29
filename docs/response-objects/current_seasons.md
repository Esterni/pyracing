# current_seasons
Data points returned from `Client.current_seasons()`

## Season

|     Attributes      |      Type       |             Example              |
| :-----------------: | :-------------: | :------------------------------: |
|       active        |     Boolean     |               True               |
|        cars         | List of Objects |      See [Car](#car-object)      |
|       cat_id        |       Int       |                2                 |
|     car_classes     | List of Objects |    See [CarClass](#carclass)     |
|      category       |       Int       |                2                 |
|      date_end       |       Int       |          1599523200000           |
|     date_start      |       Int       |          1591660800000           |
|       is_lite       |     Boolean     |              False               |
|  license_eligible   |     Boolean     |               True               |
|      race_week      |       Int       |                8                 |
|      season_id      |       Int       |               2846               |
|   season_quarter    |       Int       |                3                 |
|     season_year     |       Int       |               2020               |
|      series_id      |       Int       |               231                |
| series_lic_group_id |       Int       |                3                 |
|  series_name_short  |       Str       | 'Advanced Mazda MX-5 Cup Series' |
|       tracks        | List of Objects |       See [Track](#track)        |

### Car

| Attribute  | Type  |         Example         |
| :--------: | :---: | :---------------------: |
|     id     |  Int  |           67            |
|    name    |  Str  | 'Global Mazda MX-5 Cup  |
| name_lower |  Str  | 'global mazda mx-5 cup' |
|   pkg_id   |  Int  |           182           |
|    sku     |  Int  |          10394          |

### Track

| Attribute         | Type  |                    Example                     |
| :---------------- | :---: | :--------------------------------------------: |
| Track.id          |  Int  |                      266                       |
| Track.name        |  Str  | 'Autodromo Internazionale Enzo e Dino Ferrari' |
| Track.name_lower  |  Str  | 'autodromo internazionale enzo e dino ferrari' |
| Track.pkg_id      |  Int  |                      197                       |
| Track.priority    |  Int  |                       0                        |
| Track.race_week   |  Int  |                       8                        |
| Track.time_of_day |  Int  |                       1                        |
| Track.config      |  Str  |                  'Grand Prix'                  |

### CarClass

!!! Note "v0.1.0 Name Differences"
    In v0.1.0 the names are `custid`, `lowername`, and `shortname`.  
    In future releases they are updated to `cust_id`, `name_lower`, and `name_short`.

| Attribute  |      Type       |             Example             |
| :--------: | :-------------: | :-----------------------------: |
|    cars    | List of Objects | See [CarClassCar](#carclasscar) |
|  cust_id   |       Int       |                0                |
|     id     |       Int       |               74                |
| name_lower |       Str       |      'mazda mx-5 cup 2016'      |
|    name    |       Str       |      'Mazda MX-5 Cup 2016'      |
| rel_speed  |       Int       |               33                |
| name_short |       Str       |         'MX5 Cup 2016'          |

#### CarClassCar

| Attribute | Type  |         Example         |
| :-------: | :---: | :---------------------: |
|    id     |  Int  |           67            |
|   name    |  Str  | 'Global Mazda MX-5 Cup' |
