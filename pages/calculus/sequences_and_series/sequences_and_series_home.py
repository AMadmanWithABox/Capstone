import dash
from dash import html, dcc

dash.register_page(__name__, path='/calculus/sequences_and_series', name='Sequences and Series', order=5)

layout = html.Div([
    dcc.Location(id='url'),
    html.H1('You reached the sequences and series page')
])