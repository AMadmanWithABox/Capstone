from sympy import *


# Check for horizontal asymptote: if (lim as x -> infinity) and (lim as x -> -infinity) == the same number
def find_horizontal_asymptote(expr, symbols):
    for symbol in symbols:
        if limit(expr, symbol, oo) == limit(expr, symbol, -oo):
            return limit(expr, symbol, oo)
