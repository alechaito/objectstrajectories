from dataclasses import dataclass
from classes.trajectory import TrajectoryPoint, Point
import numpy as np
import sys

@dataclass
class Data:
    """
    A base class for loading and storing trajectory data from a file.

    Attributes:
        filename (str): The name of the file containing the trajectory data.
        dataset (ndarray): The trajectory data loaded from the file.
    """
    filename = str
    dataset = None
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        try:
            self.dataset = np.load(f"./files/{self.filename}")
        except OSError:
            print("Error: No such file or directory.")
            sys.exit(0)
            

