# _*_ coding: utf_8 _*_
import time
import math
import os

ALL = -1
# Entries per page. This is the ammount set
# in iRacing site. We shouldn't increase it.
NUM_ENTRIES = 25

# Minimum time in seconds between two consecutive requests to iRacing site
# (we don't want to flood/abuse the service).
# I'm not sure about the minimum value for this, I'll have to ask a dev.
WAIT_TIME = 0.3

IRATING_OVAL_CHART = 1
IRATING_ROAD_CHART = 2

RACE_TYPE_OVAL = 1
RACE_TYPE_ROAD = 2

LIC_ROOKIE = 1
LIC_D = 2
LIC_C = 3
LIC_B = 4
LIC_A = 5
LIC_PRO = 6
LIC_PRO_WC = 7

SORT_IRATING = 'irating'
SORT_TIME = 'start_time'
SORT_POINTS = 'points'
ORDER_DESC = 'desc'
ORDER_ASC = 'asc'

# List of session eventType
EVENT_TEST = 1
EVENT_PRACTICE = 2
EVENT_QUALY = 3
EVENT_TTRIAL = 4
EVENT_RACE = 5
EVENT_OFFICIAL = 6
EVENT_UNOFFICIAL = 7

# INCIDENT FLAGS
# These are used in the laps data
FLAG_PITTED = 2
FLAG_OFF_TRACK = 4
FLAG_BLACK_FLAG = 8
FLAG_CAR_RESET = 16
FLAG_CONTACT = 32
FLAG_CAR_CONTACT = 64
FLAG_LOST_CONTROL = 128
FLAG_DISCONTINUITY = 256
FLAG_INTERPOLATED_CROSSING = 512
FLAG_CLOCK_SMASH = 1024
FLAG_TOW = 2048

INC_FLAGS = {
    0: "clean",
    2: "pitted",
    4: "off track",
    8: "black flag",
    16: "car reset",
    32: "contact",
    64: "car contact",
    128: "lost control",
    256: "discontinuity",
    512: "interpolated crossing",
    1024: "clock smash",
    2048: "tow"
}

custid = 435144

# iRacing rounds down to the 5 minute mark - DO NOT CHANGE
now_unix_ms = int(math.floor(time.time()/300)*300)*1000

# Context sites for the 2 types of endpoints
mSite = 'https://members.iracing.com/membersite/member'
mStats = 'https://members.iracing.com/memberstats/member'

# IRACING SERVICE URLS
URL_LOGIN = 'https://members.iracing.com/membersite/login.jsp'
URL_LOGIN2 = 'https://members.iracing.com/membersite/Login'
URL_LOGOUT = 'https://members.iracing.com/membersite/LogOut'
URL_HOME = 'https://members.iracing.com/membersite/member/Home.do'

# THE BIG ONES
URL_SUBS_RESULTS = (mSite + '/GetSubsessionResults')
URL_CURRENT_SEASONS = (mSite + '/GetSeasons')

URL_SEASON_STANDINGS = (mStats + '/GetSeasonStandings')
URL_SERIES_RACERESULTS = (mStats + '/GetSeriesRaceResults')


# RECENT HISTORICAL
URL_LASTRACE_STATS = (mStats + '/GetLastRacesStats')
URL_LAST_SERIES = (mStats + '/GetLastSeries')
URL_RESULTS = (mStats + '/GetResults?'
                                f'custid={custid}'  # custid required
                                '&showraces=1'
                                '&showquals=0'
                                '&showtts=0'
                                '&showops=0'
                                '&showofficial=1'
                                '&showunofficial=0'
                                '&showrookie=1'
                                '&showclassd=1'
                                '&showclassc=1'
                                '&showclassb=1'
                                '&showclassa=1'
                                '&showpro=1'
                                '&showprowc=1'
                                '&lowerbound=0'
                                f'&upperbound={NUM_ENTRIES}'
                                '&sort=start_time'
                                '&order=desc'
                                '&format=json'
                                '&category%5B%5D=1'
                                '&category%5B%5D=2'
                                '&category%5B%5D=3'
                                '&category%5B%5D=4'
                                f'&seasonyear={year}'
                                f'&seasonquarter={quarter}'
                                f'&raceweek={raceweek}'
                                f'&trackid={trackid}'
                                f'&carclassid={carclass}'
                                f'&carid={carid}')
