import dash
from dash import html

dash.register_page(__name__, path='/calculus/derivatives', name="Derivatives")

layout = html.Div([
    html.H1('You reached the derivatives page')
])