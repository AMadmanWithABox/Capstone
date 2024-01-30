import dash
from dash import html, Output, Input, callback, page_container, dcc
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
        className="link",
        inherit=True
    )


def create_header_link(icon, href, size=22, color="indigo"):
    return dmc.Anchor(
        dmc.ThemeIcon(
            DashIconify(
                icon=icon,
                width=size,
            ),
            variant="outline",
            radius=30,
            size=36,
            color=color,
        ),
        href=href,
        target="_blank",
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
                    align="center",
                    children=[
                        dmc.Col(
                            span="auto",
                            display="flex",
                            children=[
                                dmc.Group(
                                    align="center",
                                    style={"width": "100%"},
                                    children=[
                                        dmc.Burger(opened=False, id="burger-button", style={"z-index": 900000}),
                                        dmc.Title(
                                            children=[
                                                dmc.MediaQuery(
                                                    create_home_link('VisuCalc'),
                                                    smallerThan="lg",
                                                    styles={"display": "none"},
                                                ),
                                                dmc.MediaQuery(
                                                    create_home_link('VC'),
                                                    largerThan="lg",
                                                    styles={"display": "none"},
                                                )
                                            ],
                                            order=1,
                                            weight=100,
                                            inline=1,
                                            align='center'
                                        )
                                    ]),
                            ],
                            pt=12
                        ),
                        dmc.Col(
                            span="auto",
                            display="center",
                            children=[
                                dmc.Title(
                                    children='Home',
                                    order=1,
                                    inline=1,
                                    align='center',
                                    weight=400,
                                    style={"width": "100%", "text-align": "center"}
                                ),
                            ],
                            pt=12
                        ),
                        dmc.Col(
                            span="auto",
                            display="center",
                            style={"width": "100%"},
                            children=dmc.Group(
                                position="right",
                                align="center",
                                style={"width": "100%"},
                                children=[
                                    create_header_link(
                                        "radix-icons:github-logo",
                                        "https://github.com/AMadmanWithABox/Capstone",
                                    ),
                                ]),
                            pt="12"
                        ),
                    ]
                )
            )
        ]
    )


def create_sidebar():
    pages = dash.page_registry.values()
    level_1_tags = list()
    level_2_tags = list()
    for page in pages:
        page_lst = page["path"].split("/")
        if len(page_lst) > 1 and page_lst[1] not in level_1_tags:
            level_1_tags.append(page_lst[1])
        if len(page_lst) > 2 and page_lst[2] not in level_2_tags:
            level_2_tags.append(page_lst[2])

    return html.Div(
        children=[
            dmc.Drawer(
                size=300,
                withCloseButton=False,
                closeOnClickOutside=False,
                closeOnEscape=False,
                id="sidebar-drawer",
                withOverlay=False,
                children=[
                    dmc.NavLink(label="Home", href="/", icon=DashIconify(icon="bi:house-door-fill"))
                ].__add__([
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
                ])
            ),
        ])


def create_appshell():
    return dmc.MantineProvider(
        dmc.MantineProvider(
            inherit=True,
            children=[
                dmc.NotificationsProvider(
                    [
                        create_header(),
                        create_sidebar(),
                        html.Div(
                            dmc.Container(size="80%", pt=90, children=page_container),
                            id="wrapper",
                        ),
                    ]
                )
            ]
        ),
        theme={"colorScheme": "dark"},
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )


@callback(
    Output("sidebar-drawer", "opened"),
    Input("burger-button", "opened"),
    config_prevent_initial_callbacks=True,
)
def open_sb(opened):
    return opened

