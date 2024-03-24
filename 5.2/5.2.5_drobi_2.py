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
        
        minus = self.numerator_v < 0
        self.numerator_v = abs(value)
        self.__denominate()
        if value < 0:
            minus = not minus

        if minus:
            self.numerator_v *= -1
        
    def denominator(self, value=None):
        if value is None:
            return self.denominator_v
        
        minus = self.numerator_v < 0
        self.numerator_v = abs(self.numerator_v)
        self.denominator_v = abs(value)
        self.__denominate()
        if value < 0:
            minus = not minus
            
        if minus:
            self.numerator_v *= -1

    def __str__(self):
        return f'{self.numerator_v}/{self.denominator()}'
    
    def __repr__(self):
        return f"Fraction('{str(self)}')"

    def __neg__(self):
        return Fraction(-self.numerator_v, self.denominator_v)

a = Fraction('-1/2')
a.denominator(-3)
print(a)

assert str(Fraction('3/-9')) == '-1/3'
assert str(Fraction('1/-2')) == '-1/2'
assert str(Fraction('4/3')) == '4/3'
assert str(Fraction('6/3')) == '2/1'
assert str(Fraction('6/-3')) == '-2/1'
assert str(Fraction('-6/3')) == '-2/1'

f = Fraction('3/-9')
assert str(f) == '-1/3'
f.numerator(-2)
assert str(f) == '2/3'

f = Fraction('3/-9')
assert str(f) == '-1/3'
f.numerator(2)
assert str(f) == '-2/3'

f = Fraction('2/4')
assert str(f) == '1/2'
f.numerator(-3)
assert str(f) == '-3/2'

f = Fraction('2/4')
assert str(f) == '1/2'
f.numerator(-3)
assert str(f) == '-3/2'