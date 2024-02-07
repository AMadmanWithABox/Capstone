from dash import dcc, html
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd


def create_graph(x_min, x_max, y_min, y_max, title, x_label, y_label, data):
    df = pd.DataFrame(data)
    graph = px.line(df, x='x', y='f(x)', title=title, line_shape='linear', range_x=[x_min, x_max], range_y=[y_min, y_max])

    return graph


def create_basic_graph(x_min, x_max, y_min, y_max, title, x_label, y_label, data, details=None):
    graph = create_graph(x_min, x_max, y_min, y_max, title, x_label, y_label, data)
    return dmc.Card(dcc.Graph(figure=graph))
