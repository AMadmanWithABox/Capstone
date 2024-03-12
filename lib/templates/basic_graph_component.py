import numpy as np
from dash import dcc
from sympy import abc
import dash_mantine_components as dmc
import plotly.graph_objects as go
from lib.math_tools.functional import *
from lib.constants import ROUNDING


def create_graph(x_range: int, expr_str, x_min=None, x_max=None, y_min=None, y_max=None, title=None, is_derivative=False):
    warnings.filterwarnings("error")
    fig = go.Figure()
    x_not_real = symbols('x')
    expr = sympify(expr_str)
    # deriv = None
    # if not is_derivative:
    #     try:
    #         deriv = create_graph(x_range, diff(expr), x_min, x_max, y_min, y_max, title, True)
    #     except:
    #         pass
    print(f'function {expr_str} is {type(expr)} {expr}')
    f = lambdify(x, expr, modules=['numpy'])
    ha = find_horizontal_asymptote(expr, [x], x_range)
    va = find_vertical_asymptote(expr, x, x_range)
    domain = np.arange(-x_range, x_range, float(1)/10**ROUNDING)
    domain = domain.round(ROUNDING)
    oa = find_oblique_asymptote(expr)
    holes = find_holes(expr)

    if holes is not None:
        for hole in holes:
            if hole in va:
                va.remove(hole)

    if va is not None and len(va) > 0:
        rounded_va = [float(round(v, ROUNDING)) for v in va]
        for i in range(len(list(domain))):
            for j in range(len(rounded_va)):
                if round(float(domain[i]), ROUNDING) == round(float(rounded_va[j]), ROUNDING):
                    domain[i] = None

    if ha is not None and len(ha) > 0:
        rounded_ha = [float(round(h, ROUNDING)) for h in ha]
        for i in range(len(rounded_ha)):
            for j in range(len(rounded_ha)):
                try:
                    if round(float(rounded_ha[i]), ROUNDING) == round(float(rounded_ha[j]), ROUNDING) and i != j:
                        rounded_ha.pop(i)
                except IndexError as e:
                    continue
        ha = rounded_ha
    y = list()
    for i in range(len(domain)):
        try:
            y.append(f(domain[i]))
        except RuntimeWarning as w:
            y.append(None)
    fig.add_trace(
        go.Scatter(
            legendrank=1,
            showlegend=True,
            x=domain,
            y=y,
            mode='lines',
            name=('$' + latex(expr) + '$')
        )
    )
    if holes is not None and len(holes) > 0:
        for h in holes:
            fig.add_shape(
                type="circle",
                xref="x",
                yref="y",
                x0=h - (float(1) / 10**ROUNDING),
                y0=int(limit(expr, x_not_real, h, dir="+-")) - (float(1) / 10**ROUNDING),
                x1=h + (float(1) / 10**ROUNDING),
                y1=int(limit(expr, x_not_real, h, dir="+-")) + (float(1) / 10**ROUNDING),
                line_color="red",
                label={'text':f'Hole at x={h}'}
            )
    if oa is not None:
        oa = lambdify(x, oa, modules=['numpy'])
        oa_y = oa(domain)
        fig.add_trace(
            go.Scatter(
                x=domain,
                y=oa_y,
                mode='lines',
                name="Oblique Asymptote",
                line_color="blue",
                line_dash="dash"
            )
        )
    if va is not None and len(va) > 0:
        for v in va:
            if v is not None and not isinstance(v, complex):
                name = None
                showlegend = False
                if v == va[0]:
                    name = "Vertical Asymptote"
                    showlegend = True
                v = float(v)
                # noinspection PyTypeChecker
                fig.add_trace(
                    go.Scatter(
                        x=[v, v],
                        y=[min(domain), max(domain)],
                        mode='lines',
                        name=name,
                        hoveron="fills",
                        showlegend=showlegend,
                        line_dash="dash",
                        line_color="red"
                    )
                )

    if ha is not None and len(ha) > 0:
        for h in ha:
            # noinspection PyTypeChecker
            if h is not None and not isinstance(h, complex):
                name = None
                showlegend = False
                if h == ha[0]:
                    name = "Horizontal Asymptote"
                    showlegend = True
                h = float(h)
                # noinspection PyTypeChecker
                fig.add_trace(
                    go.Scatter(
                        y=[h, h],
                        x=[min(domain), max(domain)],
                        mode='lines',
                        name=name,
                        hoveron="fills",
                        showlegend=showlegend,
                        line_dash="dash",
                        line_color="green"
                    )
                )

    fig.update_traces(mode='lines', hovertemplate=None)
    fig.update_layout(
        title=title,
        hovermode='closest',
        legend={
            'font': {'size': 20}
        }
    )

    if x_min is not None and x_max is not None:
        fig.update_xaxes(range=[x_min, x_max])
    if y_min is not None and y_max is not None:
        fig.update_yaxes(range=[y_min, y_max])
    warnings.resetwarnings()
    # if deriv is not None:
    #     for data in deriv['data']:
    #         fig.add_trace(data)
    return fig


def create_basic_graph(x_range, expr, x_min=None, x_max=None, y_min=None, y_max=None, title=None):
    graph = create_graph(x_range, expr, x_min, x_max, y_min, y_max, title)
    return dmc.Card(dcc.Graph(figure=graph, mathjax=True, style={'height': '75vh'}), shadow="sm")
