from unittest import TestCase
import numpy as np
from classes.data import Data

class TestData(TestCase):
    def setUp(self):
        self.data = Data("test_data.npy")

    def test_init_with_valid_file(self):
        self.assertIsInstance(self.data.dataset, np.ndarray)

    def test_init_with_invalid_file(self):
        with self.assertRaises(SystemExit):
            Data("nonexistent_file.npy")
