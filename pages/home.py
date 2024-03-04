import dash
from dash import html, callback, Output, Input, dcc, State
import dash_mantine_components as dmc

dash.register_page(__name__, path='/')


def create_hero_section():
    return dmc.Stack(
        className="hero-section",
        spacing="xl",
        children=[dmc.Card(
            className="hero-headline-card",
            radius="lg",
            children=[
                dmc.Title(
                    "Visualize Calculus like never before",
                    className="hero-headline",
                    weight=300,
                ),
            ]
        ),
            dmc.Card(
                className="hero-subheadline-card",
                radius="lg",
                style={
                    "height": "fit-content",
                    "width": "100%",
                    "textAlign": "center",
                },
                children=[
                    dmc.Stack(
                        children=[
                            dmc.Title(
                                "Interactive graphs and real-time calculations to enhance your learning experience",
                                weight=500,
                            ),
                            dmc.Group(
                                position="center",
                                spacing="lg",
                                grow=True,
                                children=[
                                    dmc.Button(
                                        "Get Started",
                                        color="blue",
                                        id="get-started-button",
                                        variant="outline",
                                    ),
                                    dmc.Button(
                                        "Learn More",
                                        color="blue",
                                        id="learn-more-button",
                                        variant="outline",
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )


def create_get_started_section():
    return (
        dmc.Container(
            dmc.Card(
                className="sub-section-card-right",
                radius="lg",
                children=[
                    dmc.Title(
                        "To get started, select a topic from the sidebar",
                        weight=300,

                    ),
                ]
            ),
            className="sub-section",
        ))


def create_learn_more_section():
    return (
        dmc.Container(
            dmc.Card(
                radius="lg",
                className="sub-section-card",
                children=[
                    dmc.Title("Learn More",
                              weight=300),
                    dmc.Text("This is a test")
                ]
            ),
            className="sub-section",
        ))


def create_page_content():
    return dmc.ScrollArea(
        offsetScrollbars=True,
        type="scroll",
        className="page-content",
        styles={
            "root"
            "height": "87vh",
            "scroll-snap-type": "y mandatory",
        },
        children=[
            html.Section(
                create_hero_section(),
                style={"scroll-snap-align": "start"},
            ),
            html.Section(
                create_get_started_section(),
                id="get-started-section",
                style={"scroll-snap-align": "start"},
            ),
            html.Section(
                create_learn_more_section(),
                id="learn-more-section",
                style={"scroll-snap-align": "start"},
            ),
        ]
    )


@callback(
    [Output("burger-button", "opened"), Output("url", "href", allow_duplicate=True)],
    Input("get-started-button", "n_clicks"),
    State("url", "pathname"),
    config_prevent_initial_callbacks=True,
)
def on_get_started_button(n, path):
    if n is None:
        return
    return True, f"{path}#get-started-section"


@callback(
    Output("url", "href", allow_duplicate=True),
    Input("learn-more-button", "n_clicks"),
    State("url", "pathname"),
    config_prevent_initial_callbacks=True,
)
def on_learn_more_button(n, path):
    if n is None:
        return
    return f"{path}#learn-more-section"


layout = [dcc.Location(id="url"), create_page_content()]
