from re import X
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


#import data

data_details = pd.read_excel("5308.xls",sheet_name="Detail_67_3_5")
data_temp=pd.read_excel("5308.xls",sheet_name="DetailTemp_67_3_5")
# data = data.query("type == 'conventional'")
# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
# data.sort_values("Date", inplace=True)


#time vs current

def cur_vs_time():
    x=html.Div(
    children=[
        html.H1(
            children="Current Vs. Time",
        ),])
    x=dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data_details["Absolute Time"],
                        "y": data_details["Cur(mA)"],
                        "type": "line",
                    },
                ],
                "layout": {"title": "Current Vs. Time "},
            },
        )
    return x


#voltage_vs_time

def vol_vs_time():
    x=html.Div(
    children=[
        html.H1(
            children="Current Vs. Time",
        ),])
    x=dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data_details["Absolute Time"],
                        "y": data_details["Voltage(V)"],
                        "type": "line",
                    },
                ],
                "layout": {"title": "Voltage(V) Vs. Time "},
            },
        )
    return x


#capacity_vs_time

def cap_vs_time():
    x=html.Div(
    children=[
        html.H1(
            children="Current Vs. Time",
        ),])
    x=dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data_details["Absolute Time"],
                        "y": data_details["CapaCity(mAh)"],
                        "type": "line",
                    },
                ],
                "layout": {"title": "CapaCity(mAh) Vs. Time "},
            },
        )
    return x

#temp_vs_time

def tmp_vs_time():
    x=html.Div(
    children=[
        html.H1(
            children="Current Vs. Time",
        ),])
    x=dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data_details["Absolute Time"],
                        "y": data_temp["Auxiliary channel TU1 T(°C)"],
                        "type": "line",
                    },
                ],
                "layout": {"title": "Auxiliary channel TU1 T(°C) Vs. Time "},
            },
        )
    return x
