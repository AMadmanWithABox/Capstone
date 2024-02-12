from sympy import *
from sympy.core.numbers import One

from lib.constants import ROUNDING


# Check for horizontal asymptote: if (lim as x -> infinity) and (lim as x -> -infinity) == the same number
def find_horizontal_asymptote(expr, func_symbols):
    if isinstance(expr, exp) and isinstance(expr.args[0], Symbol):
        return [int(limit(expr, func_symbols[0], -oo))]
    if isinstance(expr, Pow) and isinstance(expr.args[1], Symbol):
        f = lambdify(func_symbols[0], expr, modules=['numpy'])
        return [int(f(-10000)) if int(f(-10000)) == int(f(-10001)) else int(f(10000))]
    try:
        ha = list()
        for symbol in func_symbols:
            if (limit(expr, symbol, oo) == limit(expr, symbol, -oo)
                    and limit(expr, symbol, oo) != oo
                    and limit(expr, symbol, oo) != -oo
                    and not isinstance(limit(expr, symbol, oo), AccumBounds)
            ):
                ha.append(int(limit(expr, symbol, oo)))
        return ha
    except:
        return list()


def find_vertical_asymptote(expr, func_symbols, x_range):
    if isinstance(expr, Number):
        return list()
    va = list()
    numerator = numer(expr)
    denominator = denom(expr)
    for s in func_symbols:
        if not isinstance(denominator, One) and not isinstance(numerator, log):
            va = list(solve(denominator, s))
        elif isinstance(expr, tan):
            va = list([round(pi / 2 + (pi * n), ROUNDING) for n in range(-x_range, x_range)])
        elif isinstance(expr, cot):
            va = list([round(pi * n, ROUNDING) for n in range(-x_range, x_range)])
        elif isinstance(expr, sec):
            va = list([round(pi / 2 + (pi * n), ROUNDING) for n in range(-x_range, x_range)])
        elif isinstance(expr, csc):
            va = list([round(pi * n, ROUNDING) for n in range(-x_range, x_range)])
        elif isinstance(expr, log):
            try:
                va = list(solve(expr.args[0], s))
            except NotImplementedError:
                pass
        elif isinstance(numerator, log) and isinstance(denominator, log):
            va = list(solve(numerator.args[0], s))
        # elif isinstance(expr, Pow):
        #     if isinstance(expr.args[0], Symbol):
        #         if isinstance(expr.args[1], Symbol):
        #             va = list()
        #         elif expr.args[1] < 1:
        #             va = list(solve(expr, s))
        #     else:
        #         va = list()
        elif isinstance(expr, Add):
            try:
                va = list(find_vertical_asymptote(n, func_symbols, x_range) for n in expr.args)
                va = list(flatten(va))
            except NotImplementedError:
                args = expr.args
                for argument in args:
                    if isinstance(argument, Mul):
                        argument = argument.args[0] if isinstance(argument.args[0], log) else argument.args[1]
                    if isinstance(argument, log):
                        va = list(solve(argument.args[0], s))

    verified_va = list()
    for num in va:
        if isinstance(num, int) and isinstance(num, float):
            verified_va.append(num)
        else:
            try:
                verified_va.append(round(float(num), ROUNDING))
            except TypeError:
                pass
    return verified_va


def find_oblique_asymptote(expr, func_symbols=None):
    numerator = numer(expr)
    denominator = denom(expr)

    if isinstance(denominator, One):
        return
    num_degree = degree(numerator)
    den_degree = degree(denominator)
    if num_degree != den_degree + 1:
        return
    poly_num = Poly(numerator)
    poly_den = Poly(denominator)
    poly_div = div(poly_num, poly_den)
    if poly_div[1] == 0:
        return
    return poly_div[0].as_expr()


def find_holes(expr):
    numerator = numer(expr)
    denominator = denom(expr)
    if isinstance(numerator, One) or isinstance(denominator, One):
        return
    print(f'Numerator {numerator} is of type {type(numerator)}')
    print(f'Denominator {denominator} is of type {type(denominator)}')
    if isinstance(denominator, Symbol):
        return [0]
    numerator = factor_list(numerator)
    denominator = factor_list(denominator)
    holes = list()
    for i in range(len(numerator[1])):
        for j in range(len(denominator[1])):
            if numerator[1][i][0] == denominator[1][j][0]:
                holes.append(numerator[1][i][0])
    holes_1d = list()
    if len(holes) > 0:
        holes = [solve(h) for h in holes]
        for i in range(len(holes)):
            for j in range(len(holes[i])):
                try:
                    holes_1d.append(round(float(holes[i][j]), ROUNDING))
                except TypeError:
                    pass
    return holes_1d
