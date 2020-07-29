# current_seasons
Data points returned from `Client.current_seasons()`

## Season

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
### SeasonCar

| Attribute  | Type  |         Example         |
| :--------: | :---: | :---------------------: |
|     id     |  int  |           67            |
|    name    |  str  | 'Global+Mazda+MX-5+Cup' |
| name_lower |  str  | 'global mazda mx-5 cup' |
|   pkg_id   |  int  |           182           |
|    sku     |  int  |          10394          |

### Track

|  Attribute  | Type  |        Example         |
| :---------: | :---: | :--------------------: |
|    name     |  str  | 'Brands Hatch Circuit' |
| name_lower  |  str  | 'brands hatch circuit' |
|   pkg_id    |  int  |           91           |
|  priority   |  int  |           1            |
|  race_week  |  int  |           7            |
| time_of_day |  int  |           2            |
|   config    |  str  |      'Grand Prix'      |

### SeasonCarClass

!!! Note "v0.1.0 Name Differences"
    In v0.1.0 the names are `custid`, `lowername`, and `shortname`.  
    In future releases they are updated to `cust_id`, `name_lower`, and `name_short`.

|     Attribute     | Type  |        Example        |
| :---------------: | :---: | :-------------------: |
|      custid       |  int  |           0           |
|        id         |  int  |          74           |
|     lowername     |  str  | 'mazda+mx-5+cup+2016' |
|       name        |  str  | 'Mazda MX-5 Cup 2016' |
|     rel_speed     |  int  |          33           |
|     shortname     |  str  |    'MX5 Cup 2016'     |
|       cars        | list  |    See [Car](#car)    |
| tire_sets_dry_max |  int  |           0           |

#### Car

| Attribute | Type  |         Example         |
| :-------: | :---: | :---------------------: |
|    id     |  int  |           67            |
|   name    |  str  | 'Global Mazda MX-5 Cup' |
