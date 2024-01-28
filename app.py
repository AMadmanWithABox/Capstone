from lib.templates.side_bar import sidebar
import dash
from dash import Dash, html, dcc
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.MINTY])

app.layout = html.Div(className="default-page", children=[
    html.Div(
        className="header",
        children=[
            html.Div(
                className="app-header",
                children=[
                    html.H1(children=dcc.Link('VisuCalc', href='/', className="app-header--name")),
                    html.H1(id="page-title", children='Home', className="app-header--title"),
                    html.Div(id="empty")
                ]
            )
        ]),
    html.Div(
        className="main-content",
        children=[
            sidebar(),
            dash.page_container
        ]
    ),
])

if __name__ == '__main__':
    app.run(debug=True)
