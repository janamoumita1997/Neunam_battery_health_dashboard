from re import X
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go




def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Battery-5308", href='/page-2'),
                    dbc.DropdownMenuItem("Battery-5329", href='/page-3'),
                ],
            ),
         
        ],
        
        brand="Home",
        brand_href="/",
        sticky="top",
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar


data_5308 = pd.read_excel("5308.xls" ,sheet_name="Statis_67_3_5")
data_5308_discharge= (data_5308["Discharge_capacity(mAh)"]/3000)*100

data_5329 = pd.read_excel("5329.xls" ,sheet_name="Statis_67_3_1")
data_5329_discharge= (data_5329["Discharge_capacity(mAh)"]/3000)*100

def create_pie_chart():
    

    x= html.Div([dcc.Graph(figure={'data': [go.Pie(labels=data_5308["Status"],
                                                            values=data_5308_discharge,
                                                          
                                                            )],"layout": {"title": "Battery-Status-5308 "}})
                          ], className='col-xl-4')
    y=html.Div([dcc.Graph(figure={'data': [go.Pie(labels=data_5329["Status"],
                                                            values=data_5329_discharge,
                                                          
                                                            )],"layout": {"title": "Battery-Status-5329"}})
                          ], className='col-sm-4')
    return x ,y



# data_5308_cycle = pd.read_excel("5308.xls" ,sheet_name="Cycle_67_3_5")
# def d_plot():
#     x=html.Div(
#     children=[
#         html.H1(
#             children="Current Vs. Time",
#         ),])
#     x=dcc.Graph(
#             figure={
#                 "data": [
#                     {
#                         "x": data_5308_cycle["ToTal of Cycle"],
#                         "y": data_5308_cycle["Capacity of charge(mAh)"],
#                         "z": data_5308_cycle["Capacity of discharge(mAh)"],
#                         "type": "scatter_3d",
#                     },
#                 ],
#                 "layout": {"title": "Auxiliary channel TU1 T(°C) Vs. Time "},
#             },
#         )
#     return x



    # import plotly.express as px

    # df = px.data.tips() # replace with your own data source

    # fig = px.pie ( df, 
    #             values='day', 
    #             names='smoker',
    #             #title='Request Types'
    # )

    # fig.update_layout(
    #     paper_bgcolor = 'rgba(0,0,0,0)',
    #     margin={'l':0, 'r':0, 'b':0},
    #     font_color='white',
    #     font_size=18,
    #     hoverlabel={'bgcolor':'white', 'font_size':16, 'font_family':'Lato'}
    # )

    # return fig


    # line=(
    
    #     children=[
    #         html.H1(
    #             children="Avocado Analytics",
    #         ),
    #         html.P(
    #             children="Analyze the behavior of avocado prices"
    #             " and the number of avocados sold in the US"
    #             " between 2015 and 2018",
    #         ),
    #         dcc.Graph(
    #             figure={
    #                 "data": [
    #                     {
    #                         "x": data["Date"],
    #                         "y": data["AveragePrice"],
    #                         "type": "pie",
    #                     },
    #                 ],
    #                 "layout": {"title": "Average Price of Avocados"},
    #             },
    #         ),
    #         ]
    #         )
