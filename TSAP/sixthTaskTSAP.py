# def main(K: set) -> int:
#     H = {abs(k) for k in K if 22 > k > -60}
#     B = {5 * k + k % 2 for k in K if (k <= 91) != (k > -14)}
#     delta = {n // 3 for n in H if n in range(0, 56)}
#     return sum(B.union(H)) * (1 - sum(delta))


# def test():
#     print(main({-90, -89, -24, 49, -77, -11, 86, 87, -38}))
#     print(main({98, -28, -27, -16, -46, -12, 53, 60, -67, -98}))


# test()
