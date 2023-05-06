# Description

This project is focused on analyzing and visualizing a set of trajectories on a latitudinal/longitudinal plain. The data provided is in the form of vector data, which represents the movement of vehicles over a certain period of time. The objective of this project is to create an object-oriented framework that can process and analyze the provided data. The framework should be able to filter and plot trajectories based on user-defined criteria, providing a means to identify patterns and trends in the vehicle movements. Ultimately, this framework can be used to gain insights into traffic flow and help optimize transportation systems.

## Data Requirements
The data file should be a numpy matrix having the following columns

- index
- uuid
- x
- y

## How to load a dataset?
1. With the file that follows the data requirement section, put the file into the folder called "files".
2. Import class Objects
3. Instance a class Objects given the filename as a parameter


```python
from classes.object import Objects

#loadind objects from given file
objects = Objects("data.npy")
```

## How to plot object and objects trajectories?

1. Plotting all objects trajectories
```python
objects.plot()
```

2. Plotting a single object trajectory
```python
# get object by uuid
object = objects.get_by_uuid(uuid=0)

object.plot()
```

### How to filter a trajectories or a single trajetory?

1. Filtering all objects trajectories
```python
from classes.object import Objects
from utils.filters import filter_length

#loadind objects from given file
objects = Objects("data.npy")

# applying filter_length
filtered_points = objects.filter(filter_length)

# plotting only filtered trajectories
objects.plot(filtered_points)
```

2. Filtering a object trajectory
```python
from classes.object import Objects
from utils.filters import filter_threshold

#loadind objects from given file
objects = Objects("data.npy")

object = objects.get_by_uuid(uuid=0)

# applying filter_length
filtered_points = object.filter(filter_threshold)

# plotting only filtered trajectories
object.plot(filtered_points)
```