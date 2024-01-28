import dash
from dash import html

dash.register_page(__name__, path='/calculus', name='Calculus', order=1)

layout = html.Div([
    html.H1('You reached the calculus page')
])