import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_nums = [1, 2, 3, 4, 5]
plt.style.use('seaborn-v0_8')  # set the style of the plot)
fig, ax = plt.subplots()  # fig and ax are the figure and axis objects

ax.plot(input_nums, squares, linewidth=3)  # plot the squares list
ax.set_title("square numbers", fontsize=23)  # set the title and font size
ax.set_xlabel("index", fontsize=14)  # set the x-axis label and font size
ax.set_ylabel("square", fontsize=14)  # set the y-axis label and font size
ax.tick_params(axis='both', labelsize=14) # 对两个轴都进行设置， 刻度标签大小为14
plt.show()
