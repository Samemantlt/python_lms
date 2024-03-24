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
        delimiter = nod(self.numerator_v, self.denominator_v)
        self.numerator_v //= delimiter
        self.denominator_v //= delimiter
    
    def numerator(self, value=None):
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
        return f'{self.numerator()}/{self.denominator()}'
    
    def __repr__(self):
        return f'Fraction({self.numerator()}, {self.denominator()})'
