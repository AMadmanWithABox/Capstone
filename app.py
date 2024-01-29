from lib.templates.appshell import sidebar, create_header
import dash
from dash import Dash, html, dcc
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(className="default-page", children=[
    html.Div(
        children=[create_header()]),
    html.Div(
        children=[
            dash.page_container
        ]
    ),
])

if __name__ == '__main__':
    app.run(debug=True)
