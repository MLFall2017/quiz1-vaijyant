"""
Created on Thu Sep 21 20:20:49 2017

@author: vaijy
"""
import os
import csv
import numpy as np

# 1. Reading a file
path = "C:\\users\\vaijy\\Desktop"
file_name = "dataset_1.csv"

os.chdir(path)

x = np.array([], dtype=float)
y = np.array([], dtype=float)
z = np.array([], dtype=float)

with open(file_name) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    header = next(csvReader)
    for row in csvReader:
        x = np.append(x, float(row[0]))
        y = np.append(y, float(row[1]))
        z = np.append(z, float(row[2]))


# 2. Calulating sample_variance
def sample_variance(x):
    n = len(x)
    x_mean = sum(x) / n
    var = sum((x - x_mean) ** 2) / (n - 1)
    return var


# 3. Covariance matrix
def covariance_matrix(x, y):
    cov_matrix = np.cov(x, y)
    return cov_matrix


# -----------------------------------------------------------------------------
print(sample_variance(x))
print(sample_variance(y))
print(sample_variance(z))
print("---------------------------------")
print(covariance_matrix(x, y))
