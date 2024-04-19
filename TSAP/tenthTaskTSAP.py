# 1-ое по популярности
# def main(x):
#     result = []
#
#     for row in x:
#         if None in row:
#             continue
#
#         fullname = (row[0].split('!')[0].split()[2] + ' ' +
#                     row[0].split('!')[0].split()[0][0] + '.' +
#                     row[0].split('!')[0].split()[1])
#         birthdate = '-'.join(row[1].split('.')[::-1])
#         mail = row[0].split('!')[1].replace('[at]', '@')
#
#         result.append([fullname, birthdate, mail])
#
#     return list(map(list, zip(*result)))
# 2-ое по популярности
# def main(x):
#     return list(map(list, zip(*([
#         [row[0].split('!')[0].split()[2] + ' ' +
#         row[0].split('!')[0].split()[0][0] + '.' +
#         row[0].split('!')[0].split()[1],
#         '-'.join(row[1].split('.')[::-1]),
#         row[0].split('!')[1].replace('[at]', '@')]
#         for row in x if None not in row]))))
#
# def test():
#     print(main([['Петр З. Рамко!ramko48[at]yahoo.com', '14.02.2004', '14.02.2004'],
#                 ['Альберт Л. Зесук!al_bert55[at]rambler.ru', '15.01.1999', '15.01.1999']]))
#
# test()