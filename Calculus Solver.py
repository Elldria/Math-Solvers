from sympy import *
a, b, c, d, x, y, z = symbols('a b c d x y z')
init_printing(use_unicode=True)

def differentiate_function():
    while True:
        expr = input('Enter expression to cancel, or q to quit ---> ')
        if expr == 'q':
            exit()
        else: pprint(diff(expr, x)) # Enter 3rd parameter to differentiate multiple times
#Call function here

def integrate_function():
    while True:
        expr = input('Enter expression to cancel, or q to quit ---> ')
        if expr == 'q':
            exit()
        else: pprint(integrate(expr)) # Enter 3rd parameter to differentiate multiple times
#Call function here


