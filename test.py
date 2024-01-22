import plotly.express as px
from die import Die

die1 = Die(8)
die2 = Die(10)

results = []
max_value = die1.num_sides + die2.num_sides
for i in range(10000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
for value in range(2, max_value+1):
    frequency = results.count(value)
    frequencies.append(frequency)

labels = {'x': 'Result', 'y': 'Frequency'}
title = 'chart showing the answer'
fig = px.bar(x=range(2, max_value+1), y=frequencies, labels=labels, title=title) # x的赋值可以用一个变量存储起来 代表x的值的范围
fig.update_layout(xaxis_dtick = 1)
fig.show()
