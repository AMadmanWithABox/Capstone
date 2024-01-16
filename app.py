from dash import Dash, html, dcc, callback, Input, Output, State

app = Dash(__name__)

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
                children=[html.Button(id="toggle-sidebar-btn", className="menu", children="PH", n_clicks=0)]
            )
        ])
])


@callback(
    Output('toggle-sidebar-btn', 'children'),
    Input('toggle-sidebar-btn', 'n_clicks')
)
def toggle_sidebar(clicks):
    if type(clicks) is None:
        return "closed"
    if clicks % 2 == 0:
        return "closed"
    return "open"


if __name__ == '__main__':
    app.run(debug=True)
