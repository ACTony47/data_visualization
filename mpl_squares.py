import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()  # fig and ax are the figure and axis objects
ax.plot(squares)  # plot the squares list
plt.show()
