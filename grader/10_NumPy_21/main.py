import numpy as np


def sum_2_rows(M):
    return M[::2] + M[1::2]


def sum_left_right(M):
    return M[:, :len(M)//2:] + M[:, len(M)//2::]


def sum_upper_lower(M):
    return M[:len(M)//2] + M[len(M)//2:]


def sum_4_quadrants(M):
    return M[:len(M)//2:, :len(M)//2:] + M[:len(M)//2:, len(M)//2::] + M[len(M)//2::, :len(M)//2:] + M[len(M)//2::, len(M)//2::]


def sum_4_cells(M):
    return M[0::2, 0::2] + M[0::2, 1::2] + M[1::2, 0::2] + M[1::2, 1::2]


def count_leap_years(years):
    return np.sum(((years-543) % 4 == 0) & (((years-543) % 100 != 0) | ((years-543) % 400 == 0)))


exec(input().strip())
# print(sum_2_rows(np.arange(36).reshape(6, 6)))
# print(sum_left_right(np.arange(36).reshape(6, 6)))
# print(sum_upper_lower(np.arange(36).reshape(6, 6)))
# print(sum_4_quadrants(np.arange(36).reshape(6, 6)))
# print(sum_4_cells(np.arange(36).reshape(6, 6)))
# print(count_leap_years(np.array([2543, 2559, 2560])))
