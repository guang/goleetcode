def linked_list_cycle(head):
    node = head
    traversed_nodes = set()
    while node is not None:
        print 'at node {}'.format(node.val)
        if node in traversed_nodes:
            return True
        traversed_nodes.add(node)
        node = node.next
    return False


def linked_list_cycle_no_space(head):
    node1 = head
    if head is None or head.next is None:
        return False
    else:
        node2 = head.next
    while node2 is not None:
        print 'node1 {}'.format(node1.val)
        print 'node2 {}'.format(node2.val)
        # cycle: collision between the two pointers
        if node1 == node2:
            return True
        # node2 moves twice as fast
        node2 = node2.next
        # no cycle: node2 at the end
        if node2 is None:
            return False
        # move both
        node1 = node1.next
        node2 = node2.next
    return False
