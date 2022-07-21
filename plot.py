import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from sklearn.linear_model import LinearRegression


if __name__ == '__main__':

    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    freqs = np.load('frequencies.npy')
    freqs = np.sort(freqs)[::-1]
    n_words = len(freqs)

    x_vals = [i for i in range(1, 1 + n_words)]
    intercept = 4.95
    coef = -1

    ax1.plot(x_vals[:100], freqs[:100], label='Bible')
    ax1.plot(x_vals[:100],
             [(10**intercept)*(x**coef) for x in x_vals[:100]], '--',
             label="$y=10^{4.95}/x$", color='green')
    ax1.set_title(f'Frequency of Words in the NIV Bible')
    ax1.set_xlabel('Word Rank')
    ax1.set_ylabel('Number of Occurrences')
    ax1.set(xlim=(-10, 100), ylim=(-100, 100000))
    ax1.set_aspect(1/1000)
    ax1.legend()

    ax2.loglog(x_vals, freqs, label='Bible')
    ax2.loglog(x_vals,
              [(10**intercept)*(x**coef) for x in x_vals], '--',
              label=f'$y=-x+4.95$', color='green')
    ax2.set_title(f'Frequency of Words in the NIV Bible')
    ax2.set_xlabel('Word Rank')
    ax2.set_ylabel('Number of Occurrences')
    ax2.set(xlim=(1, 100000), ylim=(1, 100000))
    ax2.set_aspect('equal')
    ax2.legend()

    fig.tight_layout()

    plt.savefig('zipf_curve.png')