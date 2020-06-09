import matplotlib.pyplot as plt


def get_x(x, y, alpha, beta):
    return (alpha - beta * y) * x


def get_y(x, y, delta, gamma):
    return (delta * x - gamma) * y


def get_data(x, y, alpha, beta, delta, gamma, step):
    data = [[], []]
    for i in range(0, 1000000):
        data[0].append(get_x(x, y, alpha, beta) * step + x)
        data[1].append(get_y(x, y, delta, gamma) * step + y)
        x = data[0][i]
        y = data[1][i]
    return data


def main():
    y = 0
    x = 1
    step = 0.001
    alpha = gamma = 0.29
    beta = delta = 0.29

    data = get_data(x, y, alpha, beta, delta, gamma, step)

    plt.plot(data[0], data[1])
    plt.savefig('plot.png')
    plt.close()


if __name__ == "__main__":
    main()
