def test_area(uni_rectangle):
    assert uni_rectangle.area() == 10 * 20


def test_perimeter(uni_rectangle):
    assert uni_rectangle.perimeter() == (10 * 2) + (20 * 2)


def test_new_rectangle(new_rectangle, uni_rectangle):
    assert new_rectangle != uni_rectangle
