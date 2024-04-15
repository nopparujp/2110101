import numpy as np


def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data


def report_lower_than_mean(weight, data):
    report = (', ').join(
        map(str, data[data[:, 1:]@weight < np.mean(data[:, 1:]@weight)][:, 0]))
    if len(report) == 0:
        print('None')
    else:
        print(report)


exec(input().strip())
# data[:, 1:] @ weight == np.average(data[:, 1:], axis=1, weights=weight)
# w, d = read_data()
# report_lower_than_mean(w, d)
