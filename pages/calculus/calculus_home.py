import dash
from dash_iconify import DashIconify
import dash_mantine_components as dmc
from dash import html, dcc

dash.register_page(__name__, path='/calculus', name='Calculus', order=1)

layout = html.Div([
    dcc.Location(id='url'),
    dmc.Stack(
        children=[
            dmc.Blockquote(
                "Calculus is the most powerful weapon of thought yet devised by the wit of man.",
                cite="~ Wallace B. Smith"
            ),
            dmc.Card(
                children=[
                    dmc.CardSection(
                        dmc.Title("What is Calculus?")
                    ),
                    dmc.Stack(
                        children=[
                            dmc.Text(
                                children=[
                                    "According to Seifedine Kadry in the book ",
                                    dmc.Anchor(
                                        children=["Mathematical Formulas for Industrial and Mechancial Engineering"],
                                        href="https://www.sciencedirect.com/book/9780750655446/mathematics-for"
                                             "-engineers-and"
                                             "-technologists",
                                        inherit=True,
                                        underline=False
                                    ),
                                    ', "Calculus is the mathematical study of change, in the same way that geometry '
                                    'is the study of shape and algebra is the study of operations and their '
                                    'application to solving equations." Some of the core topics discussed in calculus '
                                    'are:'
                                ]),
                            dmc.List([
                                dmc.ListItem(
                                    [dmc.Anchor("Limits", href="/calculus/limits", underline=False),
                                     ": The value of a function as it approaches an x value."],
                                    icon=dmc.ThemeIcon(DashIconify(icon="oui:kql-function"), variant="light")
                                ),
                                dmc.ListItem(
                                    [dmc.Anchor("Derivatives", href="/calculus/derivatives", underline=False),
                                     ": A fundamental tool that measures how sensitive a function's output "
                                     "changes in relation to it's input."],
                                    icon=dmc.ThemeIcon(DashIconify(icon="mdi:graph-sankey"), variant="light")
                                ),
                                dmc.ListItem(
                                    [dmc.Anchor("Integration", href="/calculus/integration", underline=False),
                                     ": Another fundamental tool for finding the area under a curve of a function."],
                                    icon=dmc.ThemeIcon(DashIconify(icon="tabler:math-integral-x"), variant="light")
                                ),
                                dmc.ListItem(
                                    [dmc.Anchor("Sequences and series",
                                                href="/calculus/sequences-and-series",
                                                underline=False),
                                     ": A sequence is a list of numbers arranged in a specific "
                                     "pattern, while a series is the sum of a sequence."],
                                    icon=dmc.ThemeIcon(DashIconify(icon="streamline:steps-number"), variant="light")
                                ),
                                dmc.ListItem(
                                    [dmc.Anchor("Multivariable calculus",
                                                href="/calculus/multivariable-calculus",
                                                underline=False),
                                     ": A subset of calculus that studies functions with two or "
                                     "more variables"],
                                    icon=dmc.ThemeIcon(DashIconify(icon="tabler:math-xy"), variant="light")
                                )
                            ],
                                withPadding=True,
                                spacing='md'
                            ),
                            dmc.Text("Click on any of the links above to learn more about the listed topic!")
                        ])

                ]
            )
        ]
    )
])
