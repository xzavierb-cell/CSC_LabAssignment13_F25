import unittest

from class_3_initialization import House  # your class file


class TestHouse(unittest.TestCase):
    def test_class_attributes(self):
        """Verify class-level school attributes."""
        self.assertEqual(House.elementary_school, "FV Elementary")
        self.assertEqual(House.middle_school, "FV Middle")
        self.assertEqual(House.high_school, "FV High")

    def test_instance_default_attributes(self):
        """Verify instance attributes set in __init__."""
        h = House()
        self.assertEqual(h.plan, "Eden")
        self.assertEqual(h.size, 2000)

    def test_instances_are_independent(self):
        """Different instances should hold their own instance attributes."""
        h1 = House()
        h2 = House()

        h1.plan = "Custom A"
        h2.plan = "Custom B"

        self.assertEqual(h1.plan, "Custom A")
        self.assertEqual(h2.plan, "Custom B")
        self.assertNotEqual(h1.plan, h2.plan)

    def test_instance_can_override_class_attribute(self):
        """Instance can override a class attribute without altering the class."""
        h = House()
        h.elementary_school = "Holly Ridge Elementary"

        # instance sees overridden value
        self.assertEqual(h.elementary_school, "Holly Ridge Elementary")

        # class remains unchanged
        self.assertEqual(House.elementary_school, "FV Elementary")

        # new instance still sees original class attribute
        h2 = House()
        self.assertEqual(h2.elementary_school, "FV Elementary")


if __name__ == "__main__":
    unittest.main()
