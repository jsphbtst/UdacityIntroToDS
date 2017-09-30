from datetime import datetime

def reformat_subway_dates(date):
    year = '20' + date[6:len(date)]
    month = date[0:2]
    day = date[3:5]
    date_formatted = year + '-' + month + '-' + day
    return date_formatted
