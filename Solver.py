from sympy import *
a, b, c, d, x, y, z = symbols('a b c d x y z')
init_printing(use_unicode=True)

def simplify_function():
    while True:
        expr = input('Enter expression to simplify, or q to quit ---> ')
        if expr == 'q':
            exit()
        else: pprint(simplify(expr))
#Call function here

def expand_function():
    while True:
        expr = input('Enter expression to expand, or q to quit ---> ')
        if expr == 'q':
            exit()
        else: pprint(expand(expr))
#Call function here

def factor_function():
    while True:
        expr = input('Enter expression to factor, or q to quit ---> ')
        if expr == 'q':
            exit()
        else: pprint(factor(expr))
#Call function here

def collect_function():
    while True:
        expr = input('Enter expression to collect terms, or q to quit ---> ')
        if expr == 'q':
            exit()
        else: pprint(collect(expr, x))  #enter variable to collect
#Call function here

def cancel_function():
    while True:
        expr = input('Enter expression to cancel, or q to quit ---> ')
        if expr == 'q':
            exit()
        else: pprint(cancel(expr))
#Call function here



















