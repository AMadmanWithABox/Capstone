import dash
import dash_mantine_components as dmc
from dash import html, dcc, Input, Output, callback
from sympy import *

from lib.templates.basic_graph_component import create_basic_graph

dash.register_page(__name__, path='/calculus/limits', name='Limits', order=2)

expressions = [
    ["Simple Rational", "1 / x"],
    ["Complex Rational", "(x**2 - 9)/(x**2 - 1)"],
    ["Exponential", "exp(x)"],
    ["Logarithm", "log(x, 3)"],
    ["Trigonometric", "tan(x)"],
]

# def create_page():
#     # testing()
#     # functions_list = [
#     #     "x**2",
#     #     "x**3 - 3*x**2 + 2",
#     #     "1/x",
#     #     "sqrt(x)",
#     #     "exp(x)",
#     #     "log(x, 3)",
#     #     "sin(x)",
#     #     "cos(x)",
#     #     "tan(x)",
#     #     "asin(x)",
#     #     "acos(x)",
#     #     "atan(x)",
#     #     "sinh(x)",
#     #     "cosh(x)",
#     #     "tanh(x)",
#     #     "x**2 + 2*x + 1",
#     #     "x**4 - 4*x**3 + 6*x**2 - 4*x + 1",
#     #     "(x**2 - 1)/(x - 1)",
#     #     "2**x",
#     #     "2**-x",
#     #     "log(x)",
#     #     "Abs(x)",
#     #     "ceiling(x)",
#     #     "floor(x)",
#     #     "x % 2",
#     #     "x * sin(x)",
#     #     "exp(-x**2)",
#     #     "1/(1 + exp(-x))",
#     #     "sin(x)**2 + cos(x)**2",
#     #     "tan(x)**2 + 1",
#     #     "sin(2*x)",
#     #     "cos(2*x)",
#     #     "sin(x)**2",
#     #     "cos(x)**2",
#     #     "(1 - cos(2*x))/2",
#     #     "(1 + cos(2*x))/2",
#     #     "1/cos(x)",
#     #     "1/sin(x)",
#     #     "1/tan(x)",
#     #     "sin(x)/cos(x)",
#     #     "x**3 + 3*x**2 + 3*x + 1",
#     #     "(x**2 - 4)/(x - 2)",
#     #     "(x**2 - 9)/(x**2 - 1)",
#     #     "log(1 + exp(x))",
#     #     "2/(1 + exp(-2*x)) - 1",
#     #     "asin(sin(x))",
#     #     "acos(cos(x))",
#     #     "atan(tan(x))",
#     #     "sinh(x)/cosh(x)",
#     #     "(exp(x) - exp(-x))/2",
#     #     "(exp(x) + exp(-x))/2",
#     #     "sin(x + pi/4)",
#     #     "cos(x - pi/4)",
#     #     "tan(x + pi/3)",
#     #     # "sin(x)**3",
#     #     # "cos(x)**3",
#     #     # "tan(x)**3",
#     #     "exp(sin(x))",
#     #     "exp(cos(x))",
#     #     "exp(tan(x))",
#     #     "log(sin(x))",
#     #     "log(cos(x))",
#     #     "log(tan(x))",
#     #     "sin(log(x))",
#     #     "cos(log(x))",
#     #     "tan(log(x))",
#     #     "exp(x) * cos(x)",
#     #     "exp(x) * sin(x)",
#     #     "log(x) * cos(x)",
#     #     "log(x) * sin(x)",
#     #     "x**2 + sin(x)",
#     #     "x**2 - cos(x)",
#     #     "sqrt(x) * sin(x)",
#     #     "sqrt(x) * cos(x)",
#     #     "(x**2 + 1)**0.5",
#     #     "1/(1 + x**2)",
#     #     "atan(x) + pi/2",
#     #     "acos(x) - pi",
#     #     "asin(1 - 2*x**2)",
#     #     "exp(-x) * sin(x)",
#     #     "exp(-x) * cos(x)",
#     #     # "(sin(x) + cos(x))**2",
#     #     # "(sin(x) - cos(x))**2",
#     #     "sin(x**2)",
#     #     "cos(x**2)",
#     #     "tan(x**2)",
#     #     "x * log(x)",
#     #     "x**x",
#     #     "(2*x) / (1 + x**2)",
#     #     "sin(x) / x",
#     #     "(1 - exp(-x)) / x",
#     #     "x**2 - 2*x + 1 / (x - 1)",
#     #     "log(x**2 + 1)",
#     #     "exp(-x**2) * cos(5*x)",
#     #     "(x**3 - 1) / (x**2 + x + 1)",
#     #     "sin(x) + cos(2*x) + tan(3*x)",
#     #     "exp(-x) * (sin(x) + cos(x))",
#     #     "log(Abs(x))",
#     #     "(x**2 - 4)**0.5",
#     #     "1 / (sin(x) + cos(x))",
#     #     "(sin(x)**2 - cos(x)**2)",
#     #     "atan(sqrt(x - 1))"
#     # ]
#
#     graph_list = html.Div(id="graph-list")
#     return graph_list
description = dcc.Markdown('''
Limits are the value a function approaches as $x$ approaches a specific value. 
If you understand the concept of a value 'approaching' then you understand what a limit is. 
Let's examine a limit function definition:
$$
\\lim_{x\\to \\infty} f(x) = \\frac1x
$$
In this function there are a few different parts. 
$\\lim$ is what tells us we are looking at a Limit function.
$x\\to \\infty$ defines what $x$ approaches. In this case $x$ is approaching $\\infty$.
When dealing with limit functions we may also see things like $x\\to 0^{-}$. 
This means we want the limit as $x$ approaches $0$ from the left, or from $x$ values less than $0$.
$f(x) = \\frac1x$ describes the function we are looking at.

''', mathjax=True)
layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id="graph-list"),
    dmc.Stack([
        dmc.RadioGroup(
            [dmc.Radio(l, value=v) for l, v in expressions],
            id="radio-group",
            value="1 / x",
            label="Select a function to graph",
            size="lg",
            mt=10
        ),
        dmc.Text(description, id="radio-output")
    ])
])


@callback(
    Output("graph-list", "children"),
    Input("radio-group", "value")
)
def select_graph(value):
    return create_basic_graph(50, value, -10, 10, -10, 10, "Limits")
