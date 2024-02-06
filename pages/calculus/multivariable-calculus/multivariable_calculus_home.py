import dash
from dash import html, dcc

dash.register_page(__name__, path='/calculus/multivariable-calculus', name='Multivariable Calculus', order=6)

layout = html.Div([
    dcc.Location(id='url'),
    html.H1('You reached the multivariable calculus page')
])