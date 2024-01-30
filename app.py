from lib.templates.appshell import create_sidebar, create_header, create_appshell
import dash
from dash import Dash, html, dcc
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
    "https://www.googletagmanager.com/gtag/js?id=G-4PJELX1C4W",
    "https://media.ethicalads.io/media/client/ethicalads.min.js",
]


app = Dash(
    __name__,
    use_pages=True,
    update_title=None,
    external_scripts=scripts,
)

app.layout = create_appshell()
server = app.server

if __name__ == '__main__':
    app.run(debug=True)
