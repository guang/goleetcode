import pytest
from linked_list_cycle_gy import linked_list_cycle, linked_list_cycle_no_space
from data_structures import ListNode


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = b

d.next = e

test_data = [
    (None, False),
    (a, True),
    (d, False),
]


@pytest.mark.parametrize('head, has_cycle', test_data)
def test_linked_list_cycle(head, has_cycle):
    expected = has_cycle
    actual = linked_list_cycle(head)
    assert expected == actual


@pytest.mark.parametrize('head, has_cycle', test_data)
def test_linked_list_cycle_no_space(head, has_cycle):
    expected = has_cycle
    actual = linked_list_cycle_no_space(head)
    assert expected == actual
