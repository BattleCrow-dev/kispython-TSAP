# 1-е по популярности
# from math import log10
#
#
# def main(x):
#     ans = 0
#     n = len(x)
#     for i in range(1, n + 1):
#         ans += 38 * log10(11 * x[n + 1 - i - 1] ** 3 + x[i - 1] ** 2)
#     return ans

# 2-е по популярности
# from math import log10
#
#
# def main(x):
#     return sum([38 * log10(11 * x[len(x) + 1 - i - 1] ** 3 + x[i - 1] ** 2)
#                 for i in range(1, len(x) + 1)])

# 3-е по популярности
# from math import log10
#
#
# def main(x):
#     n = len(x)
#     ans = 0
#     i = 1
#     while i < n + 1:
#         ans += 38 * log10(11 * x[n + 1 - i - 1] ** 3 + x[i - 1] ** 2)
#         i += 1
#     return ans

# 4-е по популярности
# from math import log10
#
#
# def main(x, i=0):
#     if i == len(x):
#         return 0
#     else:
#         return (38 * log10(11 * x[len(x) - i - 1] ** 3 + x[i] ** 2)
#                 + main(x, i + 1))


# def test():
#     print(main([0.41, 0.0, 0.28, 0.98, 0.5]))
#     print(main([0.46, 0.74, 0.08, 0.18, -0.24]))
#     print(main([0.71, 0.12, 0.7, 0.98, 0.35]))
#     print(main([-0.21, 0.69, 0.57, 0.29, 0.61]))
#     print(main([0.93, 0.97, 0.96, -0.28, 0.52]))


# test()
