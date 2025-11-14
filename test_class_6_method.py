import unittest

from class_6_method import WashingMachine, test


class TestWashingMachine(unittest.TestCase):
    def setUp(self):
        """Get fresh instance for each test."""
        self.machine = test()

    def test_class_attributes(self):
        """Verify class-level attributes."""
        self.assertEqual(WashingMachine.brand, "Samsung")
        self.assertEqual(WashingMachine.type, "Front Load")

    def test_instance_attributes(self):
        """Verify instance attributes after creation."""
        self.assertEqual(self.machine.capacity, 13)
        self.assertEqual(self.machine.owner, "Eve")
        self.assertFalse(self.machine.is_running)  # start/stop not called
        self.assertEqual(self.machine.mode, "Spin")  # mode was set in test()


if __name__ == "__main__":
    unittest.main()
