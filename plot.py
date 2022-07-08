import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from sklearn.linear_model import LinearRegression


if __name__ == '__main__':

    fig = plt.figure()
    ax = fig.add_subplot()

    freqs = np.load('frequencies.npy')
    freqs = np.sort(freqs)[::-1]
    n_words = len(freqs)

    x_vals = [i for i in range(1, 1 + n_words)]
    logx = np.log10(x_vals[:1000]).reshape(-1, 1)
    logy = np.log10(freqs[:1000]).reshape(-1, 1)
    linreg = LinearRegression(n_jobs=-1)
    linreg.fit(logx, logy)
    r2 = linreg.score(logx, logy)
    intercept = linreg.intercept_.item()
    coef = linreg.coef_[0].item()

    ax.loglog(x_vals, freqs, label='Bible')
    ax.loglog(x_vals,
              [(10**intercept)*(x**coef) for x in x_vals],
              label=f'$y={coef:.2f}x+{intercept:.2f}$')
    ax.set_title(f'$Frequency\; of\; Words\; in\; the\; NIV\; Bible,\; R^2 = {r2:.2f}$')
    ax.set_xlabel('Word Rank')
    ax.set_ylabel('Number of Occurrences')

    plt.legend()

    plt.savefig('zipf_curve.png')