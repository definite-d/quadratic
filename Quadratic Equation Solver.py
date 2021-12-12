#import time
#start = time.perf_counter()
""" Task is to create a program to solve quadratic equations."""
import string
from math import sqrt
from cmath import sqrt as csqrt

operators = ['+', '-', '*', '/', '=']

# equation = str(input('Please input an equation: '))

equation = r'x^2 -x - 6 = 0    '


def rectify_to_one(value):
        if value in '':
            return '1'
        if value == '-':
            return '-1'
        else:
            return value

class Equation:

    def __init__(self, eq_str):
        """
        Initiaization function.
        """
        self.origin = eq_str

        for char in self.origin:
            if char in string.ascii_lowercase:
                self.var = char
            
        """
        Split the equation into the components (a, b, c)
        """
        guinea_pig = self.origin
        for operator in operators:
            if operator in guinea_pig:
                guinea_pig = guinea_pig.replace(operator, f'@{operator}')
        self.parts = guinea_pig.split('@')
        violations = [' ', ',', '+']
        for violation in violations:
            self.parts = list(map(lambda x: x.replace(violation, ''), self.parts))
    
        constants = []
        for part in self.parts:
            if f'{self.var}^2' in part:
                self.a = part.replace(f'{self.var}^2', '')
                self.a = rectify_to_one(self.a)
            if (f'{self.var}' in part) and (f'{self.var}^2' not in part):
                self.b = part.replace(f'{self.var}', '')
                self.b = rectify_to_one(self.b)
            if f'{self.var}' not in part and part != '':
                constants.append(part)
        self.c = 0
        for const in constants:
            if '=' in const:
                const = const.replace('=', '-')
            self.c += int(const)
        self.c = str(self.c)
        self.ans1 = None
        self.ans2 = None

    def get_answers(self):
        self.a = int(self.a)
        self.b = int(self.b)
        self.c = int(self.c)
        try:
            fourac = (4*self.a*self.c)*-1
            rooted = sqrt((self.b**2)+(fourac))
            self.ans1 = ((-1*self.b) + rooted)/(2*self.a)
            self.ans2 = ((-1*self.b) - rooted)/(2*self.a)
            return self.ans1, self.ans2
        except ValueError:
            fourac = (4*self.a*self.c)*-1
            rooted = csqrt((self.b**2)+(fourac))
            self.ans1 = ((-1*self.b) + rooted)/(2*self.a)
            self.ans2 = ((-1*self.b) - rooted)/(2*self.a)
            return self.ans1, self.ans2

some_eq = Equation(equation)
print('a',some_eq.a)
print('b',some_eq.b)
print('c',some_eq.c)
some_eq.get_answers()
print(f'Roots of equation: {some_eq.ans1}, {some_eq.ans2}')

#end = time.perf_counter()
#print('Time taken:', end-start)

