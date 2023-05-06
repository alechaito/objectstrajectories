from dataclasses import dataclass
from classes.data import Data
from classes.trajectory import TrajectoryPoint, Point
from typing import Optional, List
from matplotlib import pyplot as plt

@dataclass
class Object:
    """
    This class represents an object with a unique identifier (uuid) and a trajectory.

    Attributes:
        uuid (int): The unique identifier of the object.
        trajectory (list, optional): A list of trajectory points. Defaults to None.
    """
    uuid: int
    trajectory: Optional[list] = None
        
@dataclass
class Objects(Data):
    """
    The Objects class is used for working with object trajectory data, 
    inherited from the Data class. The Data class loads and stores trajectory data from a file. 
    The Objects class contains attributes and methods for manipulating and analyzing the 
    trajectory data.

    Attributes:
        instances(dict): A dictionary containing all the objects trajectories indexed by their UUID.

    Methods:
        get_by_uuid(self, uuid: int) -> dict: Returns an object for the given UUID.
        load_object_instances_from_dataset(self): Loads object instances from the dataset and stores them in the instances dictionary.
        filter(self, filter_func): Filters the trajectory data based on the provided filter_func function.
        plot(self, trajetory: list = None): Plots the given trajectory as a scatter plot. If trajetory is not provided, the method uses the internal trajectory data stored in the object.
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

    def load_object_instances_from_dataset(self) -> None:
        """
        Loads object instances from the dataset stored in the `self.dataset` attribute of the 
        `Objects` object, and stores them in the `self.instances` attribute as a dictionary of 
        lists of `TrajectoryPoint` objects, indexed by UUID.

        Returns:
            None
        """
        for input in self.dataset:
            uuid = int(input[1])
            if uuid not in self.instances:
                self.instances[uuid] = []

            trajectory_point = TrajectoryPoint(input[0], Point(input[2], input[3]))
            self.instances[uuid].append(trajectory_point)

        for uuid in self.instances:
            self.instances[uuid] = sorted(self.instances[uuid], key=lambda x: x.index)

    def filter(self, filter_func) -> List[TrajectoryPoint]:
        """
        Returns a filtered list of all trajectory points in the data set.

        The method applies the specified filter function to each object in the data set and
        returns a list of all trajectory points for which the filter function returns True.

        Args:
            filter_func (Callable[[List[TrajectoryPoint]], bool]): A function that takes a
                list of `TrajectoryPoint` objects and returns True or False.

        Returns:
            List[TrajectoryPoint]: A list of `TrajectoryPoint` objects that satisfy the
            filter condition.
        """
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