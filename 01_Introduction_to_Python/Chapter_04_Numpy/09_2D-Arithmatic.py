# Import numpy package
import numpy as np

# Collapse the data lists to view main code
baseball = [[74.0, 180.0, 22.99], [74.0, 215.0, 34.69], [72.0, 210.0, 30.78], [72.0, 210.0, 35.43], [73.0, 188.0, 35.71], [69.0, 176.0, 29.39], [69.0, 209.0, 30.77], [71.0, 200.0, 35.07], [76.0, 231.0, 30.19], [71.0, 180.0, 27.05], [73.0, 188.0, 23.88], [73.0, 180.0, 26.96], [74.0, 185.0, 23.29], [74.0, 160.0, 26.11], [69.0, 180.0, 27.55], [70.0, 185.0, 34.27], [73.0, 189.0, 27.99], [75.0, 185.0, 22.38], [78.0, 219.0, 22.89], [79.0, 230.0, 25.76]]

updated = [[1.2303559, -11.16224898, 1.0], [1.02614252, 16.09732309, 1.0], [1.1544228, 5.08167641, 1.0], [0.64427532, -5.09538071, 1.0], [1.00590086, 2.24342718, 1.0], [0.97953547, 12.19841763, 1.0], [0.62874324, 13.72324216, 1.0], [1.27075194, -8.87946313, 1.0], [0.47655945, -10.82495536, 1.0], [0.91699376, -7.01116249, 1.0], [1.17179326, 1.19946614, 1.0], [1.14509104, -12.00385685, 1.0], [1.20684945, -13.29830645, 1.0], [1.03436155, 3.01324251, 1.0], [0.87747454, 10.51779503, 1.0], [0.9813308, -1.55666485, 1.0], [1.03051228, 4.47971582, 1.0], [1.21042271, -19.04502745, 1.0], [1.34612414, 6.74418894, 1.0], [0.97544726, 7.27211497, 1.0]]

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = [0.0254, 0.453592, 1]

# Print out product of np_baseball and conversion
print(np_baseball * conversion)