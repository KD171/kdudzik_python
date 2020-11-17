# from lab_1.zd_16_complex_number import ComplexNumber
import parser
import argparse
import re
import collections

token_map = {'+': 'ADD', '\-': 'ADD',
             '*': 'MUL', '/': 'MUL',
             '(': 'LPAR', ')': 'RPAR',
             '\[': 'LPAR', '\]': 'PPAR',
             '**': 'POW'}

Token = collections.namedtuple('Token', ['name', 'value'])


class Calculator:

    def __init__(self, expr):
        print('[\d.]+|[%s]' % ''.join(token_map))
        split_expr = re.findall('[\d.]+|[%s]' % ''.join(token_map), expr)
        tokens = [Token(token_map.get(x, 'NUM'), x) for x in split_expr]
        print(split_expr)




expres = '56**8/(46)'
Calculator(expres)
