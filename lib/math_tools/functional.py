from sympy import *


# Check for horizontal asymptote: if (lim as x -> infinity) and (lim as x -> -infinity) == the same number
def find_horizontal_asymptote(expr, func_symbols):
    ha = list()
    for symbol in func_symbols:
        if limit(expr, symbol, oo) == limit(expr, symbol, -oo):
            ha.append(int(limit(expr, symbol, oo)))
    return ha
