from dash import dcc, html
import dash_mantine_components as dmc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_graph(x_data: list, y_data: list, title, x_min=None, x_max=None, y_min=None, y_max=None):
    if x_min is None:
        x_min = min(x_data)
    if x_max is None:
        x_max = max(x_data)
    if y_min is None:
        y_min = min(y_data)
    if y_max is None:
        y_max = max(y_data)

    graph = px.line(x=x_data, y=y_data, title=title, line_shape='linear', range_x=[x_min, x_max],
                    range_y=[y_min, y_max])
    for x, y in zip(x_data, y_data):
        if y is None:
            graph.add_vline(x=x, line_dash="dash", line_color="black")
    return graph


def create_basic_graph(x_data: list, y_data: list, title, x_min=None, x_max=None, y_min=None, y_max=None):
    graph = create_graph(x_data, y_data, title, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)
    return dmc.Card(dcc.Graph(figure=graph))
