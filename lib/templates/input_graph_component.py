from lib.templates.basic_graph_component import create_basic_graph
import dash_mantine_components as dmc


def create_input_graph(inputs: list, x_range: int, expr_str, x_min=None, x_max=None, y_min=None, y_max=None,
                                 title=None):
    input_graph_layout = dmc.Group(children=[
        create_basic_graph(x_range, expr_str, x_min, x_max, y_min, y_max, title),
        dmc.RadioGroup(children=[
            inputs
        ]),
    ],
    )
    return input_graph_layout
