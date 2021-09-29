import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

data = pd.read_csv("suicide_rates.csv")
# data = data.query("year == 1985 and country == 'Albany'")
df_brazil = data[data.country == "Brazil"]
suicides_brazil_mean = df_brazil.groupby('year')['suicides/100k pop'].mean()
suicides_world_mean = data.groupby('year')['suicides/100k pop'].mean()
years = df_brazil.year.unique()

men_women = df_brazil.groupby('sex').suicides_no.sum() / df_brazil.groupby('sex').suicides_no.sum().sum()







external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Suicide - Brazil and World"

fig = go.Figure(data=[go.Scatter(x=data["year"], y=suicides_brazil_mean)])
fig2 = go.Figure(data=[go.Bar(x=data["year"], y=data["year"])]) 
fig4 = px.pie(men_women, color_discrete_sequence=px.colors.sequential.RdBu)


app.layout = html.Div(
    children=[
        
        html.H1(children="Suicide - Brazil and World",),
        html.P(
            children="Suicides that occurred in Brazil and around the world"
            " between 1985 and 2015",
            className="header-description",
        ),
        dcc.Graph(
            id='suicide_on_brazil',
            figure= {

                'data': [
                
                    {
                        'x': years, 
                        'y': suicides_brazil_mean, 
                        'type': 'line', 
                        'name': 'Brazil'},
                        
                        {
                        'x': years, 
                        'y': suicides_world_mean, 
                        'type': 'line', 
                        'name': 'World'},
                  
                
                ],

                'layout':{
                    'title': 'Suicide on Brazil and rest the world'
                }

            }
            
        ),
        dcc.Graph(
            figure=fig4,
        ),

        

        
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)