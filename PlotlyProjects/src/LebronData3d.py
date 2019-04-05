import plotly.plotly as py
import plotly.graph_objs as go

lebron_info = open("D:/SparkProjects/NBADataBase/data/lebron_data.csv")

yearList = lebron_info.readline().split(',')
pointsList = [float(i) for i in lebron_info.readline().split(',')]
reboundsList = [float(i) for i in lebron_info.readline().split(',')]
assistsList = [float(i) for i in lebron_info.readline().split(',')]
stealsList = [float(i) for i in lebron_info.readline().split(',')]
blocksList = [float(i) for i in lebron_info.readline().split(',')]
gamesList = [float(i) for i in lebron_info.readline().split(',')]
fieldPercentList = [float(i) for i in lebron_info.readline().split(',')]
threePercentList = [float(i) for i in lebron_info.readline().split(',')]

trace = go.Scatter3d(
    x=pointsList,
    y=reboundsList,
    z=assistsList,
    showlegend=True,
)

layout = go.Layout(
    title='LeBron James',
    scene=dict(
        xaxis=dict(
            title='Points',
            showgrid=True,
            showline=False
        ),
        yaxis=dict(
            title='Rebounds',
            showgrid=True,
            showline=False
        ),
        zaxis=dict(
            title='Assists',
            showgrid=True,
            showline=False
        )
    )
)
fig = go.Figure(data=[trace], layout=layout)
py.plot(fig, filename='LeBron James')
