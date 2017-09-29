import numpy
import pandas
import statsmodels.api as sm

# GOAL: Get a 78%+ Accuracy. This gets 78.68%.
def simple_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']

        if (passenger['Sex'] == 'male') or (passenger['Pclass'] > 2) \
        or (passenger['Fare'] <= 10) or (passenger['Parch'] >= 4):
            predictions[passenger_id] = 0
        else:
            predictions[passenger_id] = 1
    return predictions
