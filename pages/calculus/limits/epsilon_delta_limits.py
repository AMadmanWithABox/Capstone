import dash
from sympy import *
from lib.math_tools.functional import find_horizontal_asymptote
import numpy as np
from dash import html, dcc
from lib.templates.basic_graph_component import create_basic_graph

dash.register_page(__name__, path='/calculus/limits/epsilon-delta', name='Epsilon-delta limits')


def create_page():
    x = symbols('x')

    expr = 1/x

    f = lambdify(x, expr)
    x_scale = 100
    domain = np.arange(-x_scale, x_scale, 0.1)
    y = f(domain)
    ha = find_horizontal_asymptote(expr, [x])
    print(ha)

    return create_basic_graph(x, y, "Epsilon-delta limits")


layout = html.Div([
    dcc.Location(id='url'),
    create_page()
])
