import csv

def load():
    res = []
    with open('Pokemon.csv', 'rt') as f:
        r = csv.reader(f)
        next(r, None)
        for row in r:
            res.append(row)

    return res


def max_total(r):
    m = 0
    for row in r:
        if m < int(row[4]):
            m = int(row[4])
    return m

print(max_total(load()))