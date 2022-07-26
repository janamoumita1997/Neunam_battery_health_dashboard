from dash import html
from navbar import create_navbar
from bat_5329 import cur_vs_time, vol_vs_time, cap_vs_time, tmp_vs_time
nav = create_navbar()

cur_time= cur_vs_time()

vol_time= vol_vs_time()

cap_time= cap_vs_time()

temp_time= tmp_vs_time()

header = html.H3('Stats-Battery-5329!')


def create_page_3():
    layout = html.Div([
        nav,
        header,
        cur_time,
        vol_time,
        cap_time,
        temp_time
    ])
    return layout
