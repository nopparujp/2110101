import numpy as np
import math


def p(X):
    return 1 / (1 + math.e ** -(-3.98 + 0.1 * X[:, 0] + 0.5 * X[:, 1]))


exec(input().strip())
# print(p(np.array([[100, 4.00]])))
# print(p(np.array([[80, 2.50], [1, 4.00]])))
