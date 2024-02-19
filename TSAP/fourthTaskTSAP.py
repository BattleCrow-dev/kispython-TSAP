# 1-е по популярности
# def main(n):
#     if n == 0:
#         return 0.15
#     elif n == 1:
#         return -0.52
#     return main(n - 1)**2 + 4 * main(n - 2)**3

# 2-е по популярности
# def main(n):
#     a, b = 0.15, -0.52
#     for i in range(2, n + 1):
#         a, b = b, b**2 + 4 * a**3
#     return b

# 3-е по популярности
# def main(n):
#     mas = [0.15, -0.52]
#
#     for i in range(2, n + 1):
#         mas.append(mas[i - 1]**2 + 4 * mas[i - 2]**3)
#
#     return mas[-1]

# 4-е по популярности
# def main(n):
#     match n:
#         case 0:
#             return 0.15
#         case 1:
#             return -0.52
#         case _:
#             return main(n - 1) ** 2 + 4 * main(n - 2) ** 3

# 5-е по популярности
# def main(n):
#     return 0.15 if n == 0 else -0.52 if n == 1 else (main(n - 1)**2 +
#                                                      4 * main(n - 2)**3)


# def test():
#     print(main(4))
#     print(main(6))
#     print(main(3))
#     print(main(9))
#     print(main(8))


# test()
