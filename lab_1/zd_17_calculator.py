#! /usr/bin/env python3
import re
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from lab_1.zd_16_complex_number import ComplexNumber

clk1 = "i(2.5j*8)(i+4)/(8i)ii"
clk2 = "3*8i"
clk3 = "4/22*5*i"
clk4 = "26-i/8i(4j)"

class Calculator:

    def __init__(self, expr):
        self.expr = expr
        elements = re.findall(r'[\d.]+|[*][*]|[+-/*()\[\]ij]', expr.replace(' ', ''))
        if len(elements) > 0:
            i = ComplexNumber(0, 1)
            j = ComplexNumber(0, 1)
            elements = self.typeChangerToFloat(elements)
            elements = self.addMissingElements(elements)
            elements = self.typeChangerToStr(elements)
            expr = ''.join(elements)
            print(self.expr, " = ", eval(expr))
        else:
            raise ValueError

    def typeChangerToFloat(self, tokens):
        operators = ['+', '-', '*', '/', '(', ')', '[', ']', 'i', 'j']
        for x in range(len(tokens)):
            if tokens[x] not in operators:
                tokens[x] = float(tokens[x])
        return tokens

    def typeChangerToStr(self, tokens):
        for x in range(len(tokens)):
                tokens[x] = str(tokens[x])
        return tokens

    def addMissingElements(self, tokens):
        new_tokens = []
        arg1 = [[')', ']'], ['i', 'j'], [')', ']'], ['i', 'j']]
        arg2 = [['(', '['], ['(', '['], ['i', 'j'], ['i', 'j']]
        for x in range(0, len(tokens) - 1, 1):
            new_tokens.append(tokens[x])
            for y in range(len(arg1)):
                if tokens[x] == arg1[y][0] or tokens[x] == arg1[y][1]:
                    if tokens[x + 1] == arg2[y][0] or tokens[x + 1] == arg2[y][1]:
                        new_tokens.append("*")
            if tokens[x] == 'i' or tokens[x] == 'j':
                if isinstance(tokens[x + 1], float):
                    new_tokens.append("*")
            if tokens[x + 1] == 'i' or tokens[x + 1] == 'j':
                if isinstance(tokens[x], float):
                    new_tokens.append("*")

        new_tokens.append(tokens[-1])
        return new_tokens


if __name__ == "__main__":
    print("Examples:")
    Calculator(clk1)
    Calculator(clk2)
    Calculator(clk3)
    Calculator(clk4)
    Calculator(input("Insert an expression to calculate: "))



