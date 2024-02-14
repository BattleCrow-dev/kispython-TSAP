# 1-ое по популярности
# def main(n, z, m, a):
#     s1, s2 = 0, 0
#
#     for c in range(1, n + 1):
#         s1 += (c / 17 - 14 * z**3 - 55 * z**2)**7
#
#     for i in range(1, a + 1):
#         for k in range(1, m + 1):
#             s2 += 78 * (19 - k - 3 * k**2)**5 + i**4
#
#     return s1 + s2

# 2-ое по популярности
# def main(n, z, m, a):
#     return (sum((c / 17 - 14 * z**3 - 55 * z**2)**7 for c in range(1, n + 1))
#             + sum(78 * (19 - k - 3 * k**2)**5 + i**4 for k in range(1, m + 1)
#                   for i in range(1, a + 1)))

# 3-ье по популярности
# from functools import reduce
#
#
# def main(n, z, m, a):
#     s1 = reduce(
#         lambda acc, c: acc + (c / 17 - 14 * z**3 - 55 * z**2) ** 7,
#         range(1, n + 1),
#         0,
#     )
#     s2 = reduce(
#         lambda acc, i: acc
#         + reduce(
#             lambda acc2, k: acc2 + 78 * (19 - k - 3 * k**2) ** 5 + i**4,
#             range(1, m + 1),
#             0,
#         ),
#         range(1, a + 1),
#         0,
#     )
#
#     return s1 + s2

# 4-ое по популярности
# def main(n, z, m, a):
#     s1, s2 = 0, 0
#
#     c = 1
#     while c < n + 1:
#         s1 += (c / 17 - 14 * z**3 - 55 * z**2)**7
#         c += 1
#
#     i = 1
#     while i < a + 1:
#         k = 1
#         while k < m + 1:
#             s2 += 78 * (19 - k - 3 * k**2)**5 + i**4
#             k += 1
#         i += 1
#
#     return s1 + s2

# 5-ое по популярности
# def main(n, z, m, a, c=1, i=1, k=1, s1=0, s2=0):
#     if c <= n:
#         s1 += (c / 17 - 14 * z**3 - 55 * z**2)**7
#         return main(n, z, m, a, c + 1, i, k, s1, s2)
#     elif i <= a:
#         if k <= m:
#             s2 += 78 * (19 - k - 3 * k**2)**5 + i**4
#             return main(n, z, m, a, c, i, k + 1, s1, s2)
#         else:
#             return main(n, z, m, a, c, i + 1, 1, s1, s2)
#     else:
#         return s1 + s2


# def test():
#     print(main(3, 0.99, 3, 5))
#     print(main(5, 0.6, 7, 3))
#     print(main(4, 0.34, 6, 7))
#     print(main(6, -0.79, 2, 4))
#     print(main(2, -0.54, 6, 8))


#test()
