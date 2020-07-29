# current_seasons
Data points returned from `Client.current_seasons()`

## Season

|     Attributes      |      Type       |            Example            |
| :-----------------: | :-------------: | :---------------------------: |
|       active        |     Boolean     |
|       cat_id        |       Int       |
|      category       |       Str       |
|      date_end       |       Int       |
|     date_start      |       Int       |
|       is_lite       |     Boolean     |
|  license_eligible   |     Boolean     |
|      race_week      |       Int       |
|      season_id      |       Int       |
|   season_quarter    |       Int       |
|     season_year     |       Int       |
|      series_id      |       Int       |
| series_lic_group_id |       Int       |
|  series_name_short  |       Str       |
|        cars         | List of Objects | See [Car Object](#car-object) |
|       tracks        | List of Objects |  See [Track Object](#track)   |

### Car
| Attribute  | Type  | Example |
| :--------: | :---: | :-----: |
|     id     |  Int  |
|    name    |  Str  |
| name_lower |  Str  |
|   pkg_id   |  Int  |
|    sku     |  Int  |

### Track
|  Attribute  | Type  | Example |
| :---------: | :---: | :-----: |
|    name     |  Str  |
| name_lower  |  Str  |
|   pkg_id    |  Str  |
|  priority   |  Int  |
|  race_week  |  Int  |
| time_of_day |  Int  |
|   config    |  Str  |

### CarClass
| Attribute | Type  | Example |
| :-------: | :---: | :-----: |
|  custid   |  Int  |
|    id     |  Int  |
| lowername |  Str  |
|   name    |  Str  |
| rel_speed |  Int  |
| shortname |  Str  |

#### CarClassCar
| Attribute | Type  | Example |
| :-------: | :---: | :-----: |
|    id     |  Int  |
|   name    |  Str  |
