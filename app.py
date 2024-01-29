from lib.templates.appshell import create_sidebar, create_header, create_appshell
import dash
from dash import Dash, html, dcc
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    update_title=None,
)

app.layout = create_appshell()
server = app.server

if __name__ == '__main__':
    app.run(debug=True)
