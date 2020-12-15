#! /usr/bin/env python3
import cmath


class ComplexNumber:

    def __init__(self, real, imaginary):
        if isinstance(real, (int, float)) and isinstance(imaginary, (int, float)):
            self.real = real
            self.imaginary = imaginary
        else:
            raise TypeError(f"Incorrect format: real: {type(real)}, imaginary: {type(imaginary)}")

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** (1 / 2)

    def __add__(self, other):
        other = self.check_other(other)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __radd__(self, other):
        return self.__add__(other)

    def __pow__(self, power, modulo=None):
        if isinstance(power, (float, int)):
            x = pow(self.real + self.imaginary * cmath.sqrt(-1), power)
        else:
            raise TypeError(f"Power is not a number; {type(power)}")
        return ComplexNumber(x.real, x.imag)

    def __str__(self):
        return '{0:.2f} {1} {2:.2f}i'.format(self.real, '+-'[self.imaginary < 0], abs(self.imaginary))

    def __neg__(self):
        return ComplexNumber(-self.real, -self.imaginary)

    def __eq__(self, other):
        other = self.check_other(other)
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        other = self.check_other(other)
        return self.real != other.real or self.imaginary != other.imaginary

    def __repr__(self):
        return str(self)

    def __sub__(self, other):
        other = self.check_other(other)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __rsub__(self, other):
        other = self.check_other(other)
        return other.__sub__(self)

    def __mul__(self, other):
        other = self.check_other(other)
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)

    def __rmul__(self, other):
        other = self.check_other(other)
        return other.__mul__(self)

    def __truediv__(self, other):
        other = self.check_other(other)
        conjugate = ComplexNumber(other.real, -other.imaginary)
        numerator = self * conjugate
        denominator = other * conjugate
        return ComplexNumber(numerator.real / denominator.real, numerator.imaginary / denominator.real)

    def __rtruediv__(self, other):
        other = self.check_other(other)
        return other.__truediv__(self)

    def _error(self, element):
        print(f"Operation {element} do not have a meaning for Complex numbers")

    def check_other(self, other):
        if isinstance(other, (int, float, str, complex)):
            if isinstance(other, str):
                try:
                    other = float(other)
                except Exception as e:
                    print(e)
            elif isinstance(other, complex):
                other = ComplexNumber(other.real, other.imag)
            else:
                other = ComplexNumber(other, 0)
        elif not isinstance(other, ComplexNumber):
            raise TypeError(f'Incorrect format: {type(other)}')
        return other
    
    def __gt__(self, other):
        self._error('>')

    def __ge__(self, other):
        self._error('>=')

    def __lt__(self, other):
        self._error('<')

    def __le__(self, other):
        self._error('<=')


if __name__ == "__main__":
    n = ComplexNumber(1, 4)
    y = ComplexNumber(0, 0)
    print(y)
    y = n ** 2
    m = ComplexNumber(4, 7)
    print(m + 2)
    print('/////////////')
    print(m/n)
    print(n ** 0.5)
    n = m
    print(n)
    var = n < m
    print(n + 2)
    m + 5
    print(4 - m)
    print(4*m)
    print(2+m*n)
    print(m/n)
    print(4/m)
    print(m/4)
    t = ComplexNumber(2, 0)
    print(t == 2)
    print(2 == t)
    print('/////////////')
    print(m*n)
    print((2+m)*n)
