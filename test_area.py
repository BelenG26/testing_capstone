from unittest import TestCase
import area

class TestShapeAreas(TestCase):

    def test_triangle_area(self):
        self.assertEqual(10, area.triangle_area(4, 5))

    def test_triangle_area_floating(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25,4.91))# almost equal for floating point numbers

    def test_negatice_base_height_raises_value_error(self):
        with self.assertRaises(ValueError):
            area.triangle_area(-3, 0)
        


