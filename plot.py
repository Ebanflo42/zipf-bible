import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from sklearn.linear_model import LinearRegression


# quick trick to fit a power law
# loop through logarithmic sections of the curve
# find the best fitting linear regression model on each one
def fit_power_law(logx, logy):

    print('Fitting power law . . .')

    n_data = len(logx)

    logx = logx.reshape(-1, 1)
    logy = logy.reshape(-1, 1)

    best_reg = LinearRegression(n_jobs=-1)
    best_reg.fit(logx[:2000], logy[:2000])
    best_score = best_reg.score(logx[:2000], logy[:2000])

    for i in tqdm(range(1, n_data//2000)):

        new_reg = LinearRegression(n_jobs=-1)
        new_reg.fit(logx[i : 2000*i], logy[i : 2000*i])
        new_score = new_reg.score(logx[i : i + 2000], logy[i : i + 2000])

        if new_score > best_score:
            best_reg = new_reg
            best_score = new_score

    return best_reg.intercept_.item(), best_reg.coef_[0].item()


if __name__ == '__main__':

    fig = plt.figure()
    ax = fig.add_subplot()

    freqs = np.load('frequencies.npy')
    freqs = np.sort(freqs)[::-1]
    n_words = len(freqs)

    x_vals = [i for i in range(1, 1 + n_words)]
    logx = np.log10(x_vals)
    logy = np.log10(freqs)
    intercept, coef = fit_power_law(logx, logy)

    ax.loglog(x_vals, freqs, label='Bible')
    ax.loglog(x_vals,
              [(10**intercept)*(x**coef) for x in x_vals],
              label=f'$y={coef:.2f}x+{intercept:.2f}$')
    ax.set_title('Frequency of Words in the NIV Bible')
    ax.set_xlabel('Word Rank')
    ax.set_ylabel('Number of Occurrences')

    plt.legend()

    plt.savefig('zipf_curve.png')