#!/home/etokral/Python_projs/starNearSun/bin/python

import plotly.graph_objects as go
import numpy as np

x = np.arange(10)

fig = go.Figure(data=go.Scatter(x=x, y=x**2))
fig.write_html('first_figure.html')

np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

fig = go.Figure()
fig.add_trace(go.Scatter(x=random_x, y=random_y0, mode='lines', name='lines'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1, mode='lines+markers', name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2, mode='markers', name='markers'))

fig.write_html('second_figure.html')

fig3d = go.Figure(data=go.Scatter3d(x=(10,0,-10), y=(15,10,5), z=(12,7,2), mode='markers'))
fig3d.write_html('third_figure.html')
