def find_insert_position(numbers, target):
    for i, val in enumerate(numbers):
        # FOUND THE MOFO
        # no mofo to be found, insert it now
        if val >= target:
            return i
    # mofo to be inserted at the very end
    return len(numbers)


def binary_search_find_insert_position(numbers, target):
    indices = list(range(len(numbers)))
    # edge case on either ends
    return binary_search_find_insert_position_recurse(numbers, indices, target)


def binary_search_find_insert_position_recurse(numbers, indices, target):
    # base case
    if len(numbers) == 1:
        if numbers[0] < target:
            return indices[0]+1
        else:
            return indices[0]

    # mid if odd, mid-1 if even
    mid_index = int(len(numbers)/2)
    mid_number = numbers[mid_index]
    if mid_number == target:
        return indices[mid_index]
    if mid_number > target:
        return binary_search_find_insert_position_recurse(numbers[:mid_index], indices[:mid_index], target)
    else:
        return binary_search_find_insert_position_recurse(numbers[mid_index:], indices[mid_index:], target)
