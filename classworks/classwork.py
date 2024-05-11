from math import *


def main_revised_v2(input_set):
    A = {l * l for l in input_set if -66 < l <= 95}

    I = {3 * l - ceil(l / 9) for l in input_set if -93 <= l or l < 44}

    M = A.union(I)

    sum_squares_I = sum(l ** 2 for l in I)

    sum_products_IM = sum(mu * i for i in I for mu in M)

    omega = sum_squares_I - sum_products_IM

    return omega


example_1_revised_v2 = main_revised_v2({33, 67, -59, 76, 45, -48, -75, -71, -37, 28})
example_2_revised_v2 = main_revised_v2({-56, 73, 41, 79, -16, 26, 59, -36, -67})

print(example_1_revised_v2, example_2_revised_v2)
