# Import numpy
import numpy as np

# Collapse the data lists to view main code
baseball = [[74, 180], [74, 215], [72, 210], [72, 210], [73, 188], [69, 176], [69, 209], [71, 200], [76, 231], [71, 180], [73, 188], [73, 180], [74, 185], [74, 160], [69, 180], [70, 185], [73, 189], [75, 185], [78, 219], [79, 230]]

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print mean height (first column)
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))