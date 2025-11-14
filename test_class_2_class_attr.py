import unittest

from class_2_class_attr import House


class TestHouse(unittest.TestCase):
    def test_class_attributes_exist(self):
        """Check the class-level attributes."""
        self.assertEqual(House.city, "Cary")
        self.assertEqual(House.community, "Palm River")
        self.assertEqual(House.builder, "Python")

    def test_instances_share_class_attributes(self):
        """Class attributes should be accessible from all instances."""
        h1 = House()
        h2 = House()

        self.assertEqual(h1.city, "Cary")
        self.assertEqual(h2.city, "Cary")

        # They should refer to the same class variable
        self.assertIs(h1.__class__.city, h2.__class__.city)

    def test_instance_override_class_attribute(self):
        """Instance can override class attribute without modifying the class itself."""
        h = House()
        h.city = "Raleigh"  # override at instance level

        # instance override
        self.assertEqual(h.city, "Raleigh")

        # class remains unchanged
        self.assertEqual(House.city, "Cary")

        # new instance still sees class value
        h2 = House()
        self.assertEqual(h2.city, "Cary")


if __name__ == "__main__":
    unittest.main()
