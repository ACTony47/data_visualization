import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
#  y_values = [1, 4, 9, 16, 25]
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]  # using list comprehension to calculate squares

plt.style.use('dark_background')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='g', s=10)
ax.scatter(x_values, y_values, c=y_values, cmap='viridis', s=10)
ax.set_title('Squares', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)
ax.axis([0, 1100, 0, 1_100_000])  # setting the axis limits first two nums are min & max of axis x
ax.ticklabel_format(style='plain')  # 设置常规表示法
plt.show()
