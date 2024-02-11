import decimal

import dash
from sympy import *
from lib.math_tools.functional import find_horizontal_asymptote
import numpy as np
from dash import html, dcc
from lib.templates.basic_graph_component import create_basic_graph

dash.register_page(__name__, path='/calculus/limits/epsilon-delta', name='Epsilon-delta limits')

def testing():
    x = symbols('x')
    expr = (3*x**2 + 2*x + 1) / (x**2 + 5*x + 2)
    denominator = denom(expr)
    print(denominator)
    solution = solve(denominator, x)
    for s in solution:
        print(s.round(2))
    print(solve(denominator, x))



def create_page():
    testing()
    expr = "(3*x**2 + 2*x + 1) / (x**2 + 5*x + 2)"
    x_range = 50

    return create_basic_graph(x_range, expr, title="Epsilon-delta limits", x_min=-10, x_max=10, y_min=-10, y_max=10)


layout = html.Div([
    dcc.Location(id='url'),
    create_page()
])
