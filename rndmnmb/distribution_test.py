import math
import numpy as np
from numpy import genfromtxt
import scipy.stats as stats


def poisson_distribution(mean):
    distribution = []
    for x in range(20):
        distribution.append(((mean ** x) / math.factorial(x)) * math.exp(-mean))
    return np.array(distribution)


def count_x_values(observed_data):
    distribution = [0] * 20

    for x in observed_data:
        distribution[int(x)] += 1

    return distribution


def poisson_distribution_observations(mean, data):
    distribution = []
    for x in data:
        distribution.append(((mean ** x) / math.factorial(x)) * math.exp(-mean))

    return np.array(distribution)


def read_csv(filename):
    observed_data = genfromtxt(filename, delimiter=',')
    observed_data = np.delete(observed_data, observed_data.size - 1)
    return observed_data


def checkChiSquared(observed_distribution, expected_values):
    sum_observed = np.sum(observed_distribution)
    sum_expected = np.sum(expected_values)
    expected = (expected_values / sum_expected) * sum_observed
    chi_square, p = stats.chisquare(observed_distribution, expected)
    print("Score:")
    print(chi_square)
    print("P-Value:")
    print(p)


# five
csv_values = read_csv("D:\\AI Engineering\\APRG\\random_numbers\\five.csv")
observed_distribution = count_x_values(csv_values)
expected_values = poisson_distribution(4)

checkChiSquared(observed_distribution, expected_values)

# ten
csv_values = read_csv("D:\\AI Engineering\\APRG\\random_numbers\\ten.csv")
observed_distribution = count_x_values(csv_values)
expected_values = poisson_distribution(4)

checkChiSquared(observed_distribution, expected_values)

# one hundred
csv_values = read_csv("D:\\AI Engineering\\APRG\\random_numbers\\onehundred.csv")
observed_distribution = count_x_values(csv_values)
expected_values = poisson_distribution(4)

checkChiSquared(observed_distribution, expected_values)

# ten thousand
csv_values = read_csv("D:\\AI Engineering\\APRG\\random_numbers\\tenthousand.csv")
observed_distribution = count_x_values(csv_values)
expected_values = poisson_distribution(4)

checkChiSquared(observed_distribution, expected_values)


