from dataclasses import dataclass
from classes.trajectory import TrajectoryPoint, Point
import numpy as np
import sys

@dataclass
class Data:
    filename = str
    dataset = None
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        try:
            self.dataset = np.load(f"./files/{self.filename}")
        except OSError:
            print("Error: No such file or directory.")
            sys.exit(0)
            

