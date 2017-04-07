import pytest
from PROBLEM_USER import PROBLEM


test_data = [
    (),
]


@pytest.mark.parametrize('', test_data)
def test_PROBLEM():
    expected = None
    actual = PROBLEM()
    assert expected == actual
