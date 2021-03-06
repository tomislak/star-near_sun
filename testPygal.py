#!/home/etokral/Python_projs/starNearSun/bin/python

import pygal

bar_chart = pygal.Bar()
bar_chart.title = "Sekvenca"
bar_chart.x_labels = map(str, range(11))
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart.render_to_file('bar_chart.svg')
