import numpy
import pandas
import statsmodels.api as sm

# GOAL: Get a 80%+ Accuracy. This gets 80.58%.
def custom_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
            
        if (passenger['Sex'] == 'male') \
        or (passenger['Pclass'] > 1 and passenger['Fare'] < 10 \
        and passenger['Age'] > 19) or (passenger['SibSp'] > 2) \
        or (passenger['Parch'] > 2):
            predictions[passenger_id] = 0
        else:
            predictions[passenger_id] = 1
    return predictions
