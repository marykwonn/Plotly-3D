import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

py.sign_in(username='marykwon', api_key='v4mYJR8F5wp857gR4E3F')

df = pd.read_csv(r'C:\Users\kwonm\Documents\TEST\SIMPTEST.csv')
# need to create series to create unique list of well names
series_well_names = df['WELL_NAME']
# list of unique well names
unique_well_names = series_well_names.unique()
# data bracket for the all traces
data_traces = []


def make_trace(well_name):
    well_coord = df.loc[df['WELL_NAME'] == well_name]

    x = well_coord['X']
    y = well_coord['Y']
    z = well_coord['Z']

    trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines',
        name=well_name
    )

    return trace


for i in unique_well_names:
    trace = make_trace(i)
    data_traces.append(trace)

layout = go.Layout(
    title="Sample Data",
    xaxis={'title': 'X'},
    yaxis={'title': 'Y'}
)

plotly.offline.plot({"data": data_traces,
                     "layout": layout},
                    filename='temporary',
                    auto_open=True)

# print('\nresult data :\n', testing)
