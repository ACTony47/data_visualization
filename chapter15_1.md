1. `fig, ax = plt.subplots()` fig是生成的整个图形，ax表示图形中的绘图
2. `ax.plot(squares)` 只提供了一个列表，默认为y轴 x轴为**0，1，2，3，4**
3. 使用`plt.style.use('seaborn-v0_8') ` 设置style 可以用plt.style.available查看可用的style