URL_WORLD_RECORDS = (mStats + '/GetWorldRecords')


# UPCOMING SESSIONS
URL_SESSION_TIMES = (mSite + '/GetSessionTimes')
URL_NEXT_EVENT = (mSite + '/GetNextEvent')
URL_TOTALREGISTERED = (mSite + '/GetTotalSessionJoinedCountsBySeason')
URL_RACEGUIDE = (mSite + '/GetRaceGuide?'
                             f'at={now_unix_ms}'
                             '&showRookie=1'
                             '&showClassD=1'
                             '&showClassC=1'
                             '&showClassB=1'
                             '&showClassA=1'
                             '&showPro=1'
                             '&showProWC=1'
                             '&showOval=1'
                             '&showRoad=1'
                             '&showDirtOval=1'
                             '&showDirtRoad=1'
                             '&hideNotFixedSetup=0'
                             '&hideNotMultiClass=0'
                             '&meetsMPR=0'
                             '&hideUnpopulated=0'
                             '&hideIneligible=0'
                             '&showOfficial=1')
URL_ACTIVEOP_COUNT = (mSite + '/GetActiveOpenPracticeCount')


# DRIVER PROFILE STATS
URL_STATS_CHART = (mStats + '/GetChartData')
URL_CAREER_STATS = (mStats + '/GetCareerStats')
URL_YEARLY_STATS = (mStats + '/GetYearlyStats')
URL_PERSONAL_BESTS = (mStats + '/GetPersonalBests')


# RACE SPECIFIC RESULTS
URL_LAPS_SINGLE = (mSite + '/GetLaps')
URL_LAPS_ALL = (mSite + '/GetLapChart')


# UTILITY ?
URL_DRIVER_STATS = (mStats + '/GetDriverStats?'
                             'search=null'
                             '&friend=-1'
                             '&watched=-1'
                             '&recent=-1'
                             '&country=null'
                             '&category=1'
                             '&classlow=-1'
                             '&classhigh=-1'
                             '&iratinglow=-1'
                             '&iratinghigh=-1'
                             '&ttratinglow=-1'
                             '&ttratinghigh=-1'
                             '&avgstartlow=-1'
                             '&avgstarthigh=-1'
                             '&avgfinishlow=-1'
                             '&avgfinishhigh=-1'
                             '&avgpointslow=-1'
                             '&avgpointshigh=-1'
                             '&avgincidentslow=-1'
                             '&avgincidentshigh=-1'
                             '&custid=435144'
                             '&lowerbound=1'
                             '&upperbound=25'
                             '&sort=irating'
                             '&order=desc'
                             '&active=1')
URL_MEM_SUBSESSID = (mSite + '/GetSubsessionForMember')
URL_CARS_DRIVEN = (mStats + '/GetCarsDriven')
URL_HOSTED_RESULTS = (mStats + '/GetPrivateSessionResults')



# ESSENTIALLY USELESS URLS

# Driver Status is the
URL_MY_RACERS = (mSite + '/GetDriverStatus')
URL_MY_RACER_COUNTS = (mSite + '/GetDriverCounts')
URL_MEM_DIVISION = (mSite + '/GetMembersDivision')


# THESE URLS DO NOT RETURN JSON
# THESE URLS DO NOT RETURN JSON
# THESE URLS DO NOT RETURN JSON

URL_EVENT_RESULT = (mSite + '/EventResult.do?'
                                f'subsessionid={subsession}')
URL_EVENT_RESULTS_CSV = (mSite + '/GetEventResultsAsCSV?'
                                    f'subsessionid={subsession}'
                                    f'&simsesnum={sessnum}'
                                    '&includeSummary=1')
URL_CURRENT_SERIES = (mSite + '/Series.do')
URL_SELECT_SERIES = (mSite + '/SelectSeries.do?'
                             f'season={seasonID}'
                             '&view=undefined'
                             '&nocache=%s')
URL_SEASON_STANDINGS2 = (mSite + '/statsseries.jsp')

