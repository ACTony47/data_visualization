from die import Die
import plotly.express as px


die1 = Die()
die2 = Die()

results = []
for roll in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)


frequencies = []
max = die1.num_sides + die2.num_sides # 为了应对不同面色子的情况
poss_results = range(2, max+1)

for value in poss_results:
    frequency = results.count(value)  # count all these values value range from 2 to 12
    frequencies.append(frequency)

title = "results from 1000 * 2 dice rolls"
labels = {'x': 'results', 'y': 'frequency'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)  # 使用update_layout 更新图像设置 xaxis_dtick 设置需要显示的间距 为1 即代表每一条都显示
fig.show()
