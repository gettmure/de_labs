import matplotlib.pyplot as plt
from math import sin, pi, exp, log, atan


class ODE:
    _plot_is_created = False
    _values_are_calculated = False

    def __init__(self, initial_x, initial_y, task):
        self._task_number = task
        self._x = initial_x
        self._y = initial_y
        self._x_values = [initial_x]
        self._y_values = [initial_y]

    def __diff_value(self):
        if (self._task_number == 1):
            return (sin(pi * self._x) +
                    self._y**2 * exp(-self._y**2))/self._x
        if (self._task_number == 2):
            return (atan(self._x - sin(log(self._x) - self._x * self._y)) + 1)

    def find_y_euler(self, step, searched_point_x):
        if (self._task_number == 1):
            while(self._x < searched_point_x):
                self._y = self._y + self.__diff_value() * step
                self._x += step
                self._x_values.append(self._x)
                self._y_values.append(self._y)
        if (self._task_number == 2):
            while(self._x > searched_point_x):
                self._y = self._y - self.__diff_value() * step
                self._x -= step
                self._x_values.append(self._x)
                self._y_values.append(self._y)
        self._values_are_calculated = True
        return self._y

    def create_plot(self):
        if (self._values_are_calculated):
            plt.plot(self._x_values, self._y_values)
            plt.xlabel('$x$')
            plt.ylabel('$y$')
            plt.title("ODE plot")
            self._plot_is_created = True
        else:
            print(
                "You haven't found values to create a plot, please, call euler's method function!")

    def show_plot(self):
        if (not self._plot_is_created):
            self.create_plot()
        plt.show()

    def save_plot(self, name, extension):
        if (self._plot_is_created):
            plt.savefig(f'{name}.{extension}')
            plt.close()
        else:
            print("Plot doesn't exist!")


def main():
    ode1 = ODE(1, log(2), 1)
    result1 = ode1.find_y_euler(0.00001, pi)
    ode1.create_plot()
    ode1.save_plot('plot_1', 'png')
    ode2 = ODE(log(2), -pi, 2)
    result2 = ode2.find_y_euler(0.00001, 1/exp(2))
    ode2.create_plot()
    ode2.save_plot('plot_2', 'png')
    print(result1, result2)


if __name__ == "__main__":
    main()
