import csv

def fix_turnstile_data(filenames):
    for name in filenames:
        with open(name) as f:
            reader = csv.reader(f)
            with open('updated_'+name, 'wb') as g:
                writer = csv.writer(g)
                for row in reader:
                    max_len = len(row)
                    tail_start = 3
                    i = 0
                    while i < round((max_len-3)/5.):
                        writer.writerow(row[:3]+row[tail_start:tail_start+5])
                        tail_start = tail_start + 5
                        i = i + 1