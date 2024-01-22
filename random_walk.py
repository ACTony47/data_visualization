from random import choice


class RandomWalk:
    """A class to generate random walks."""
    def __init__(self, num_points=5000):  # 默认点数设置为5000
        """Initialize attributes of a random walk."""
        self.num_points = num_points
        # 所有游走都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ calculate all the points """
        while len(self.x_values) < self.num_points:  # achieve all the points
            # choice randomly choose one digit in the list
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction
            # refuse to stay and not moving
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step  # add the last digit in x_values
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

