import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Scatter(
    x=[1, 2, 3], y=[1, 2, 3],
    marker=dict(
        color=['red', 'blue', 'green'],
        size=[30, 80, 200]),
    mode='markers')
plot_url = py.plot([trace])

