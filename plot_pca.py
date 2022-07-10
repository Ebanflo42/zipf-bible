import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt


if __name__ == '__main__':

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.grid(visible=True)
    ax.set_axisbelow(True)

    covariance = np.array([[8, 4], [4, 5]])
    sample = rd.multivariate_normal(np.zeros(2), covariance, size=200)

    ax.scatter(sample[:, 0], sample[:, 1])

    ax.axis('equal')
    ax.set(xlim=(-10, 10), ylim=(-8, 8))

    yax = ax.yaxis.get_gridlines()
    yax[4].set_color("k")
    yax[4].set_linewidth(2.5)

    xax = ax.xaxis.get_gridlines()
    xax[4].set_color("k")
    xax[4].set_linewidth(2.5)

    vals, vecs = np.linalg.eig(covariance)
    v1, v2 = vecs[:, 0], vecs[:, 1]
    v1 /= np.linalg.norm(v1)
    v2 /= np.linalg.norm(v2)
    ax.arrow(0, 0, vals[0]*v1[0], vals[0]*v1[1],
             width=0.1, head_width=0.3, color='red')
    ax.arrow(0, 0, vals[1]*v2[0], vals[1]*v2[1],
             width=0.1, head_width=0.3, color='red')

    plt.savefig('pca_plot.png')