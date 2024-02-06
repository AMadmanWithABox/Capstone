import dash
from dash import html, dcc

dash.register_page(__name__, path='/calculus/limits', name='Limits', order=2)

layout = html.Div([
    dcc.Location(id='url'),
    html.H1('You reached the limits page')
])