import ast
from _ast import *

tree = ast.Module(
  body=[
    Expr(
      value=BinOp(
        left=BinOp(
          left=Name(id='y', ctx=Load()),
          op=BitOr(),
          right=Constant(value=4)),
        op=Add(),
        right=IfExp(
          test=Compare(
            left=Name(id='x', ctx=Load()),
            ops=[
              GtE()],
            comparators=[
              Constant(value=5)]),
          body=Constant(value=1),
          orelse=Constant(value=1))))],
  type_ignores=[])

# Выполняем интерпретацию AST и выводим результат
print(ast.unparse(tree))
