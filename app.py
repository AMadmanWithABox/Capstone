from dash import Dash, html, dcc, callback, Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Hello World')
])

if __name__ == '__main__':
    app.run(debug=True)
