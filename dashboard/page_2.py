from dash import html
from navbar import create_navbar
from bat_5308 import cur_vs_time,vol_vs_time ,cap_vs_time, tmp_vs_time

nav = create_navbar()

cur_time=cur_vs_time()

vo_time =vol_vs_time()

cap_time=cap_vs_time()

tmp_time =tmp_vs_time()

header = html.H3('Welcome to cell-5308!')



def create_page_2():
    layout = html.Div([
        nav,
        header,
        cur_time,
        vo_time,
        cap_time,
        tmp_time
    ])
    return layout
