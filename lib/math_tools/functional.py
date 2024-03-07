import warnings

import sympy
from sympy import *
from sympy.calculus.util import continuous_domain
from sympy.core.numbers import One
from sympy.abc import x, y

from lib.constants import ROUNDING


# Check for horizontal asymptote: if (lim as x -> infinity) and (lim as x -> -infinity) == the same number
def find_horizontal_asymptote(expr, func_symbols, x_range):
    try:
        inverse_expr = solve(Eq(y, expr), x)
        ha = list()
        for expression in inverse_expr:
            try:
                ha.extend(find_vertical_asymptote(expression, y, x_range))
            except:
                pass
        return ha
    except:
        if isinstance(expr, exp) and isinstance(expr.args[0], Symbol):
            if len(expr.args) > 1:
                return limit(expr, func_symbols[0], -oo)
            return [0]
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


# def window_solver(expr, x_range):
#     solve_set = list()
#     current = -x_range
#     if isinstance(expr.args[0], log) or isinstance(expr, log) or (isinstance(expr.args[0], Pow) and (expr.args[0].args[1] < 1)):
#         current = 0
#     while current < x_range:
#         try:
#             current = nsolve(expr, (current, current + 0.5), solver='bisect', rational=False)
#             solve_set.append(current)
#             current += 0.001
#         except ValueError as e:
#             current += 1
#             pass
#         except TypeError as e:
#             pass
#     return solve_set


def singularity_finder(expr, func_symbol, x_range):
    solve_set = list()
    # Singularities are Asymptotes
    solve_set_unfiltered = singularities(expr, func_symbol, Interval(-x_range, x_range))
    if solve_set_unfiltered is EmptySet:
        return solve_set

    for s in solve_set_unfiltered:
        if not s.is_real:
            continue

        else:
            solve_set.append(nfloat(s))
    return solve_set


def find_vertical_asymptote(expr, func_symbol, x_range):
    va = singularity_finder(expr, func_symbol, x_range)
    # if isinstance(expr, Number):
    #     return list()
    # va = list()
    # args = list(expr.args)
    # args.append(expr)
    # for s in func_symbols:
    #     for argument in args:
    #         numerator = numer(argument)
    #         denominator = denom(argument)
    #         if not isinstance(denominator, One) and not isinstance(numerator, log):
    #             if isinstance(denominator, sin) or isinstance(denominator, cos) or isinstance(denominator, tan):
    #                 va = window_solver(denominator, x_range)
    #             else:
    #                 va = list(solve(denominator, s))
    #         elif isinstance(argument, tan):
    #             inside = argument.args[0]
    #             solve_set = window_solver(cos(inside), x_range)
    #             va = list([round(n, ROUNDING) for n in solve_set])
    #             print(va)
    #         elif isinstance(argument, log):
    #             try:
    #                 print(argument)
    #                 if isinstance(argument.args[0], Symbol):
    #                     va = list([0])
    #                 else:
    #                     va = list(solve(argument.args[0], s))
    #                 print(va)
    #             except NotImplementedError:
    #                 pass
    #         elif isinstance(numerator, log) and isinstance(denominator, log):
    #             va = list(solve(numerator.args[0], s))
    #         elif isinstance(argument, Pow):
    #             if isinstance(argument.args[0], Symbol):
    #                 if isinstance(argument.args[1], Symbol):
    #                     va = list()
    #                 elif argument.args[1] < 1:
    #                     va = list(solve(argument, s))
    #             elif isinstance(argument.args[0], tan):
    #                 va = window_solver(argument.args[0], x_range)
    #             else:
    #                 va = list()
    #         elif isinstance(argument, Add):
    #             try:
    #                 va = list(find_vertical_asymptote(n, func_symbols, x_range) for n in argument.args)
    #                 va = list(flatten(va))
    #             except NotImplementedError:
    #                 args = argument.args
    #                 for argument2 in args:
    #                     if isinstance(argument2, Mul):
    #                         argument2 = argument2.args[0] if isinstance(argument2.args[0], log) else argument2.args[1]
    #                     if isinstance(argument2, log):
    #                         va = list(solve(argument2.args[0], s))

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
    # print(f'Numerator {numerator} is of type {type(numerator)}')
    # print(f'Denominator {denominator} is of type {type(denominator)}')
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
