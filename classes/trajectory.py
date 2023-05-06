from dataclasses import dataclass

@dataclass
class Point:
    x:  float
    y:  float

@dataclass
class TrajectoryPoint:
    index:  float
    point:  Point

