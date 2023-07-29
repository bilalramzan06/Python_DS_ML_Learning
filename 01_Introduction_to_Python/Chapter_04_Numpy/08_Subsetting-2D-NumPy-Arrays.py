# Import numpy package
import numpy as np

# Collapse the data lists to view main code
baseball = [[74, 180], [74, 215], [72, 210], [72, 210], [73, 188], [69, 176], [69, 209], [71, 200], [76, 231], [71, 180], [73, 188], [73, 180], [74, 185], [74, 160], [69, 180], [70, 185], [73, 189], [75, 185], [78, 219], [79, 230]]

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 5th row of np_baseball
print(np_baseball[4][:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]

# Print out height of 12th player
print(np_baseball[11, 0])