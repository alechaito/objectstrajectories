from dataclasses import dataclass
from classes.data import Data
from classes.trajectory import TrajectoryPoint, Point
from typing import Optional
from matplotlib import pyplot as plt

@dataclass
class Object:
    """
    This class represents an object with a unique identifier (uuid) and a trajectory.

    Attributes:
        - uuid (int): The unique identifier of the object.
        - trajectory (list, optional): A list of trajectory points. Defaults to None.

    Methods:
        - filter(filter_func): Returns a new trajectory list containing only the trajectories that satisfy the given filter function.
        - plot(trajectory=None): Plots the given trajectory as a scatter plot.
    
    """
    uuid: int
    trajectory: Optional[list] = None

    def filter(self, filter_func) -> list:
        """
        Returns a new trajectory list containing only the trajectories that satisfy the given filter function.
        
        Args:
        - func: a function that takes a trajectory list as input and returns a boolean value
        
        Returns:
        - A new trajectory list
        """
        filtered = []
        for point in self.trajectory:
            if filter_func(point):
                filtered.append(point)
        return filtered

    def plot(self, trajetory: list = None) -> None:
        """
        Plots the given trajectory as a scatter plot.

        Args:
            trajetory (list, optional): A list of trajectory points to plot. If not
                provided, the method uses the internal trajectory data stored in the
                object. Defaults to None.

        Returns:
            None
        """
        if trajetory is None:
            trajetory = self.trajectory

        xs = [trajectory_point.point.x for trajectory_point in trajetory]
        ys = [trajectory_point.point.y for trajectory_point in trajetory]
        plt.plot(xs, ys)
        plt.show()
        
@dataclass
class Objects(Data):
    """
    A class for working with object trajectory data.

    Inherits from the `Data` class, which loads and stores trajectory data from a file.

    Attributes:
        filename (str): The name of the file containing the trajectory data.
        trajectories (dict): A dictionary containing all the objects trajectories
            indexed by their UUID.

    Methods:
        get_by_id(uuid: int) -> dict: Returns an object dictionary for the given UUID.
    """
    instances = dict()

    def __init__(self, filename: str):
        super().__init__(filename)
        self.load_object_instances_from_dataset()

    def get_by_uuid(self, uuid: int) -> dict:
        """
        Returns an object for the given UUID.

        Args:
            uuid (int): The UUID of the object to return.

        Returns:
            object: A object containing information about the object.
        """
        object = Object(uuid)
        object.trajectory = self.instances[uuid]
        return object

    def load_object_instances_from_dataset(self):
        for input in self.dataset:
            uuid = int(input[1])
            if uuid not in self.instances:
                self.instances[uuid] = []

            trajectory_point = TrajectoryPoint(input[0], Point(input[2], input[3]))
            self.instances[uuid].append(trajectory_point)

        for uuid in self.instances:
            self.instances[uuid] = sorted(self.instances[uuid], key=lambda x: x.index)

    def filter(self, filter_func):
        filtered_points = []
        for uuid in self.instances:
            if filter_func(self.instances[uuid]):
                filtered_points.extend(self.instances[uuid])

        return filtered_points

    def plot(self, trajetory: list = None) -> None:
        """
        Plots the given trajectory as a scatter plot.

        Args:
            trajetory (list, optional): A list of trajectory points to plot. If not
                provided, the method uses the internal trajectory data stored in the
                object. Defaults to None.

        Returns:
            None
        """

        if trajetory is None:
            trajetory = []
            for uuid in self.instances:
                trajetory.extend(self.instances[uuid])

        xs = [trajectory_point.point.x for trajectory_point in trajetory]
        ys = [trajectory_point.point.y for trajectory_point in trajetory]
        plt.plot(xs, ys)
        plt.show()