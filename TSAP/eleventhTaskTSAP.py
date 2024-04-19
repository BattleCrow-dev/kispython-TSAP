# class MealyError(Exception):
#     pass
#
# 1-ое по популярности
# class Mealy:
#     state = 'A'
#
#     def mix(self):
#         if self.state == 'A':
#             self.state = 'B'
#             return 0
#         elif self.state == 'B':
#             self.state = 'F'
#             return 3
#         elif self.state == 'C':
#             self.state = 'D'
#             return 4
#         elif self.state == 'D':
#             self.state = 'E'
#             return 5
#         elif self.state == 'E':
#             self.state = 'E'
#             return 8
#         else:
#             raise MealyError('mix')
#
#     def fill(self):
#         if self.state == 'A':
#             self.state = 'C'
#             return 1
#         elif self.state == 'B':
#             self.state = 'C'
#             return 2
#         elif self.state == 'D':
#             self.state = 'B'
#             return 6
#         elif self.state == 'E':
#             self.state = 'F'
#             return 7
#         else:
#             raise MealyError('fill')
#
# 2-ое по популятности
# class Mealy:
#     state = 'A'
#
#     def mix(self):
#         match self.state:
#             case 'A':
#                 self.state = 'B'
#                 return 0
#             case 'B':
#                 self.state = 'F'
#                 return 3
#             case 'C':
#                 self.state = 'D'
#                 return 4
#             case 'D':
#                 self.state = 'E'
#                 return 5
#             case 'E':
#                 self.state = 'E'
#                 return 8
#             case _:
#                 raise MealyError('mix')
#
#     def fill(self):
#         match self.state:
#             case 'A':
#                 self.state = 'C'
#                 return 1
#             case 'B':
#                 self.state = 'C'
#                 return 2
#             case 'D':
#                 self.state = 'B'
#                 return 6
#             case 'E':
#                 self.state = 'F'
#                 return 7
#             case _:
#                 raise MealyError('fill')
#
# 3-ье по популярности
# class Mealy:
#     state = 'A'
#
#     MIX = {
#         'A' : ('B', 0),
#         'B' : ('F', 3),
#         'C' : ('D', 4),
#         'D' : ('E', 5),
#         'E' : ('E', 8)
#     }
#
#     FILL = {
#         'A' : ('C', 1),
#         'B' : ('C', 2),
#         'D' : ('B', 6),
#         'E' : ('F', 7)
#     }
#
#     def set_next(self, attr: str):
#         try:
#             action = self.__getattribute__(attr)
#             next_state = action[self.state]
#             self.state = next_state[0]
#             return next_state[1]
#         except KeyError:
#             raise MealyError(attr.lower())
#
#     def mix(self):
#         try:
#             return self.set_next('MIX')
#         except MealyError as exp:
#             raise exp
#
#     def fill(self):
#         try:
#             return self.set_next('FILL')
#         except MealyError as exp:
#             raise exp
#
# def main():
#     return Mealy()
#
# def test():
#     mealy = main()
#     assert mealy.mix() == 0
#     assert mealy.mix() == 3
#     try:
#         mealy.mix()
#     except MealyError:
#         pass
#     try:
#         mealy.fill()
#     except MealyError:
#         pass
#
#     mealy = main()
#     assert mealy.fill() == 1
#     assert mealy.mix() == 4
#     assert mealy.fill() == 6
#     assert mealy.fill() == 2
#     assert mealy.mix() == 4
#     assert mealy.mix() == 5
#     assert mealy.mix() == 8
#     assert mealy.fill() == 7
