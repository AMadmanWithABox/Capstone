import dash
from dash import html, dcc
from lib.templates.basic_graph_component import create_basic_graph

dash.register_page(__name__, path='/calculus/limits/epsilon-delta', name='Epsilon-delta limits')

layout = html.Div([
    dcc.Location(id='url'),
    create_basic_graph(-10, 10, -10, 10, 'Epsilon-delta limits', 'x', 'f(x)', {
        'x': [-10, 10],
        'f(x)': [-10, 10],
    }, details='Under construction...'),
])
