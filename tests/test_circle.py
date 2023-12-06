import math

import source.shapes as sp


class TestCircle:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = sp.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        results = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert results == expected
