# for basic operations
from _plotly_utils.basevalidators import DashValidator
import numpy as np
import pandas as pd

# for visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# for interactive visualizations
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.offline as offline
offline.init_notebook_mode()
from plotly import tools
import plotly.figure_factory as ff
import plotly.express as px

from bubbly.bubbly import bubbleplot

import plotly.tools as tls
import squarify
from mpl_toolkits.basemap import Basemap
from numpy import DataSource, array
from matplotlib import cm
import dabl





#=======================================
#Geração de dados

# df = pd.read_csv('df_total_12_08_21.csv')
# df_states = df[(~df['estado'].isna()) & (df['codmun'].isna())]
# df_brasil = df[df['regiao'] == 'Brasil']
# df_states.to_csv('df_states.csv')
# df_brasil.to_csv('df_brasil.csv')
#=======================================



#=======================================
#Carregar dados




data = pd.read_csv('suicide_rates.csv')

data = data.sort_values(['year'], ascending = True)

print(data.shape)







# # Instância do DashBoard
# #---------------------------

app = DashValidator.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY]) #Aplicando o tema

                       

suicide = pd.DataFrame(DataSource.groupby(['country','year'])['suicides'].sum().reset_index())

count_max_sui=pd.DataFrame(suicide.groupby('country')['suicides'].sum().reset_index())

count = [ dict(
        type = 'choropleth',
        locations = count_max_sui['country'],
        locationmode='country names',
        z = count_max_sui['suicides'],
        text = count_max_sui['country'],
        colorscale = 'Cividis',
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
)]
layout = dict(
    title = 'Suicides happening across the Globe',
    geo = dict(
        showframe = True,
        showcoastlines = True,
        projection = dict(
            type = 'orthographic'
        )
    )
)
fig = dict( data=count, layout=layout )
iplot(fig, validate=False, filename='d3-world-map')


# # Layout
# #---------------------------

# app.layout = dbc.Container(
#     children=[
#         dbc.Row([
        
#             dbc.Col([

#                 html.Div([

#                     html.Img(id="logo", src=app.get_asset_url("logo_dark1.png"), height=50),
#                     html.H5("Evolução do COVID-19"),
#                     dbc.Button("BRASIL", color="primary", id="location-button", size="lg"),


#                 ], style={"background-color": "#1E1E1E", "margin": "-25px", "padding": "25px"}),
#                 html.P("Informe a data na qual deseja obter informações:", style={"margin-top": "40px"}),  
#                 html.Div(id="div-test", 
#                     children=[
#                     dcc.DatePickerSingle(
#                     id="date-picker",
#                     min_date_allowed=df_brasil["data"].min(),
#                     max_date_allowed=df_brasil["data"].max(),
#                     initial_visible_month=df_brasil["data"].min(),
#                     date= df_brasil["data"].max(),
#                     display_format="MMMM D, YYYY",
#                     style={"border": "0px solid black"} 
                
#                 )   
                
                
                        
#             ]),
        
#                 dbc.Row([       #Linha

#                     dbc.Col([       #Coluna

#                         dbc.Card([              #Primeiro card
#                             dbc.CardBody([
                        
#                         html.Span("Casos recuperados"),
#                         html.H3(style={"color": "#adfc92"}, id="casos-recuperados-text"),
#                         html.Span("Em acompanhamento"),
#                         html.H5(id="em-acompanhamento-text"),

#                     ])

#                 ], color="light", outline=True, style={"margin-top": "10px",
#                                         "box-shadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)",
#                                         "color": "#FFFFFF"})
#             ], md=4),

#             dbc.Col([       #Coluna

#                 dbc.Card([              #Primeiro card
#                     dbc.CardBody([
                        
#                         html.Span("Casos confirmados totais"),
#                         html.H3(style={"color": "#389fd6"}, id="casos-confirmados-text"),
#                         html.Span("Em acompanhamento"),
#                         html.H5(id="novos-casos-text"),

#                     ])

#                 ], color="light", outline=True, style={"margin-top": "10px",
#                                         "box-shadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)",
#                                         "color": "#FFFFFF"})
#             ], md=4),

#             dbc.Col([       #Coluna

#                 dbc.Card([              #Primeiro card
#                     dbc.CardBody([
                        
#                         html.Span("Óbitos confirmados"),
#                         html.H3(style={"color": "#DF2935"}, id="obitos-text"),
#                         html.Span("Em acompanhamento"),
#                         html.H5(id="obitos-na-data-text"),

#                     ])

#                 ], color="light", outline=True, style={"margin-top": "10px",
#                                         "box-shadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)",
#                                         "color": "#FFFFFF"})
#             ], md=4),


#         ]),

#             html.Div([
#                 html.P("Selecione o tipo de dado que deseja visualizar:", style={"margin-top": "25px"}),
#                 dcc.Dropdown(id="location-dropdown",
#                                 options=[{"label": j, "value": i} 
#                                     for i, j in select_columns.items()],
#                                 value = "casosNovos",
#                                 style={"margin-top": "10px"}),
#                 dcc.Graph(id="line-graph", figure=fig2, style={
#                             "background-color": "#242424",}),
#             ], id="teste")

            
#         ], md=5, style={"padding":"25px", "background-color": "#242424"}),

