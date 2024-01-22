import matplotlib.pyplot as plt
from random_walk import RandomWalk

# rw = RandomWalk()
# rw.fill_walk()
# plt.style.use('classic')
# fig,ax = plt.subplots()
# ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap='viridis', s=15)
# ax.set_aspect('equal')  # 指定两条轴上的间距必须相等
# plt.show()
while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()
    plt.style.use('classic')

    # fig, ax = plt.subplots()
    # set the size manually
    fig, ax = plt.subplots(figsize=(16, 9), dpi=128)

    point_numbers = range(rw.num_points)  # 使用range生成一个数值列表
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # plot生成折线图
    ax.plot(rw.x_values, rw.y_values, linewidth=1, c='blue')

    #ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
    #  edgecolor='none' 消除轮廓
    # ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap='viridis', s=15)

    # emphasize the starting point and ending point
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # hide the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_aspect('equal')
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
