import dash
from dash import html

dash.register_page(__name__, path='/calculus/limits')

layout = html.Div([
    html.H1('You reached the limits page')
])