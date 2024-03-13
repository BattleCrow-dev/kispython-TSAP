# 1-е по популярности
# def main(x):
#     tree = {
#         'index': 1,
#         2014: {
#             'index': 0,
#             'SCAML': {
#                 'index': 3,
#                 'C++': 0,
#                 'BRO': {
#                     'index': 2,
#                     1963: 1,
#                     1971: 2,
#                     1969: 3
#                 }
#             },
#             'QMAKE': 4
#         },
#         1971: {
#             'index': 2,
#             1963: {
#                 'index': 4,
#                 'SELF': 5,
#                 'APL': 6
#             },
#             1971: 7,
#             1969: {
#                 'index': 3,
#                 'C++': 8,
#                 'BRO': {
#                     'index': 0,
#                     'SCAML': 9,
#                     'QMAKE': 10
#                 }
#             }
#         },
#         1977: 11
#     }
#
#     def get_value(t):
#         if type(t) is int:
#             return t
#         return get_value(t[x[t["index"]]])
#
#     return get_value(tree)


# 2-е по популярности
# def main(x):
#     tree = {
#         x[1] == 2014: {
#             x[0] == 'SCAML': {
#                 x[3] == 'C++': 0,
#                 x[3] == 'BRO': {
#                     x[2] == 1963: 1,
#                     x[2] == 1971: 2,
#                     x[2] == 1969: 3
#                 }
#             },
#             x[0] == 'QMAKE': 4
#         },
#         x[1] == 1971: {
#             x[2] == 1963: {
#                 x[4] == 'SELF': 5,
#                 x[4] == 'APL': 6
#             },
#             x[2] == 1971: 7,
#             x[2] == 1969: {
#                 x[3] == 'C++': 8,
#                 x[3] == 'BRO': {
#                     x[0] == 'SCAML': 9,
#                     x[0] == 'QMAKE': 10
#                 }
#             }
#         },
#         x[1] == 1977: 11
#     }
#
#     while type(tree) is not int:
#         tree = tree[True]
#
#     return tree

# 3-е по популярности
# def main(x):
#     match x[1]:
#         case 2014:
#             return ((x[0] == 'QMAKE') * 4 +
#                     (x[0] == 'SCAML') *
#                     ((x[3] == 'C++') * 0) +
#                     (x[3] == 'BRO')
#                     * ((x[2] == 1963) * 1 +
#                        (x[2] == 1971) * 2 +
#                        (x[2] == 1969) * 3))
#         case 1971:
#             return ((x[2] == 1963) *
#                     ((x[4] == 'SELF') * 5 +
#                      (x[4] == 'APL') * 6) +
#                     (x[2] == 1971) * 7 +
#                     (x[2] == 1969) *
#                     ((x[3] == 'C++') * 8 +
#                      (x[3] == 'BRO') *
#                      ((x[0] == 'SCAML') * 9 +
#                       (x[0] == 'QMAKE') * 10)))
#         case 1977:
#             return 11


# def main(x):
#     match x[1]:
#         case 2014:
#             match x[0]:
#                 case 'SCAML':
#                     match x[3]:
#                         case 'C++':
#                             return 0
#                         case 'BRO':
#                             match x[2]:
#                                 case 1963:
#                                     return 1
#                                 case 1971:
#                                     return 2
#                                 case 1969:
#                                     return 3
#                 case 'QMAKE':
#                     return 4
#         case 1971:
#             match x[2]:
#                 case 1963:
#                     match x[4]:
#                         case 'SELF':
#                             return 5
#                         case 'APL':
#                             return 6
#                 case 1971:
#                     return 7
#                 case 1969:
#                     match x[3]:
#                         case 'C++':
#                             return 8
#                         case 'BRO':
#                             match x[0]:
#                                 case 'SCAML':
#                                     return 9
#                                 case 'QMAKE':
#                                     return 10
#         case 1977:
#             return 11

# 4-е по популярности
# def main(x):
#     x2_1 = [(x[2] == 1963, 1), (x[2] == 1971, 2), (x[2] == 1969, 3)]
#     x0_1 = [(x[0] == 'SCAML', 9), (x[0] == 'QMAKE', 10)]
#     x3_1 = [(x[3] == 'C++', 0), (x[3] == 'BRO', x2_1)]
#     x3_2 = [(x[3] == 'C++', 8), (x[3] == 'BRO', x0_1)]
#     x4 = [(x[4] == 'SELF', 5), (x[4] == 'APL', 6)]
#     x0_2 = [(x[0] == 'SCAML', x3_1), (x[0] == 'QMAKE', 4)]
#     x2_2 = [(x[2] == 1963, x4), (x[2] == 1971, 7), (x[2] == 1969, x3_2)]
#     x1 = [(x[1] == 2014, x0_2), (x[1] == 1971, x2_2), (x[1] == 1977, 11)]
#
#     cur = x1
#
#     while type(cur) is not int:
#         for child in cur:
#             if child[0]:
#                 cur = child[1]
#
#     return cur

# 5-е по популярности
# class Node:
#     children = []
#     var = 0
#     value = 0
#
#     def __init__(self, var, value=0):
#         self.children = []
#         self.var = var
#         self.value = value
#
#     def append(self, node, cond):
#         self.children.append((cond, node))
#
#     def get_value(self, x):
#         for child in self.children:
#             if x[self.var] == child[0]:
#                 return child[1].get_value(x)
#         return self.value
#
#
# def main(x):
#     x0_1 = Node(0)
#     x0_2 = Node(0)
#     x1 = Node(1)
#     x2_1 = Node(2)
#     x2_2 = Node(2)
#     x3_1 = Node(3)
#     x3_2 = Node(3)
#     x4 = Node(4)
#
#     x1.append(x0_1, 2014)
#     x1.append(x2_2, 1971)
#     x1.append(Node(0, 11), 1977)
#
#     x0_1.append(x3_1, 'SCAML')
#     x0_1.append(Node(0, 4), 'QMAKE')
#
#     x3_1.append(Node(0, 0), 'C++')
#     x3_1.append(x2_1, 'BRO')
#
#     x2_1.append(Node(0, 1), 1963)
#     x2_1.append(Node(0, 2), 1971)
#     x2_1.append(Node(0, 3), 1969)
#
#     x2_2.append(x4, 1963)
#     x2_2.append(Node(0, 7), 1971)
#     x2_2.append(x3_2, 1969)
#
#     x4.append(Node(0, 5), 'SELF')
#     x4.append(Node(0, 6), 'APL')
#
#     x3_2.append(Node(0, 8), 'C++')
#     x3_2.append(x0_2, 'BRO')
#
#     x0_2.append(Node(0, 9), 'SCAML')
#     x0_2.append(Node(0, 10), 'QMAKE')
#
#     return x1.get_value(x)


# def test():
#     print(main(['QMAKE', 1977, 1963, 'C++', 'APL']))
#     print(main(['QMAKE', 2014, 1971, 'C++', 'SELF']))
#     print(main(['QMAKE', 1971, 1971, 'BRO', 'SELF']))
#     print(main(['QMAKE', 1971, 1969, 'BRO', 'APL']))
#     print(main(['QMAKE', 1971, 1963, 'BRO', 'APL']))
#
#
# test()
