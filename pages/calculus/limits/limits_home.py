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
When dealing with limit functions we may also see things like $x\\to a^{-}$. 
This means we want the limit as $x$ approaches $a$ from the left, or from $x$ values less than $a$.
$f(x) = \\frac1x$ describes the function we are looking at.
$$

$$

''', mathjax=True, dedent=False)

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