# Doesn't work. Loads a page but redirects back to home
URL_GET_PASTSERIES = (mSite + '/PreviousSeasons.do')


# LOCATIONS (AKA Country Code)
countryCodes = {
    'ALL': 'null',
    'AFGHANISTAN': 'AF',
    'ALAND_ISLANDS': 'AX',
    'ALBANIA': 'AL',
    'ALGERIA': 'DZ',
    'AMERICAN_SAMOA': 'AS',
    'ANDORRA': 'AD',
    'ANGOLA': 'AO',
    'ANGUILLA': 'AI',
    'ANTARCTICA': 'AQ',
    'ANTIGUA_AND_BARBUDA': 'AG',
    'ARGENTINA': 'AR',
    'ARMENIA': 'AM',
    'ARUBA': 'AW',
    'AUSTRALIA': 'AU',
    'AUSTRIA': 'AT',
    'AZERBAIJAN': 'AZ',
    'BAHAMAS': 'BS',
    'BAHRAIN': 'BH',
    'BANGLADESH': 'BD',
    'BARBADOS': 'BB',
    'BELARUS': 'BY',
    'BELGIUM': 'BE',
    'BELIZE': 'BZ',
    'BENIN': 'BJ',
    'BERMUDA': 'BM',
    'BHUTAN': 'BT',
    'BOLIVIA_PLURINATIONAL_STATE_OF': 'BO',
    'BOSNIA_AND_HERZEGOVINA': 'BA',
    'BOTSWANA': 'BW',
    'BOUVET_ISLAND': 'BV',
    'BRAZIL': 'BR',
    'BRITISH_INDIAN_OCEAN_TERRITORY': 'IO',
    'BRUNEI_DARUSSALAM': 'BN',
    'BULGARIA': 'BG',
    'BURKINA_FASO': 'BF',
    'BURUNDI': 'BI',
    'CAMBODIA': 'KH',
    'CAMEROON': 'CM',
    'CANADA': 'CA',
    'CAPE_VERDE': 'CV',
    'CAYMAN_ISLANDS': 'KY',
    'CENTRAL_AFRICAN_REPUBLIC': 'CF',
    'CHAD': 'TD',
    'CHILE': 'CL',
    'CHINA': 'CN',
    'CHRISTMAS_ISLAND': 'CX',
    'COCOS_KEELING_ISLANDS': 'CC',
    'COLOMBIA': 'CO',
    'COMOROS': 'KM',
    'CONGO': 'CG',
    'CONGO_THE_DEMOCRATIC_REPUBLIC_OF_THE': 'CD',
    'COOK_ISLANDS': 'CK',
    'COSTA_RICA': 'CR',
    'COTE_DIVOIRE': 'CI',
    'CROATIA': 'HR',
    'CUBA': 'CU',
    'CYPRUS': 'CY',
    'CZECH_REPUBLIC': 'CZ',
    'DENMARK': 'DK',
    'DJIBOUTI': 'DJ',
    'DOMINICA': 'DM',
    'DOMINICAN_REPUBLIC': 'DO',
    'ECUADOR': 'EC',
    'EGYPT': 'EG',
    'EL_SALVADOR': 'SV',
    'EQUATORIAL_GUINEA': 'GQ',
    'ERITREA': 'ER',
    'ESTONIA': 'EE',
    'ETHIOPIA': 'ET',
    'FALKLAND_ISLANDS_MALVINAS': 'FK',
    'FAROE_ISLANDS': 'FO',
    'FIJI': 'FJ',
    'FINLAND': 'FI',
    'FRANCE': 'FR',
    'FRENCH_GUIANA': 'GF',
    'FRENCH_POLYNESIA': 'PF',
    'FRENCH_SOUTHERN_TERRITORIES': 'TF',
    'GABON': 'GA',
    'GAMBIA': 'GM',
    'GEORGIA': 'GE',
    'GERMANY': 'DE',
    'GHANA': 'GH',
    'GIBRALTAR': 'GI',
    'GREECE': 'GR',
    'GREENLAND': 'GL',
    'GRENADA': 'GD',
    'GUADELOUPE': 'GP',
    'GUAM': 'GU',
    'GUATEMALA': 'GT',
    'GUERNSEY': 'GG',
    'GUINEA': 'GN',
    'GUINEA_BISSAU': 'GW',
    'GUYANA': 'GY',
    'HAITI': 'HT',
    'HEARD_ISLAND_AND_MCDONALD_ISLANDS': 'HM',
    'HOLY_SEE_VATICAN_CITY_STATE': 'VA',
    'HONDURAS': 'HN',
    'HONG_KONG': 'HK',
    'HUNGARY': 'HU',
    'ICELAND': 'IS',
    'INDIA': 'IN',
    'INDONESIA': 'ID',
    'IRAN_ISLAMIC_REPUBLIC_OF': 'IR',
    'IRAQ': 'IQ',
    'IRELAND': 'IE',
    'ISLE_OF_MAN': 'IM',
    'ISRAEL': 'IL',
    'ITALY': 'IT',
    'JAMAICA': 'JM',
    'JAPAN': 'JP',
    'JERSEY': 'JE',
    'JORDAN': 'JO',
    'KAZAKHSTAN': 'KZ',
    'KENYA': 'KE',
    'KIRIBATI': 'KI',
    'KOREA_DEMOCRATIC_PEOPLES_REPUBLIC_OF': 'KP',
    'KOREA_REPUBLIC_OF': 'KR',
    'KUWAIT': 'KW',
    'KYRGYZSTAN': 'KG',
    'LAO_PEOPLES_DEMOCRATIC_REPUBLIC': 'LA',
    'LATVIA': 'LV',
    'LEBANON': 'LB',
    'LESOTHO': 'LS',
    'LIBERIA': 'LR',
    'LIBYAN_ARAB_JAMAHIRIYA': 'LY',
    'LIECHTENSTEIN': 'LI',
    'LITHUANIA': 'LT',
    'LUXEMBOURG': 'LU',
    'MACAO': 'MO',
    'MACEDONIA_THE_FORMER_YUGOSLAV_REPUBLIC_OF': 'MK',
    'MADAGASCAR': 'MG',
    'MALAWI': 'MW',
    'MALAYSIA': 'MY',
    'MALDIVES': 'MV',
    'MALI': 'ML',
    'MALTA': 'MT',
    'MARSHALL_ISLANDS': 'MH',
    'MARTINIQUE': 'MQ',
    'MAURITANIA': 'MR',
    'MAURITIUS': 'MU',
    'MAYOTTE': 'YT',
    'MEXICO': 'MX',
    'MICRONESIA_FEDERATED_STATES_OF': 'FM',
    'MOLDOVA_REPUBLIC_OF': 'MD',
    'MONACO': 'MC',
    'MONGOLIA': 'MN',
    'MONTENEGRO': 'ME',
    'MONTSERRAT': 'MS',
    'MOROCCO': 'MA',
    'MOZAMBIQUE': 'MZ',
    'MYANMAR': 'MM',
    'NAMIBIA': 'NA',
    'NAURU': 'NR',
    'NEPAL': 'NP',
    'NETHERLANDS': 'NL',
    'NETHERLANDS_ANTILLES': 'AN',
    'NEW_CALEDONIA': 'NC',
    'NEW_ZEALAND': 'NZ',
    'NICARAGUA': 'NI',
    'NIGER': 'NE',
    'NIGERIA': 'NG',
    'NIUE': 'NU',
    'NORFOLK_ISLAND': 'NF',
    'NORTHERN_MARIANA_ISLANDS': 'MP',
    'NORWAY': 'NO',
    'OMAN': 'OM',
    'PAKISTAN': 'PK',
    'PALAU': 'PW',
    'PALESTINIAN_TERRITORY_OCCUPIED': 'PS',
    'PANAMA': 'PA',
    'PAPUA_NEW_GUINEA': 'PG',
    'PARAGUAY': 'PY',
    'PERU': 'PE',
    'PHILIPPINES': 'PH',
    'PITCAIRN': 'PN',
    'POLAND': 'PL',
    'PORTUGAL': 'PT',
    'PUERTO_RICO': 'PR',
    'QATAR': 'QA',
    'REUNION': 'RE',
    'ROMANIA': 'RO',
    'RUSSIAN_FEDERATION': 'RU',
    'RWANDA': 'RW',
    'SAINT_BARTHELEMY': 'BL',
    'SAINT_HELENA_ASCENSION_AND_TRISTAN_DA_CUNHA': 'SH',
    'SAINT_KITTS_AND_NEVIS': 'KN',
    'SAINT_LUCIA': 'LC',
    'SAINT_MARTIN_FRENCH_PART': 'MF',
    'SAINT_PIERRE_AND_MIQUELON': 'PM',
    'SAINT_VINCENT_AND_THE_GRENADINES': 'VC',
    'SAMOA': 'WS',
    'SAN_MARINO': 'SM',
    'SAO_TOME_AND_PRINCIPE': 'ST',
    'SAUDI_ARABIA': 'SA',
    'SENEGAL': 'SN',
    'SERBIA': 'RS',
    'SEYCHELLES': 'SC',
    'SIERRA_LEONE': 'SL',
    'SINGAPORE': 'SG',
    'SLOVAKIA': 'SK',
    'SLOVENIA': 'SI',
    'SOLOMON_ISLANDS': 'SB',
    'SOMALIA': 'SO',
    'SOUTH_AFRICA': 'ZA',
    'SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS': 'GS',
    'SPAIN': 'ES',
    'SRI_LANKA': 'LK',
    'SUDAN': 'SD',
    'SURINAME': 'SR',
    'SVALBARD_AND_JAN_MAYEN': 'SJ',
    'SWAZILAND': 'SZ',
    'SWEDEN': 'SE',
    'SWITZERLAND': 'CH',
    'SYRIAN_ARAB_REPUBLIC': 'SY',
    'TAIWAN_PROVINCE_OF_CHINA': 'TW',
    'TAJIKISTAN': 'TJ',
    'TANZANIA_UNITED_REPUBLIC_OF': 'TZ',
    'THAILAND': 'TH',
    'TIMOR_LESTE': 'TL',
    'TOGO': 'TG',
    'TOKELAU': 'TK',
    'TONGA': 'TO',
    'TRINIDAD_AND_TOBAGO': 'TT',
    'TUNISIA': 'TN',
    'TURKEY': 'TR',
    'TURKMENISTAN': 'TM',
    'TURKS_AND_CAICOS_ISLANDS': 'TC',
    'TUVALU': 'TV',
    'UGANDA': 'UG',
    'UKRAINE': 'UA',
    'UNITED_ARAB_EMIRATES': 'AE',
    'UNITED_KINGDOM': 'GB',
    'UNITED_STATES': 'US',
    'UNITED_STATES_MINOR_OUTLYING_ISLANDS': 'UM',
    'URUGUAY': 'UY',
    'UZBEKISTAN': 'UZ',
    'VANUATU': 'VU',
    'VENEZUELA_BOLIVARIAN_REPUBLIC_OF': 'VE',
    'VIET_NAM': 'VN',
    'VIRGIN_ISLANDS_BRITISH': 'VG',
    'VIRGIN_ISLANDS_US': 'VI',
    'WALLIS_AND_FUTUNA': 'WF',
    'WESTERN_SAHARA': 'EH',
    'YEMEN': 'YE',
    'ZAMBIA': 'ZM',
    'ZIMBABWE': 'ZW'
}

