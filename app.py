import json
import pathlib
from lib.templates.side_bar import sidebar
import dash
from dash import Dash, html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])



# def sort_pages(pages):
    # for path in list(pages.mapping):
    #     path = str(path)
    #     path = path.split(".")
    #     print(path)
    #     sorted_pages = {
    #         "pages": {}
    #     }

        # return sorted_pages


app.layout = html.Div(id="default-page", children=[
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
        # id="sidebar",
        # className="sidebar",
        children=[sidebar(dash.page_registry.values())]
    ),
])


# @callback(
#     Output('toggle-sidebar-btn', 'children'),
#     Input('toggle-sidebar-btn', 'n_clicks')
# )
# def toggle_sidebar(clicks):
#     if type(clicks) is None:
#         return ">&#9776;"
#     if clicks % 2 == 0:
#         return ">&#9776;"
#     return "X"


if __name__ == '__main__':
    app.run(debug=True)
