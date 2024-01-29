import dash
from dash import html, Output, Input, callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify


def get_icon(icon):
    return DashIconify(icon=icon, height=16)


def create_home_link(label):
    """
    Creates a hyperlink for the home page
    :param label: The text to display
    :return: A hyperlink using the dmc Anchor component
    """
    return dmc.Anchor(
        label,
        href="/",
        underline=False,
    )


def create_header():
    return dmc.Header(
        height=70,
        fixed=True,
        px=25,
        children=[
            dmc.Stack(
                justify="center",
                style={"height": 70},
                children=dmc.Grid(
                    children=[
                        dmc.Col(
                            display="flex",
                            children=[
                                html.H1(
                                    create_home_link('VisuCalc')
                                )
                            ],
                            span="content",
                            pt=12
                        ),
                        dmc.Col(
                            span="auto",
                            children=dmc.Group(
                                position="right",
                                spacing="xl",
                                children=[
                                    html.H1(
                                        children='Home',
                                    ),
                                    sidebar(),
                                ])
                        ),
                    ]
                )
            )
        ]
    )


def sidebar():
    pages = dash.page_registry.values()
    level_1_tags = list()
    level_2_tags = list()
    for page in pages:
        page_lst = page["path"].split("/")
        if len(page_lst) > 1 and page_lst[1] not in level_1_tags:
            level_1_tags.append(page_lst[1])
        if len(page_lst) > 2 and page_lst[2] not in level_2_tags:
            level_2_tags.append(page_lst[2])

    return html.Div(children=[html.Div(
        dmc.ActionIcon(
            DashIconify(
                icon="charm:menu-hamburger",
                width=30
            ),
            id="burger-button",
            size="lg",
            className="burger-button",
            mr="10px",
            mt="10px",
            variant="filled",
        )
    ),
        dmc.Drawer(
            id="sidebar-drawer",
            children=[
                dmc.NavLink(label="Home", href="/", icon=DashIconify(icon="bi:house-door-fill"))].__add__([
                dmc.NavLink(
                    label=dash.page_registry.get(f"pages.{sub1}.{sub1}-home").get('name'),
                    href=f"/{sub1}",
                    children=[
                        dmc.NavLink(
                            label=dash.page_registry.get(f"pages.{sub1}.{sub2}.{sub2}-home").get('name'),
                            href=f"/{sub1}/{sub2}",
                            children=[
                                dmc.NavLink(
                                    label=page["name"],
                                    href=page["path"],
                                    active="exact"
                                )
                                for page in pages
                                if
                                page["path"].startswith(f"/{sub1}/{sub2}") and page["path"] != f"/{sub1}/{sub2}"
                            ])
                        for sub2 in level_2_tags
                    ])
                for sub1 in level_1_tags
                if sub1 != ""

            ])),

    ])


@callback(
    Output("sidebar-drawer", "opened"),
    Input("burger-button", "n_clicks"),
    config_prevent_initial_callbacks=True,
)
def open(n_clicks):
    return True
