import array
import numpy as np
from sympy import *
from dash import dcc, html
import dash_mantine_components as dmc
import plotly.graph_objects as go
from lib.math_tools.functional import find_horizontal_asymptote


def create_graph(x_range: int, expr_str, x_min=None, x_max=None, y_min=None, y_max=None, title=None):
    fig = go.Figure()
    x = symbols('x')
    expr = simplify(sympify(expr_str))
    f = lambdify(x, expr, modules=['numpy'])
    ha = find_horizontal_asymptote(expr, [x])
    va = solve(denom(expr), x)
    domain = np.arange(-x_range, x_range, float(0.01))
    domain = domain.round(2)
    rounded_va = [round(float(v), 2) for v in va]
    print(range(len(list(domain))))
    print(rounded_va[0])
    print(type(domain[0]))
    for i in range(len(list(domain))):
        for j in range(len(rounded_va)):
            if float(domain[i]) == rounded_va[j]:
                print('here')
                domain[i] = None



    y = f(domain)
    fig.add_trace(go.Scatter(x=domain, y=y, mode='lines', name=('$' + latex(expr) + '$')))
    if va is not None and len(va) > 0:
        for v in va:
            if v.is_real:
                v = float(v)
                fig.add_trace(
                    go.Scatter(
                        x=[v, v],
                        y=[y_min, y_max],
                        mode='lines',
                        name="Vertical Asymptote",
                        hoveron="fills",
                        line_dash="dash",
                        line_color="red"
                    )
                )

    if ha is not None and len(ha) > 0:
        for h in ha:
            fig.add_trace(
                go.Scatter(
                    x=[min(domain), max(domain)],
                    y=[h, h],
                    mode='lines',
                    name="Horizontal Asymptote",
                    hoveron="fills",
                    line_dash="dash",
                    line_color="green"
                )
            )
    fig.update_traces(mode='lines', hovertemplate=None)
    fig.update_layout(title=title, hovermode='closest',
                      legend={'font': {'size': 20}}
                      )
    if x_min is not None and x_max is not None:
        fig.update_xaxes(range=[x_min, x_max])
    if y_min is not None and y_max is not None:
        fig.update_yaxes(range=[y_min, y_max])
    return fig


def create_basic_graph(range, expr, x_min=None, x_max=None, y_min=None, y_max=None, title=None):
    graph = create_graph(range, expr, x_min, x_max, y_min, y_max, title)
    return dmc.Card(dcc.Graph(figure=graph, mathjax=True))
