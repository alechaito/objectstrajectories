import pytest
from classes.object import Objects

class TestObjects:
    def setup_method(self):
        self.objects = Objects('test_data.npy')

    def test_get_object_valid_uuid(self):
        # Test that a valid UUID returns the correct object
        obj = self.objects.get_by_uuid(1)
        assert obj.uuid == 1

    def test_get_object_invalid_uuid(self):
        # Test that an invalid UUID returns None
        obj = self.objects.get_by_uuid(-1)
        assert obj is None
    
    def test_filter(self):
        # Test that the filter function correctly filters out trajectories
        def filter_func(trajectory):
            return len(trajectory) > 3

        filtered = self.objects.filter(filter_func)
        assert len(filtered) == 4

    def test_plot(self):
        # Test that the plot function does not raise an exception
        self.objects.plot()