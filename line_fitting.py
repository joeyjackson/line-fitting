import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def main():
    slope = (0,1,1)
    y_inter = 30
    x_p, y_p = generate_noisy_trendline_points(slope=slope, y_inter=y_inter)
    plt.scatter(x_p, y_p)
    bottom, top = plt.ylim()
    left, right = plt.xlim()

    m = np.array([[0, 1]])
    b = np.array([[30]])

    x = np.array([np.linspace(left, right, int(right - left))])
    x_3 = np.power(x, 3)

    y = m.dot(np.vstack((x, x_3))) + b

    x = x.reshape(-1)
    y = y.reshape(-1)
    plt.plot(x, y)
    plt.ylim(bottom, top)
    plt.show()


def generate_noisy_trendline_points(num_pts=100, variation=0.1, slope=1, y_inter=0):
    if type(slope) == float or type(slope) == int:
        slope = [slope]
    else:
        slope = list(slope)

    x = np.random.normal(100, 50, num_pts)
    x_terms = []
    for i in range(len(slope)):
        x_terms.append(np.power(x, i+1))

    m = np.array([slope])
    b = np.array([[y_inter]])

    y = (m.dot(np.vstack(x_terms)) + b)

    noise = np.random.normal(0, (np.max(y) - np.min(y)) * variation, num_pts)

    y += noise

    return x, y


if __name__ == '__main__':
    main()