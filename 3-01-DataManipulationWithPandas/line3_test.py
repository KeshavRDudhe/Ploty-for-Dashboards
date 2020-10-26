#######
# This line chart uses pandas to reduce a U.S. Census Bureau
# dataset down to just six New England states.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Launch the application:
app = dash.Dash()

# read a .csv file into a pandas DataFrame:
df = pd.read_csv('../sourcedata/nst-est2017-alldata.csv')
# grab just the six New England states:
df2 = df[df['DIVISION']=='1']
# set the index to state name:
df2.set_index('NAME', inplace=True)
# grab just the population columns:
df2 = df2[[col for col in df2.columns if col.startswith('POP')]]

print(list(df2))


# pass data (use a list comprehension to build traces) into pyo.plot directly
# pyo.plot([go.Scatter(
#     x = df2.columns,
#     y = df2.loc[name],
#     mode = 'markers+lines',
#     name = name
# ) for name in df2.index], filename='line3.html')


app.layout = html.Div([

    dcc.Graph(
        id='old_faithful',

        figure={
            'data': [
                go.Scatter(
                    x = df['POPESTIMATE2010'],
                    y = df['POPESTIMATE2011'],
                    mode = 'markers'
                )          
            ]                    ,
 
            'layout': go.Layout(
                title = 'Old Faithful Eruption Intervals v Durations',
                xaxis = {'title': 'Duration of eruption (minutes)'},
                yaxis = {'title': 'Interval to next eruption (minutes)'},
                hovermode='closest'
            )

            
        }
    )
])

# Add the server clause:
if __name__ == '__main__':
    app.run_server()
