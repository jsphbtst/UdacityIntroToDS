import numpy
import pandas
import statsmodels.api as sm

# GOAL: Get a 79%+ Accuracy. This gets 79.01%.
def complex_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        
        if (passenger['Sex'] == 'female') or (passenger['Pclass'] == 1 and passenger['Age'] <= 18):
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
    return predictions
