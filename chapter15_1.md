1. `fig, ax = plt.subplots()` fig是生成的整个图形，ax表示图形中的绘图
2. `ax.plot(squares)` 只提供了一个列表，默认为y轴 x轴为**0，1，2，3，4**
3. 使用`plt.style.use('seaborn-v0_8') ` 设置style 可以用plt.style.available查看可用的style
4. `ax.scatter(x_values, y_values, c='g', s=100)` c = color s = 指的是大小
5. `y_values = [x**2 for x in x_values]` 直接计算得到列表的值