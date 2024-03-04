import dash
import dash_mantine_components as dmc
from sympy import *
from dash import html, dcc, callback, Output, Input
from lib.templates.basic_graph_component import create_basic_graph

dash.register_page(__name__, path='/calculus/limits/epsilon-delta', name='Epsilon-delta limits', order=1)

layout = html.Div([
    dcc.Location(id='url'),
    html.H1('You reached the Epsilon-delta limits page')
])