import pandas

def get_hourly_exits(df):
    df['EXITSn_hourly'] = df['EXITSn'].diff()
    # df['EXITSn_hourly'] = df['EXITSn_hourly'] - df['EXITSn_hourly'].shift()
    df['EXITSn_hourly'] = df['EXITSn_hourly'].fillna(0)
    return df
