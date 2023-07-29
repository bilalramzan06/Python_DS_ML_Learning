# Import numpy
import numpy as np

# Collapse the data lists to view main code
positions = ["GK", "M", "A", "D", "M", "D", "M", "M", "M", "A", "M", "M", "A", "A", "A", "M", "D", "A", "D", "M"]
heights = [191, 184, 185, 180, 181, 187, 170, 179, 183, 186, 185, 170, 187, 183, 173, 188, 183, 180, 188, 175]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == "GK"]

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != "GK"]

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))