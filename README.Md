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

## How to plot objects trajectories?

```python
objects = Objects("data.npy")

objects.plot()
```


### How to filter trajectories?

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