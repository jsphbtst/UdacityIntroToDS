import pandas
import pandasql

def num_rainy_days(filename):
    weather_data = pandas.read_csv(filename)

    q = """
    select sum(rain) from weather_data where rain=1
    """
    
    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days