#         dbc.Col([

#             dcc.Loading(id="loading-1", type="default", 
#             children=[
#                 dcc.Graph(id="choropleth-map", figure=fig, style={"height": "100vh", "margin-right": "10px"})],
#                 ),
            
#             ], md=7),
#         ], no_gutters=True)
#     ], fluid=True
# )

# #date = "2021-4-15"
# #location = "RJ"
# #=======================
# #Interatividade

# @app.callback(

#    [
#         Output("casos-recuperados-text", "children"),
#         Output("em-acompanhamento-text", "children"),
#         Output("casos-confirmados-text", "children"),
#         Output("novos-casos-text", "children"),
#         Output("obitos-text", "children"),
#         Output("obitos-na-data-text", "children"),
#     ], [Input("date-picker", "date"), Input("location-button", "children")]
    
# )

# def display_status(date, location):

#     if location == "BRASIL":
#         df_data_on_date = df_brasil[df_brasil["data"] == date]
#     else:
#         df_data_on_date = df_states[(df_states["estado"] == location) & (df_states["data"] == date)]
    
#     recuperados_novos = "-" if df_data_on_date["Recuperadosnovos"].isna().values[0] else f'{int(df_data_on_date["Recuperadosnovos"].values[0]):,}'.replace(",", ".") 
#     acompanhamentos_novos = "-" if df_data_on_date["emAcompanhamentoNovos"].isna().values[0]  else f'{int(df_data_on_date["emAcompanhamentoNovos"].values[0]):,}'.replace(",", ".") 
#     casos_acumulados = "-" if df_data_on_date["casosAcumulado"].isna().values[0]  else f'{int(df_data_on_date["casosAcumulado"].values[0]):,}'.replace(",", ".") 
#     casos_novos = "-" if df_data_on_date["casosNovos"].isna().values[0]  else f'{int(df_data_on_date["casosNovos"].values[0]):,}'.replace(",", ".") 
#     obitos_acumulado = "-" if df_data_on_date["obitosAcumulado"].isna().values[0]  else f'{int(df_data_on_date["obitosAcumulado"].values[0]):,}'.replace(",", ".") 
#     obitos_novos = "-" if df_data_on_date["obitosNovos"].isna().values[0]  else f'{int(df_data_on_date["obitosNovos"].values[0]):,}'.replace(",", ".") 
        
#     return (recuperados_novos, acompanhamentos_novos, casos_acumulados, casos_novos, obitos_acumulado, obitos_novos,)



# @app.callback(
    
#     Output("line-graph", "figure"),
#     [Input("location-dropdown", "value"), Input("location-button", "children")]
    
# )

# def plot_line_graph(plot_type, location):
    
#     if location == "BRASIL":
#         df_data_on_location = df_brasil.copy()
#     else:
#         df_data_on_location = df_states[(df_states["estado"] == location)]
#     fig2 = go.Figure(layout={"template":"plotly_dark"})
#     bar_plots = ["casosNovos", "obitosNovos"]

#     if plot_type in bar_plots:
#         fig2.add_trace(go.Bar(x=df_data_on_location["data"], y=df_data_on_location[plot_type]))
#     else:
#         fig2.add_trace(go.Scatter(x=df_data_on_location["data"], y=df_data_on_location[plot_type]))
    
#     fig2.update_layout(
#         paper_bgcolor="#242424",
#         plot_bgcolor="#242424",
#         autosize=True,
#         margin=dict(l=10, r=10, b=10, t=10),
#         )
#     return fig2
    
# @app.callback(
#     Output("choropleth-map", "figure"), 
#     [Input("date-picker", "date")]
# )
# def update_map(date):
#     df_data_on_states = df_states[df_states["data"] == date]

#     fig = px.choropleth_mapbox(df_data_on_states, locations="estado", geojson=brazil_states, 
#         center={"lat": CENTER_LAT, "lon": CENTER_LON},  # https://www.google.com/maps/ -> right click -> get lat/lon
#         zoom=4, color="casosAcumulado", color_continuous_scale="Redor", opacity=0.55,
#         hover_data={"casosAcumulado": True, "casosNovos": True, "obitosNovos": True, "estado": False}
#         )

#     fig.update_layout(paper_bgcolor="#242424", mapbox_style="carto-darkmatter", autosize=True,
#                     margin=go.layout.Margin(l=0, r=0, t=0, b=0), showlegend=False)
#     return fig

# @app.callback(

#     Output("location-button", "children"),[Input("choropleth-map", "clickData"), Input("location-button", "n_clicks")]

# )

# def update_location(click_data, n_clicks):
#     changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
#     if click_data is not None and changed_id != "location-button.n_clicks":
        
#         state = click_data["points"][0]["location"]
        
#         return "{}".format(state)

#     else:

#         return "BRASIL"

if __name__ == "__main__":
    app.run_server(debug=True)