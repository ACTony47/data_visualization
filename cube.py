import matplotlib.pyplot as plt

x_values = range(1, 100)
y_values = [x**3 for x in x_values]
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap='coolwarm')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('Cube of x')
ax.axis([1, 100, 1, 100_000])
plt.show()
