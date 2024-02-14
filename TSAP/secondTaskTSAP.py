# 1-ое по популярности
# from math import tan
#
#
# def main(z):
#     if z < -27:
#         return (86 * z + 97 * z**2 + z**3)**7 - z**3 - z**4
#     elif z < 22:
#         return (z - 1)**7 - (96 * z**3)**5
#     elif z < 97:
#         a = (z**2 + 56 * z**3)**3 / 64
#         b = (z + 44 + 3 * z**2)**4 / 8
#         return a - b
#     else:
#         return 33 * tan(z) ** 2

# 2-ое по популярности
# from math import tan
#
#
# def main(z):
#     return (86 * z + 97 * z**2 + z**3)**7 - z**3 - z**4 if z < -27 \
#         else (z - 1)**7 - (96 * z**3)**5 if z < 22 \
#         else (z**2 + 56 * z**3)**3 / 64 - (z + 44 + 3 * z**2)**4 / 8 if z < 97 \
#         else 33 * tan(z) ** 2

# 3-ье по популярности
# from math import tan
#
#
# def main(z):
#     conditions = {
#         z < -27: (86 * z + 97 * z ** 2 + z ** 3) ** 7 - z ** 3 - z ** 4,
#         -27 <= z < 22: (z - 1) ** 7 - (96 * z ** 3) ** 5,
#         22 <= z < 97: (z ** 2 + 56 * z ** 3) ** 3 / 64 -
#                       (z + 44 + 3 * z ** 2) ** 4 / 8,
#         97 <= z: 33 * tan(z) ** 2
#     }
#
#     return conditions[True]


# def test():
#     print(main(118))
#     print(main(130))
#     print(main(52))
#     print(main(-17))
#     print(main(-41))
#
#
# test()
