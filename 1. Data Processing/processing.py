import os
import pandas as pd
from functions import *

ROOT = "C:/Users/offco/Documents/Dev_Projects/JHUCovidDatasetAnP"
DIR = ROOT + "/COVID-19"
SAVE_DIR = ROOT + "/modified"
CONFIRMED_SAVE_DIR = SAVE_DIR + "/confirmed"
DEATHS_SAVE_DIR = SAVE_DIR + "/deaths"
COUNTRIES = ['China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Italy', 'Canada', 'Korea, South']
FIX_LIST = ['US', 'Hong Kong'] + COUNTRIES

CSSE_TS_DIR = DIR + "/csse_covid_19_data/csse_covid_19_time_series"
CSSE_TS_G = CSSE_TS_DIR + "/time_series_covid19_confirmed_global.csv"
CSSE_TS_US = CSSE_TS_DIR + "/time_series_covid19_confirmed_US.csv"
CSSE_TS_D_G = CSSE_TS_DIR + "/time_series_covid19_deaths_global.csv"
CSSE_TS_D_US = CSSE_TS_DIR + "/time_series_covid19_deaths_US.csv"

# INITIAL
confirmed_global = pd.read_csv(CSSE_TS_G)
confirmed_us = pd.read_csv(CSSE_TS_US)
deaths_global = pd.read_csv(CSSE_TS_D_G)
deaths_us = pd.read_csv(CSSE_TS_D_US)

confirmed_hk = confirmed_global[confirmed_global['Province/State'] == 'Hong Kong'].reset_index(drop=True)
deaths_hk = deaths_global[deaths_global['Province/State'] == 'Hong Kong'].reset_index(drop=True)

confirmed_global = fix_dataframe_one(confirmed_global)
confirmed_us = fix_dataframe_two(confirmed_us)
confirmed_hk = fix_dataframe_one(confirmed_hk)
deaths_hk = fix_dataframe_one(deaths_hk)
deaths_global = fix_dataframe_one(deaths_global)

# DATE INDEXING
deaths_us = deaths_us.drop(['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Lat', 'Long_'], axis=1).groupby(['Country_Region']).sum().transpose()
deaths_us.index.name = 'Date'
deaths_us.reset_index(inplace=True)
deaths_us = deaths_us[1:]
deaths_us.reset_index(inplace=True, drop=True)
deaths_us.head()
deaths_us['Date'] = deaths_us['Date'].apply(lambda x: datetime.strptime(x, '%m/%d/%y'))
deaths_us.set_index('Date', inplace=True)

# FIX ONE, TWO
confirmed_china = pd.DataFrame(confirmed_global[COUNTRIES[0]])
confirmed_japan = pd.DataFrame(confirmed_global[COUNTRIES[1]])
confirmed_germany = pd.DataFrame(confirmed_global[COUNTRIES[2]])
confirmed_uk = pd.DataFrame(confirmed_global[COUNTRIES[3]])
confirmed_india = pd.DataFrame(confirmed_global[COUNTRIES[4]])
confirmed_france = pd.DataFrame(confirmed_global[COUNTRIES[5]])
confirmed_italy = pd.DataFrame(confirmed_global[COUNTRIES[6]])
confirmed_canada = pd.DataFrame(confirmed_global[COUNTRIES[7]])
confirmed_skorea = pd.DataFrame(confirmed_global[COUNTRIES[8]])

deaths_china = pd.DataFrame(deaths_global[COUNTRIES[0]])
deaths_japan = pd.DataFrame(deaths_global[COUNTRIES[1]])
deaths_germany = pd.DataFrame(deaths_global[COUNTRIES[2]])
deaths_uk = pd.DataFrame(deaths_global[COUNTRIES[3]])
deaths_india = pd.DataFrame(deaths_global[COUNTRIES[4]])
deaths_france = pd.DataFrame(deaths_global[COUNTRIES[5]])
deaths_italy = pd.DataFrame(deaths_global[COUNTRIES[6]])
deaths_canada = pd.DataFrame(deaths_global[COUNTRIES[7]])
deaths_skorea = pd.DataFrame(deaths_global[COUNTRIES[8]])

# FIX THREE
confirmed_us = final_fix(confirmed_us)
deaths_us = final_fix(deaths_us)

confirmed_hk = final_fix(confirmed_hk)
deaths_hk = final_fix(deaths_hk)

# EXPORT AS .CSV
try:
    os.mkdir(SAVE_DIR)
    os.mkdir(CONFIRMED_SAVE_DIR)
    os.mkdir(DEATHS_SAVE_DIR)
except FileExistsError:
    pass

confirmed_us.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[0].lower()}.csv")
deaths_us.to_csv(DEATHS_SAVE_DIR + f"/deaths_{FIX_LIST[0].lower()}.csv")

confirmed_hk.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[1].lower()}.csv")
deaths_hk.to_csv(DEATHS_SAVE_DIR + f"/deaths_{FIX_LIST[1].lower()}.csv")

confirmed_china.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[2].lower()}.csv")
deaths_china.to_csv(DEATHS_SAVE_DIR + f"/deaths_{FIX_LIST[2].lower()}.csv")

confirmed_japan.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[3].lower()}.csv")
deaths_japan.to_csv(DEATHS_SAVE_DIR + f"/confirmed_{FIX_LIST[3].lower()}.csv")

confirmed_germany.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[4].lower()}.csv")
deaths_germany.to_csv(DEATHS_SAVE_DIR + f"/deaths_{FIX_LIST[4].lower()}.csv")

confirmed_uk.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[5].lower()}.csv")
deaths_uk.to_csv(DEATHS_SAVE_DIR + f"/deaths_{FIX_LIST[5].lower()}.csv")

confirmed_india.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[6].lower()}.csv")
deaths_india.to_csv(DEATHS_SAVE_DIR + f"/deaths_{FIX_LIST[6].lower()}.csv")

confirmed_france.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[7].lower()}.csv")
deaths_france.to_csv(DEATHS_SAVE_DIR + f"/deaths_{FIX_LIST[7].lower()}.csv")

confirmed_italy.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[8].lower()}.csv")
deaths_italy.to_csv(DEATHS_SAVE_DIR + f"/deaths_{FIX_LIST[8].lower()}.csv")

confirmed_canada.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[9].lower()}.csv")
deaths_canada.to_csv(DEATHS_SAVE_DIR + f"/deaths_{FIX_LIST[9].lower()}.csv")

confirmed_skorea.to_csv(CONFIRMED_SAVE_DIR + f"/confirmed_{FIX_LIST[10].lower()}.csv")
deaths_skorea.to_csv(DEATHS_SAVE_DIR + f"/deaths_{FIX_LIST[10].lower()}.csv")