def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


class Fraction:
    def __init__(self, numerator, denominator=None):
        if denominator is None:
            numerator, denominator = map(int, str(numerator).split('/'))
        self.numerator_v = numerator
        self.denominator_v = denominator
        self.__denominate()
    
    def __denominate(self):
        delimiter = nod(abs(self.numerator_v), abs(self.denominator_v))
        self.numerator_v //= delimiter
        self.denominator_v //= delimiter
        if self.denominator_v < 0:
            self.denominator_v *= -1
            self.numerator_v *= -1
    
    def numerator(self, value=None):
        if value is None:
            return abs(self.numerator_v)
        self.numerator_v = value
        self.__denominate()

    def __numerator_p(self, value=None):
        if value is None:
            return self.numerator_v
        self.numerator_v = value
        self.__denominate()
    
    def denominator(self, value=None):
        if value is None:
            return self.denominator_v
        self.denominator_v = value
        self.__denominate()
    
    def __str__(self):
        return f'{self.__numerator_p()}/{self.denominator()}'
    
    def __repr__(self):
        return f"Fraction('{str(self)}')"
    
    def __neg__(self):
        return Fraction(-self.__numerator_p(), self.denominator())

    def __add__(self, other):
        result = Fraction(
            self.__numerator_p() * other.denominator() + other.__numerator_p() * self.denominator(), 
            self.denominator() * other.denominator()
        )
        return result

    def __sub__(self, other):
        return self + (-other)
    
    def __iadd__(self, other):
        self.__numerator_p(self.__numerator_p() * other.denominator() + other.__numerator_p() * self.denominator())
        self.denominator(self.denominator() * other.denominator())

        return self
    
    def __isub__(self, other):
        self += (-other)
        return self

    def __imul__(self, other):
        self.numerator_v *= other.numerator_v
        self.denominator_v *= other.denominator_v
        self.__denominate()

        return self
    
    def __itruediv__(self, other):
        self *= other.reverse()
        return self
    
    def __mul__(self, other):
        a = Fraction(self.__numerator_p(), self.denominator())
        a *= other
        return a
    
    def __truediv__(self, other):
        a = Fraction(self.__numerator_p(), self.denominator())
        a /= other
        return a
    
    def reverse(self):
        return Fraction(self.denominator_v, self.numerator_v)
