import json
import pathlib

import dash
from dash import Dash, html, dcc, callback, Input, Output, State

app = Dash(__name__, use_pages=True)


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
        id="sidebar",
        className="sidebar",
        children=[
            html.Div(
                className="sidebar-content",
                children=[],
            ),
            html.Div(
                className="sidebar-margin",
                children=[
                    html.Button(
                        id="toggle-sidebar-btn",
                        className="toggle-sidebar-btn",
                        children=">&#9776;",
                        n_clicks=0
                    )
                ]
            )
        ]),
    html.Div([
        html.H1('Multi-page app with Dash Pages'),
        html.Div([
            html.Div(
                dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
            ) for page in dash.page_registry.values()
        ]),
        dash.page_container
    ])
])


@callback(
    Output('toggle-sidebar-btn', 'children'),
    Input('toggle-sidebar-btn', 'n_clicks')
)
def toggle_sidebar(clicks):
    if type(clicks) is None:
        return ">&#9776;"
    if clicks % 2 == 0:
        return ">&#9776;"
    return "X"


if __name__ == '__main__':
    app.run(debug=True)
