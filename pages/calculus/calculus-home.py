import dash
from dash import html, dcc

dash.register_page(__name__, path='/calculus', name='Calculus', order=1)

layout = html.Div([
    dcc.Location(id='url'),
    html.H1('You reached the calculus page')
])