import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def main():
    slope = 20
    y_inter = 30
    x, y = generate_noisy_trendline_points(slope=slope, y_inter=y_inter)
    plt.scatter(x, y)

    m = np.array([[0, 0.5]])
    b = np.array([[30]])
    x_1 = np.linspace(0, 100, 100).reshape((1, 100))
    x_2 = x_1 * x_1
    y_1 = m.dot(np.vstack((x_1, x_2))) + b
    plt.plot(x_1.reshape(-1), y_1.reshape(-1))
    plt.show()


def generate_noisy_trendline_points(num_pts=100, variation=50, slope=1, y_inter=0):
    x = np.random.normal(100, 50, num_pts)
    noise = np.random.normal(0, variation, num_pts)
    y = (slope * x.astype(np.double) + y_inter) + noise
    return x, y


if __name__ == '__main__':
    main()