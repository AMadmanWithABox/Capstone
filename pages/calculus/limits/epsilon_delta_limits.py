import dash
import numpy as np
from dash import html, dcc
from lib.templates.basic_graph_component import create_basic_graph

dash.register_page(__name__, path='/calculus/limits/epsilon-delta', name='Epsilon-delta limits')


def create_page():
    x = np.arange(-10, 10, step=0.01)
    y = 1/x

    return create_basic_graph(-10, 10, -10, 10, 'Epsilon-delta limits', 'x', 'f(x)', {
        'x': x,
        'f(x)': y,
    }, details='Under construction...')


layout = html.Div([
    dcc.Location(id='url'),
    create_page()
])
