from dataclasses import dataclass
from classes.trajectory import TrajectoryPoint, Point
import numpy as np
import sys

@dataclass
class Data:
    filename = str
    dataset = None
    trajectories = dict()
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        try:
            self.dataset = np.load(f"./project/files/{self.filename}")
            #self.convert_dataset()
        except OSError:
            print("Error: No such file or directory.")
            sys.exit(0)
            

