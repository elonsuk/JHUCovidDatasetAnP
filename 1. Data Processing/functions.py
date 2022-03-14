from datetime import datetime

def fix_dataframe_one(df):
    df = df.drop(['Lat', 'Long'], axis=1).groupby(['Country/Region']).sum().transpose()
    df.index.name = 'Date'
    df.reset_index(inplace=True)
    df['Date'] = df['Date'].apply(lambda x: datetime.strptime(x, '%m/%d/%y'))
    df.set_index('Date', inplace=True)
    return df

def fix_dataframe_two(df):
    df = df.drop(['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Lat', 'Long_'], axis=1).groupby(['Country_Region']).sum().transpose()
    df.index.name = 'Date'
    df.reset_index(inplace=True)
    df['Date'] = df['Date'].apply(lambda x: datetime.strptime(x, '%m/%d/%y'))
    df.set_index('Date', inplace=True)
    return df

def final_fix(df):
    df.rename(columns={df.columns[0]: 'cases'}, inplace=True)
    df.rename_axis('', axis='columns', inplace=True)
    return df