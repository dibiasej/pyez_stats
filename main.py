from pyez_stats import Bernoulli
import os

if __name__ == "__main__":

    arr = [5, 4, 3, 6, 7, 2]
    arr1 = [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1]

    gaus = Bernoulli(arr1)
    print(gaus.maximum_likelihood_estimator())
    print(gaus.p_hat())