import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from collections import deque
import CharismaCollector

x = deque(maxlen=50)
y = deque(maxlen=50)

print("Do you want average of all (assets), average of (industry), or one (asset)?")
choice = input("Please enter one of the words in the parenthesis:\n")
if choice != "all":
    name = input("Please enter name of asset or industry:\n")
else:
    name = ''

time, value = CharismaCollector.collector(choice, name)
x.append(time)
y.append(value)

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(id='graph-update',
                     interval=30 * 1000)
    ]
)


@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def graph_update(input_data):
    global x
    global y
    new_time, new_data = CharismaCollector.collector(choice, name)
    x.append(new_time)
    y.append(new_data)

    data = go.Scatter(x=list(x), y=list(y), name='IBS Data', mode='lines+markers')
    return {'data': [data], 'layout': go.Layout(xaxis={'type': 'date', 'tick0': x[0], 'tickmode': 'linear', 'dtick': 30000},
                                                yaxis=dict(range=[min(y), max(y)]))}


if __name__ == "__main__":
    app.run_server(debug=True)
