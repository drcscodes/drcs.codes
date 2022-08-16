"""Silly program to demonstrate profiling and debugging"""

import random
import sys

def add(a, b):
    def inc(x):
        return x + 1
    if b == 0:
        return a
    else:
        return add(inc(a), b - 1)

def sub(a, b):
    def dec(x):
        return x - 1
    if b == 0:
        return a
    else:
        return sub(dec(a), b - 1)

def mult(a, b, accum = 0):
    if b == 0:
        return accum
    else:
        return mult(a, b - 1, accum + a)

def div(a, b, accum = 0):
    if a < b:
        return accum
    else:
        return div(a - b, b, accum + 1)

def profile():
    n = 10000
    while n > 0:
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        add(x, y)
        sub(x, y)
        mult(x, y)
        div(x, y)
        n -= 1


def main(args):
    if len(args) < 2:
        profile()
        sys.exit(0)
    x = int(args[1])
    op = args[2]
    y = int(args[3])
    funcs = {'+': add, '-': sub, '*': mult, '/': div}
    print('{} {} {} = {}'.format(x, op, y, funcs[op](x, y)))

if __name__=='__main__':
    main(sys.argv)