# List of SIDs (SeriesID) listed in order from /GetRaceGuide
# Note: removed any dashs due to errors
SID_Carburetor_Cup = 116
SID_DIRTcar_Street_Stock_Series_Fixed = 290
SID_Fanatec_Global_Mazda_MX5_Cup = 139
SID_Fanatec_Street_Stock_Series_R = 182
SID_iRacing_Advanced_Legends_Cup = 32
SID_iRacing_Dirt_Legends_Cup = 315
SID_PickUp_Cup = 259
SID_Pro_2_Lite_Truck_Championship = 387
SID_Rookie_iRacing_Rallycross_Series = 326
SID_Sling_Mud_for_Fun_Sprint_Cars = 303
SID_Trak_Racer_Dallara_Dash = 258
SID_BMW_120_Challenge_Fixed = 397
SID_BMW_SIM_120_Cup = 400
SID_DIRTcar_Limited_Late_Model_Series = 291
SID_Fanatec_DIRTcar_305_Sprint_Car_Series = 292
SID_Fanatec_Global_Challenge = 210
SID_iRacing_ARCA_Menards_Series = 167
SID_iRacing_Formula_Renault_20 = 269
SID_iRacing_Late_Model_Tour = 33
SID_iRacing_Rallycross_Series = 325
SID_iRacing_Spec_Racer_Ford_Challenge = 63
SID_Lucas_Oil_Off_Road_Racing_Pro_4_Series = 391
SID_NASCAR_SK_Modified_Weekly_Series = 45
SID_Nurburgring_Endurance_Championship = 275
SID_Pure_Driving_School_Formula_Sprint = 384
SID_Ruf_GT3_Challenge = 277
SID_SimLab_Production_Car_Challenge = 112
SID_Skip_Barber_Race_Series = 34
SID_Advanced_Mazda_MX5_Cup_Series = 231
SID_DIRTcar_360_Sprint_Car_Series_ = 305
SID_DIRTcar_Class_C_Street_Stock_Series_Fixed = 311
SID_DIRTcar_Pro_Late_Model_Series_ = 306
SID_Fanatec_GT_Challenge = 278
SID_Grand_Prix_Legends = 201
SID_IMSA_Michelin_Pilot_Challenge = 386
SID_IMSA_Sportscar_Championship = 227
SID_Indy_Pro_2000_Championship = 414
SID_IndyCar_iRacing_Series = 374
SID_IndyCar_Series_Oval_Fixed = 165
SID_iRacing_Dirt_Midget_Cup = 327
SID_iRacing_Endurance_Series = 408
SID_iRacing_F3_Championship = 358
SID_iRacing_Street_Stock_Series_C = 190
SID_iRacing_Super_Late_Model_Series = 223
SID_iRacing_Super_Late_Model_Series_Fixed = 416
SID_Kamel_GT_Championship_ = 285
SID_Lucas_Oil_Off_Road_Racing_Pro_2_Series = 378
SID_NASCAR_iRacing_Class_C = 47
SID_NASCAR_iRacing_Class_C_Fixed = 164
SID_NASCAR_iRacing_Series_Fixed = 207
SID_NASCAR_iRacing_Series_Open = 229
SID_NASCAR_iRacing_Tour_Modified_Series = 102
SID_NASCAR_iRacing_Tour_Modified_Series_Fixed = 417
SID_NASCAR_Legends_Series = 413
SID_Porsche_Esports_Sprint_Challenge = 410
SID_Porsche_iRacing_Cup = 299
SID_Radical_Racing_Challenge_C = 74
SID_Supercars_Series = 399
SID_Supercars_Series_Australian_Server_Only = 405
SID_USAC_360_Sprint_Car_Series = 310
SID_VRS_GT_Endurance_Series = 237
SID_World_of_Outlaws_Late_Model_Series_Fixed = 369
SID_AMSOIL_USAC_Sprint_Car = 309
SID_Classic_Lotus_Grand_Prix = 65
SID_DIRTcar_UMP_Modified_Series = 316
SID_IndyCar_Series_Road = 133
SID_iRacing_Endurance_Le_Mans_Series = 331
SID_iRacing_Formula_35_Championship = 359
SID_iRacing_Le_Mans_Series = 330
SID_iRacing_Silver_Crown_Cup = 53
SID_iRacing_Sprint_Car_Cup = 131
SID_NASCAR_iRacing_Class_B = 62
SID_NASCAR_iRacing_Class_B_Fixed = 103
SID_VRS_GT_Sprint_Series = 228
SID_World_of_Outlaws_Late_Model_Series_ = 308
SID_World_of_Outlaws_Sprint_Car_Series = 307
SID_iRacing_Grand_Prix_Series = 260
SID_NASCAR_iRacing_Class_A = 58
SID_NASCAR_iRacing_Class_A_Fixed_ = 191
SID_NASCAR_Road_to_Pro = 328
SID_Porsche_TAG_Heuer_Esports_Supercup = 409
SID_WoO_Late_Model_WC_Series = 339
SID_eNASCAR_CocaCola_Series = 402
