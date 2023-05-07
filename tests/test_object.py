import pytest
from unittest import TestCase
from classes.object import Objects
from classes.trajectory import TrajectoryPoint, Point

class TestObjects(TestCase):
    def setUp(self):
        self.objects = Objects("test_data.npy")
        self.objects.instances = {
            1: [
                    TrajectoryPoint(0, Point(1, 2)), 
                    TrajectoryPoint(0, Point(1, 3)),
                    TrajectoryPoint(0, Point(1, 4)),
                    TrajectoryPoint(0, Point(1, 5)),

                ],
            2: [
                    TrajectoryPoint(0, Point(1, 1)), 
                ]
        }

    def test_get_object_valid_uuid(self):
        # Test that a valid UUID returns the correct object
        obj = self.objects.get_by_uuid(1)
        assert obj.uuid == 1

    def test_get_object_invalid_uuid(self):
        with pytest.raises(KeyError):
            self.objects.get_by_uuid(-1)

    def test_filter(self):
        # Filter function should be able to filter just the element with uuid=2
        def filter_func(trajectory):
            return len(trajectory) < 2

        filtered = self.objects.filter(filter_func)
        # Object with uuid=2 has just 1 point then
        assert len(filtered) == 1

    def test_plot(self):
        # Test that the plot function does not raise an exception
        self.objects.plot()