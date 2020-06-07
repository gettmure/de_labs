import matplotlib.pyplot as plt


class ODE:
    _plot_is_created = False
    _values_are_calculated = False

    def __init__(self, initial_x, initial_y, alpha, beta):
        self._x = initial_x
        self._y = initial_y
        self._alpha = alpha
        self._gamma = alpha
        self._beta = beta
        self._delta = beta
        self._x_values = [initial_x]
        self._y_values = [initial_y]

    def __get_x_value(self, x, y):
        return (self._alpha - self._beta * y) * x

    def __get_y_value(self, x, y):
        return (self._delta * x - self._gamma) * y

    def calculcate_values(self, step):
        for i in range(0, 5):
            x = self.__get_x_value(self._x, self._y) * step + self._x
            y = self.__get_y_value(self._x, self._y) * step + self._y
            self._x = self._x_values[i]
            self._y = self._x_values[i]
            self._x_values.append(x)
            self._y_values.append(y)
            print(self._x_values[i],  self._y_values[i])
        self._values_are_calculated = True

    def create_plot(self):
        if (self._values_are_calculated):
            plt.plot(self._x_values, self._y_values)
            plt.xlabel('$x$')
            plt.ylabel('$y$')
            plt.title("ODE plot")
            self._plot_is_created = True
        else:
            print("obama denied this operation!")

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
    ode = ODE(1, 1, 0.29, 0.29)
    ode.calculcate_values(0.001)
    ode.create_plot()
    ode.save_plot('plot', 'png')


if __name__ == "__main__":
    main()
