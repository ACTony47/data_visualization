1. `fig, ax = plt.subplots()` fig是生成的整个图形，ax表示图形中的绘图
2. `ax.plot(squares)` 只提供了一个列表，默认为y轴 x轴为**0，1，2，3，4**
3. 使用`plt.style.use('seaborn-v0_8') ` 设置style 可以用plt.style.available查看可用的style
4. `ax.scatter(x_values, y_values, c='g', s=100)` c = color s = 指的是大小
5. `y_values = [x**2 for x in x_values]` 直接计算得到列表的值
6. **_颜色映射_** `ax.scatter(x_values, y_values, c=y_values, cmap='viridis', s=10)` c = y_values 指的是颜色和y值相关联 cmap告诉使用哪一个颜色映射 colormaps https://matplotlib.org/stable/users/explain/colors/colormaps.html
7. 自动保存 `plt.savefig('squares.png', bbox_inches='tight')` 第二个参数表示删除多余空白部分 第一个参数可以将图片存放在指定位置，选择某特定文件夹以及文件名
8. 