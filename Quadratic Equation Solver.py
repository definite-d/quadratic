#import time
#start = time.perf_counter()
""" Task is to create a program to solve quadratic equations."""
import string
import tkinter
from math import sqrt
from cmath import sqrt as csqrt

operators = ['+', '-', '*', '/', '=']

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
        self.is_Quadratic = False
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
        for part in self.parts:
            if f'{self.var}^2' in part:
                    self.is_Quadratic = True
                    break
        self.c = 0
        for const in constants:
            if '=' in const:
                const = const.replace('=', '-')
            self.c += int(const)
        self.c = str(self.c)
        self.ans1 = None
        self.ans2 = None

    def get_answers(self):
        if self.is_Quadratic == True:
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


import PySimpleGUI as sg

# Shuffled custom quadratic (Shuffle 1) PySimpleGUI Theme.
# Generated using Themera v1.0.0.
quadratic_Shuffled1_themedict = {'BACKGROUND': '#c10b12',
    'TEXT': 'white',
    'INPUT': '#fcc49c',
    'TEXT_INPUT': '#913d07',
    'SCROLL': '#666',
    'BUTTON': ('#660', '#fde6ce'),
    'PROGRESS': ('#f99fa3', '#f0490f'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 0}

sg.theme_add_new('quadratic_Shuffled1', quadratic_Shuffled1_themedict)
sg.theme('quadratic_Shuffled1')

layout =[
        [sg.Text('Quadratic Equation Solver', font=('Century Gothic', 24))],
        [sg.Column([
                [sg.Input('Please input a valid equation', key='equation')],
                [sg.Text('Decimal Accuracy', background_color='black'), sg.Spin([n+1 for n in range(15)], k='accuracy')],
                ], background_color='black', element_justification='center', size=(336, 57))],
        [sg.Text('Roots of Equation', k='r_lbl', font=('Century Gothic', 15))],
        [sg.Text('', k='r_txt', font=('Century Gothic', 13))],
]

main_window = sg.Window('Quadratic Equation Solver', layout, element_justification='center')

while True:
        event, values = main_window(timeout=5)

        if event in [None, 'Exit']:
                break

        try:
                eq = Equation(values['equation'])
                ans1, ans2 = eq.get_answers()
                if type(ans1) != complex:
                        ans1 = round(ans1, values['accuracy'])
                        ans2 = round(ans2, values['accuracy'])
                main_window['r_txt'](f'{ans1}, {ans2}')
        except (ValueError, AttributeError):
                main_window['r_txt'](f'Invalid Equation')
                pass

#end = time.perf_counter()
#print('Time taken:', end-start)

