def main(x):
    ans = [0 for i in range(26)]
    q2, q3, q4 = int(x['Q2']), int(x['Q3']), int(x['Q4'])

    ind = 4
    while ind < len(ans):
        if ind < 14:
            ans[ind] = q2 % 2
            q2 >>= 1
        elif ind < 20:
            ans[ind] = q3 % 2
            q3 >>= 1
        else:
            ans[ind] = q4 % 2
            q4 >>= 1
        ind += 1

    return hex(int('0b' + ''.join([str(i) for i in ans[::-1]]), 2))


def test():
    print(main({'Q2': '785', 'Q3': '52', 'Q4': '63'}))
    print(main({'Q2': '723', 'Q3': '7', 'Q4': '35'}))
    print(main({'Q2': '961', 'Q3': '25', 'Q4': '26'}))
    print(main({'Q2': '301', 'Q3': '17', 'Q4': '36'}))

    assert main({'Q2': '785', 'Q3': '52', 'Q4': '63'}) == '0x3fd3110'
    assert main({'Q2': '723', 'Q3': '7', 'Q4': '35'}) == '0x231ed30'
    assert main({'Q2': '961', 'Q3': '25', 'Q4': '26'}) == '0x1a67c10'
    assert main({'Q2': '301', 'Q3': '17', 'Q4': '36'}) == '0x24452d0'


test()
