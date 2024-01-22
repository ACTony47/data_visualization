import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.style.use('classic')
fig,ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap='viridis', s=15)
ax.set_aspect('equal')  # 指定两条轴上的间距必须相等
plt.show()
