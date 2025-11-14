import unittest

from class_5_instance import WashingMachine, test


class TestWashingMachine(unittest.TestCase):
    def setUp(self):
        """Get fresh instances for each test."""
        self.machine1, self.machine2 = test()

    def test_class_attributes(self):
        """Verify class-level attributes."""
        self.assertEqual(WashingMachine.brand, "Samsung")
        self.assertEqual(WashingMachine.type, "Front Load")

    def test_instance_initialization(self):
        """Instances created by test() should have correct values."""
        self.assertEqual(self.machine1.capacity, 15)
        self.assertEqual(self.machine1.owner, "Bob")
        self.assertFalse(self.machine1.is_running)
        self.assertEqual(self.machine1.mode, "Normal")

        self.assertEqual(self.machine2.capacity, 12)
        self.assertEqual(self.machine2.owner, "Alice")
        self.assertFalse(self.machine2.is_running)
        self.assertEqual(self.machine2.mode, "Normal")

    def test_instances_are_independent(self):
        """machine1 and machine2 should not share instance data."""
        self.assertNotEqual(self.machine1.capacity, self.machine2.capacity)
        self.assertNotEqual(self.machine1.owner, self.machine2.owner)

    def test_instance_can_override_class_attribute(self):
        """Instance overriding class attributes should not affect class."""
        m = WashingMachine(5, "OverrideOwner")
        m.brand = "LG"

        self.assertEqual(m.brand, "LG")  # instance override works
        self.assertEqual(WashingMachine.brand, "Samsung")  # class stays the same

        # new instance still uses the original class attribute
        new_m = WashingMachine(6, "Another")
        self.assertEqual(new_m.brand, "Samsung")


if __name__ == "__main__":
    unittest.main()
