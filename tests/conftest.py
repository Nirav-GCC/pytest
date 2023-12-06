import pytest

import source.shapes as shapes


@pytest.fixture
def uni_rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def new_rectangle():
    return shapes.Rectangle(5, 7)
