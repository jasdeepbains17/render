import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd

countries_wins = pd.DataFrame({
    "Country": ["Brazil", "Germany", "Italy", "Argentina", "France", "Uruguay", "United Kingdom", "Spain"],
    "Wins": [5, 4, 4, 3, 2, 2, 1, 1]
})
worldcup_years = pd.DataFrame({
    "year": ["1930", "1934", "1938", "1950", "1954", "1958", "1962", "1966", "1970", "1974", "1978", "1982", "1986", "1990", "1994", "1998", "2002", "2006", "2010", "2014", "2018", "2022"],
    "winners": ["Uruguay", "Italy", "Italy", "Uruguay", "West Germany", "Brazil", "Brazil", "England", "Brazil", "West Germany", "Argentina",
                "Italy", "Argentina", "West Germany", "Brazil", "France", "Brazil", "Italy", "Spain", "Germany", "France", "Argentina"],
    "runner ups": ["Argentina", "Czechoslovakia", "Hungary", "Brazil", "Hungary", "Sweden", "Czechoslovakia", "West Germany", "Italy", "Netherlands",
                "Netherlands", "West Germany", "West Germany", "Argentina", "Italy", "Brazil", "Germany", "France", "Netherlands", "Argentina", "Croatia", "France"]
})

fig = px.choropleth(
    countries_wins,
    locations="Country",
    locationmode="country names",
    color="Wins",
    color_continuous_scale="Viridis",
    scope="world",
    title="Map of FIFA World Cup Winners"
)

app = dash.Dash()
app.layout = [
    html.H1(children="Fifa World Cup Winners", style={'textAlign':'center'}),
    dcc.Graph(figure=fig),
    html.Br(),
    html.Label("Select World Cup Year:"),
    dcc.Dropdown(worldcup_years.year, "1930", id="dropdown-selection"),
    dcc.Markdown(id="wc-results", children=" ")
]

@callback(
    Output(component_id="wc-results", component_property="children"),
    Input(component_id="dropdown-selection", component_property="value")
)

def update_markdown(year):
    index = worldcup_years.index[worldcup_years["year"] == year]
    out_str = f'''
    Winner: _**{worldcup_years['winners'].iloc[index].item()}**_ 
    
    Runner Up: _{worldcup_years['runner ups'].iloc[index].item()}_
    '''
    return out_str

if __name__ == '__main__':
    app.run(debug=True)