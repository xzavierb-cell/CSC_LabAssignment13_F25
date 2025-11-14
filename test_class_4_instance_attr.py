import unittest

from class_4_instance_attr import House


class TestHouse(unittest.TestCase):
    def test_class_attributes(self):
        """Class-level school attributes should be correct."""
        self.assertEqual(House.elementary_school, "FV Elementary")
        self.assertEqual(House.middle_school, "FV Middle")
        self.assertEqual(House.high_school, "FV High")

    def test_instance_initialization(self):
        """Verify that owner and address are set, and size has default value."""
        h = House(owner="Alice", address="123 Main St")

        self.assertEqual(h.owner, "Alice")
        self.assertEqual(h.address, "123 Main St")
        self.assertEqual(h.size, 2500)

    def test_instances_are_independent(self):
        """Different instances should not share instance data."""
        h1 = House(owner="A", address="Addr1")
        h2 = House(owner="B", address="Addr2")

        self.assertNotEqual(h1.owner, h2.owner)
        self.assertNotEqual(h1.address, h2.address)

    def test_instance_can_override_class_attribute(self):
        """Instance override of class attribute should not affect class or other instances."""
        h = House(owner="X", address="Road1")
        h.elementary_school = "Custom Elementary"

        # instance override works
        self.assertEqual(h.elementary_school, "Custom Elementary")

        # class unaffected
        self.assertEqual(House.elementary_school, "FV Elementary")

        # other instance unaffected
        h2 = House(owner="Y", address="Road2")
        self.assertEqual(h2.elementary_school, "FV Elementary")

    def test_missing_init_arguments(self):
        """House constructor should require owner and address."""
        with self.assertRaises(TypeError):
            House()  # missing required parameters

        with self.assertRaises(TypeError):
            House(owner="OnlyOwner")  # missing address


if __name__ == "__main__":
    unittest.main()
