from die import Die
import plotly.express as px

die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1, die.num_sides+1)  # range from 1 to die.num-sides
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)
title = "test show"
labels = {'x': 'results', 'y': 'frequency'}  # set graph labels
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)  # set the x and y axis
fig.show()
