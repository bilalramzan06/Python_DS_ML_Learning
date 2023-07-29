# Import numpy
import numpy as np

# Collapse the data lists to view main code
height_in = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74, 74, 69, 70, 73, 75, 78, 79]

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in inches to meter: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)