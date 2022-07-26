from dash import html
from navbar import create_navbar, create_pie_chart #, d_plot
import plotly.express as px
import dash_html_components as html



nav = create_navbar()
fig2, fig3=create_pie_chart()


header = html.H3('Welcome to Battery-health-Stats!')


def create_page_home():
    layout = html.Div([
        nav,
        header,
        fig2,
        fig3
        
        
    ])


    return layout
