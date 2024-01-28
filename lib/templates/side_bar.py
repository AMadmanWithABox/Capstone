import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify


def get_icon(icon):
    return DashIconify(icon=icon, height=16)


def sidebar():
    pages = dash.page_registry.values()
    print(pages)
    level_1_tags = list()
    level_2_tags = list()
    for page in pages:
        page_lst = page["path"].split("/")
        if len(page_lst) > 1 and page_lst[1] not in level_1_tags:
            level_1_tags.append(page_lst[1])
        if len(page_lst) > 2 and page_lst[2] not in level_2_tags:
            level_2_tags.append(page_lst[2])

    return html.Div(children=[
        html.Div(className="sidebar-content",
             children=[dmc.NavLink(label="Home", href="/", icon=DashIconify(icon="bi:house-door-fill"))].__add__([
                 dmc.NavLink(label=dash.page_registry.get(f"pages.{sub1}.{sub1}-home").get('name'), href=f"/{sub1}", children=[

                     dmc.NavLink(label=dash.page_registry.get(f"pages.{sub1}.{sub2}.{sub2}-home").get('name'), href=f"/{sub1}/{sub2}", children=[
                         dmc.NavLink(
                             label=page["name"],
                             href=page["path"],
                             active="exact"
                         )
                         for page in pages
                         if page["path"].startswith(f"/{sub1}/{sub2}") and page["path"] != f"/{sub1}/{sub2}"
                     ])
                     for sub2 in level_2_tags
                 ])
                 for sub1 in level_1_tags
                 if sub1 != ""

             ])),
    ])
