from classes.object import Objects
from utils.filters import filter_length

#loadind objects from given file
objects = Objects("data.npy")

# plotting all trajectories
objects.plot()

# applying filter_length
filtered_points = objects.filter(filter_length)

# plotting only filtered trajectories
objects.plot(filtered_points)






