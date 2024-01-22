import dash
from dash import html

dash.register_page(__name__, path='/calculus/sequences-and-series')

layout = html.Div([
    html.H1('You reached the sequences and series page')
])