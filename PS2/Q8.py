import pandas

def get_hourly_entries(df):
    df['ENTRIESn_hourly'] = df['ENTRIESn'].diff()
    # df['ENTRIESn_hourly'] = df['ENTRIESn'] - df['ENTRIESn'].shift()
    df['ENTRIESn_hourly'] = df['ENTRIESn_hourly'].fillna(1)
    return df