from dash import Dash, html, dcc, callback, Input, Output, State

app = Dash(__name__)

app.layout = html.Div(id="default-page", children=[
    html.Div(id="title-bar", children=[
        html.H1(id="app-name", children=dcc.Link('VisuCalc', href='/')),
        html.H1(id="page-title", children='Home'),
    ]),
])

if __name__ == '__main__':
    app.run(debug=True)
