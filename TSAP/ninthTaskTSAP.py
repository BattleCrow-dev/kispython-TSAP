# 1-ое по популярности
# import re
#
#
# def main(x):
#     res = dict()
#     regex_names = r'\bvar\s+(\w+)\b'
#     regex_values = r'\s+@"([^"]+)"'
#     names = re.findall(regex_names, x)
#     values = re.findall(regex_values, x)
#     for i in range(len(names)):
#         res[names[i]] = values[i]
#     return res

def main(x):
    res = {}
    words = x.split()
    i = 0
    while i < len(words):
        if 'var' in words[i]:
            name = words[i + 1]
            value = words[i + 3][2:-1].split('"')[0]
            res[name] = value
        i += 1
    return res


def test():
    print(main('| var reri_965 is @"lazate" var aran_689 is @"tiinon" var estete is\n@"dimabe"var azatiso_51 is @"quti_594" |'))
    print(main('| var isxe is @"user" var ramage_340 is @"zaante" var atra is @"tela" |'))
    print(main('| var esxe is @"atis_165" var geleer is @"orma_618" var diarbi is @"teon" var arrion_463 is @"attiat_709" |'))


test()