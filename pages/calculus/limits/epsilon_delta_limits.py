import dash
from sympy import *
from dash import html, dcc
from lib.templates.basic_graph_component import create_basic_graph

dash.register_page(__name__, path='/calculus/limits/epsilon-delta', name='Epsilon-delta limits', order=1)


def testing():
    x = symbols('x')
    expr = (x**2 + 6*x + 9) / (x + 3)
    denominator = denom(expr)
    print(denominator)
    solution = solve(denominator, x)
    for s in solution:
        print(s.round(2))
    print(solve(denominator, x))


def create_page():
    # testing()
    functions_list = [
        "x**2",
        "x**3 - 3*x**2 + 2",
        "1/x",
        "sqrt(x)",
        "exp(x)",
        "log(x, 3)",
        "sin(x)",
        "cos(x)",
        "tan(x)",
        "asin(x)",
        "acos(x)",
        "atan(x)",
        "sinh(x)",
        "cosh(x)",
        "tanh(x)",
        "x**2 + 2*x + 1",
        "x**4 - 4*x**3 + 6*x**2 - 4*x + 1",
        "(x**2 - 1)/(x - 1)",
        "2**x",
        "2**-x",
        "log(x)",
        "Abs(x)",
        "ceiling(x)",
        "floor(x)",
        "x % 2",
        "x * sin(x)",
        "exp(-x**2)",
        "1/(1 + exp(-x))",
        "sin(x)**2 + cos(x)**2",
        "tan(x)**2 + 1",
        "sin(2*x)",
        "cos(2*x)",
        "sin(x)**2",
        "cos(x)**2",
        "(1 - cos(2*x))/2",
        "(1 + cos(2*x))/2",
        "1/cos(x)",
        "1/sin(x)",
        "1/tan(x)",
        "sin(x)/cos(x)",
        "x**3 + 3*x**2 + 3*x + 1",
        "(x**2 - 4)/(x - 2)",
        "(x**2 - 9)/(x**2 - 1)",
        "log(1 + exp(x))",
        "2/(1 + exp(-2*x)) - 1",
        "asin(sin(x))",
        "acos(cos(x))",
        "atan(tan(x))",
        "sinh(x)/cosh(x)",
        "(exp(x) - exp(-x))/2",
        "(exp(x) + exp(-x))/2",
        "sin(x + pi/4)",
        "cos(x - pi/4)",
        "tan(x + pi/3)",
        # "sin(x)**3",
        # "cos(x)**3",
        # "tan(x)**3",
        "exp(sin(x))",
        "exp(cos(x))",
        "exp(tan(x))",
        "log(sin(x))",
        "log(cos(x))",
        "log(tan(x))",
        "sin(log(x))",
        "cos(log(x))",
        "tan(log(x))",
        "exp(x) * cos(x)",
        "exp(x) * sin(x)",
        "log(x) * cos(x)",
        "log(x) * sin(x)",
        "x**2 + sin(x)",
        "x**2 - cos(x)",
        "sqrt(x) * sin(x)",
        "sqrt(x) * cos(x)",
        "(x**2 + 1)**0.5",
        "1/(1 + x**2)",
        "atan(x) + pi/2",
        "acos(x) - pi",
        "asin(1 - 2*x**2)",
        "exp(-x) * sin(x)",
        "exp(-x) * cos(x)",
        # "(sin(x) + cos(x))**2",
        # "(sin(x) - cos(x))**2",
        "sin(x**2)",
        "cos(x**2)",
        "tan(x**2)",
        "x * log(x)",
        "x**x",
        "(2*x) / (1 + x**2)",
        "sin(x) / x",
        "(1 - exp(-x)) / x",
        "x**2 - 2*x + 1 / (x - 1)",
        "log(x**2 + 1)",
        "exp(-x**2) * cos(5*x)",
        "(x**3 - 1) / (x**2 + x + 1)",
        "sin(x) + cos(2*x) + tan(3*x)",
        "exp(-x) * (sin(x) + cos(x))",
        "log(Abs(x))",
        "(x**2 - 4)**0.5",
        "1 / (sin(x) + cos(x))",
        "(sin(x)**2 - cos(x)**2)",
        "atan(sqrt(x - 1))"
    ]
    x_range = 50
    graph_list = html.Div([
        create_basic_graph(x_range, expr, title="Epsilon-delta limits", x_min=-10, x_max=10, y_min=-10, y_max=10) for expr in functions_list
    ])
    return graph_list


layout = html.Div([
    dcc.Location(id='url'),
    create_page()
])
