import unittest

from class_1_define import House


class TestHouse(unittest.TestCase):
    def test_can_instantiate(self):
        """House class should allow creating an object."""
        h = House()
        self.assertIsInstance(h, House)


if __name__ == "__main__":
    unittest.main()
