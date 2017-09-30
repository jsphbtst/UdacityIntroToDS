import pandas
import pandasql

def avg_weekend_temperature(filename):
    weather_data = pandas.read_csv(filename)

    q = """
    select 
    avg(cast(meantempi as integer)) 
    from 
    weather_data 
    where 
    cast(strftime('%w',date) as integer)=0 or cast(strftime('%w',date) as integer)=6
    """
    
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    return mean_temp_weekends