# 3.1
def multiply_by_12(x):
    a = x + x  # 2x
    b = a + a  # 4x
    c = b + b + b  #12x
    return c


# 3.2
def multiply_by_16(x):
    a = x + x  # 2x
    b = a + a  # 4x
    c = b + b  # 8x
    d = c + c  # 16x
    return d


# 3.3
def multiply_by_15(x):
    a = x + x  # 2x
    b = a + a  # 4x
    c = b + b  # 8x
    d = x - c  # -7x
    e = c - d  # 15x
    return e


print("3.1: Умножение на 12")
print(5, '->', multiply_by_12(5))
print(10, '->', multiply_by_12(10))
print(1, '->', multiply_by_12(1))
print()
print("3.2: Умножение на 16:")
print(5, '->', multiply_by_16(5))
print(10, '->', multiply_by_16(10))
print(1, '->', multiply_by_16(1))
print()
print("3.3: Умножение на 15:")
print(5, '->', multiply_by_15(5))
print(10, '->', multiply_by_15(10))
print(1, '->', multiply_by_15(1))
