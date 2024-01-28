import dash
from dash import html
import dash_bootstrap_components as dbc


def sidebar(pages):
    level_1_tags = list()
    level_2_tags = list()
    for page in pages:
        page_lst = page["path"].split("/")
        if len(page_lst) > 1 and page_lst[1] not in level_1_tags:
            level_1_tags.append(page_lst[1])
        if len(page_lst) > 2 and page_lst[2] not in level_2_tags:
            level_2_tags.append(page_lst[2])

    # the style arguments for the sidebar. We use position:fixed and a fixed width
    SIDEBAR_STYLE = {
        "position": "fixed",
        # "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
    }

    # the styles for the main content position it to the right of the sidebar and
    # add some padding.
    CONTENT_STYLE = {
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    }


    return html.Div(
        dbc.Accordion(start_collapsed=True, flush=True, children=[
            dbc.AccordionItem(title=sub1, children=[
                dbc.Accordion(start_collapsed=True, flush=True, children=[
                    dbc.AccordionItem(title=page["name"], children=[
                        dbc.NavLink(
                            html.Div(
                                page["name"],
                                className="ms-2"
                            ),
                            href=page["path"],
                            active="exact"
                        )]
                    )
                    for page in pages
                    if page["path"].startswith(f"/{sub1}/{sub2}")
                ])
                for sub2 in level_2_tags
            ])
            for sub1 in level_1_tags
            if sub1 != ""
        ],
            class_name="bg-light",
        ),
        style=SIDEBAR_STYLE,
    )
