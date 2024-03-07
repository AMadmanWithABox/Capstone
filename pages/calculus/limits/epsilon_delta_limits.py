# import dash
# import dash_mantine_components as dmc
# from dash import html, dcc, Input, Output, callback
# from sympy import *
#
# from lib.templates.basic_graph_component import create_basic_graph
#
# dash.register_page(__name__, path='/calculus/limits/epsilon-delta', name='epsilon delta Limits', order=2)
#
#
# def testing():
#     x = symbols('x')
#     expr = (x ** 2 + 6 * x + 9) / (x + 3)
#     denominator = denom(expr)
#     print(denominator)
#     solution = solve(denominator, x)
#     for s in solution:
#         print(s.round(2))
#     print(solve(denominator, x))
#
#
#
# functions_list = [
#     "x**2",
#     "x**3 - 3*x**2 + 2",
#     "1/x",
#     "sqrt(x)",
#     "exp(x)",
#     "log(x, 3)",
#     "sin(x)",
#     "cos(x)",
#     "tan(x)",
#     "asin(x)",
#     "acos(x)",
#     "atan(x)",
#     "sinh(x)",
#     "cosh(x)",
#     "tanh(x)",
#     "x**2 + 2*x + 1",
#     "x**4 - 4*x**3 + 6*x**2 - 4*x + 1",
#     "(x**2 - 1)/(x - 1)",
#     "2**x",
#     "2**-x",
#     "log(x)",
#     "Abs(x)",
#     "ceiling(x)",
#     "floor(x)",
#     "x % 2",
#     "x * sin(x)",
#     "exp(-x**2)",
#     "1/(1 + exp(-x))",
#     "sin(x)**2 + cos(x)**2",
#     "tan(x)**2 + 1",
#     "sin(2*x)",
#     "cos(2*x)",
#     "sin(x)**2",
#     "cos(x)**2",
#     "(1 - cos(2*x))/2",
#     "(1 + cos(2*x))/2",
#     "1/cos(x)",
#     "1/sin(x)",
#     "1/tan(x)",
#     "sin(x)/cos(x)",
#     "x**3 + 3*x**2 + 3*x + 1",
#     "(x**2 - 4)/(x - 2)",
#     "(x**2 - 9)/(x**2 - 1)",
#     "log(1 + exp(x))",
#     "2/(1 + exp(-2*x)) - 1",
#     "asin(sin(x))",
#     "acos(cos(x))",
#     "atan(tan(x))",
#     "sinh(x)/cosh(x)",
#     "(exp(x) - exp(-x))/2",
#     "(exp(x) + exp(-x))/2",
#     "sin(x + pi/4)",
#     "cos(x - pi/4)",
#     "tan(x + pi/3)",
#     # "sin(x)**3",
#     # "cos(x)**3",
#     # "tan(x)**3",
#     "exp(sin(x))",
#     "exp(cos(x))",
#     "exp(tan(x))",
#     "log(sin(x))",
#     "log(cos(x))",
#     "log(tan(x))",
#     "sin(log(x))",
#     "cos(log(x))",
#     "tan(log(x))",
#     "exp(x) * cos(x)",
#     "exp(x) * sin(x)",
#     "log(x) * cos(x)",
#     "log(x) * sin(x)",
#     "x**2 + sin(x)",
#     "x**2 - cos(x)",
#     "sqrt(x) * sin(x)",
#     "sqrt(x) * cos(x)",
#     "(x**2 + 1)**0.5",
#     "1/(1 + x**2)",
#     "atan(x) + pi/2",
#     "acos(x) - pi",
#     "asin(1 - 2*x**2)",
#     "exp(-x) * sin(x)",
#     "exp(-x) * cos(x)",
#     # "(sin(x) + cos(x))**2",
#     # "(sin(x) - cos(x))**2",
#     "sin(x**2)",
#     "cos(x**2)",
#     "tan(x**2)",
#     "x * log(x)",
#     "x**x",
#     "(2*x) / (1 + x**2)",
#     "sin(x) / x",
#     "(1 - exp(-x)) / x",
#     "x**2 - 2*x + 1 / (x - 1)",
#     "log(x**2 + 1)",
#     "exp(-x**2) * cos(5*x)",
#     "(x**3 - 1) / (x**2 + x + 1)",
#     "sin(x) + cos(2*x) + tan(3*x)",
#     "exp(-x) * (sin(x) + cos(x))",
#     "log(Abs(x))",
#     "(x**2 - 4)**0.5",
#     "1 / (sin(x) + cos(x))",
#     "(sin(x)**2 - cos(x)**2)",
#     "atan(sqrt(x - 1))"
#     ]
#
#
# layout = html.Div([
#     create_basic_graph(50, value, -10, 10, -10, 10, "Epsilon-delta limits") for value in functions_list
# ])
#
#
