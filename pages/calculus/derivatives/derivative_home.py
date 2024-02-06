import dash
from dash import html, dcc

dash.register_page(__name__, path='/calculus/derivatives', name="Derivatives", order=3)

layout = html.Div([
    dcc.Location(id='url'),
    html.H1('You reached the derivatives page')
])