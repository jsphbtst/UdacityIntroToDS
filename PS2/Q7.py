import pandas

def filter_by_regular(filename):
    turnstile_data = pandas.read_csv(filename)
    turnstile_data = turnstile_data[turnstile_data['DESCn'] == 'REGULAR']
    print turnstile_data
    return turnstile_data