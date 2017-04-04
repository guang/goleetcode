import pytest
from search_insert_position_gy import (
    find_insert_position,
    binary_search_find_insert_position,
)

dummy_data = [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([1, 3], 5, 2),
    ([1, 2, 4, 6, 7], 3, 2),
    ([1, ], 1, 0),
]


@pytest.mark.parametrize("numbers,target,expected_position", dummy_data)
def test_find_insert_position(numbers, target, expected_position):
    actual_position = find_insert_position(numbers, target)
    assert actual_position == expected_position


@pytest.mark.parametrize("numbers,target,expected_position", dummy_data)
def test_binary_search_find_insert_position(numbers, target, expected_position):
    actual_position = binary_search_find_insert_position(numbers, target)
    assert actual_position == expected_position
