def two_sum(nums, target):
    for i, i_val in enumerate(nums):
        for j, j_val in enumerate(nums[i+1:]):
            if i_val + j_val == target:
                return [i, i+1+j]


def two_sum_linear_time(nums, target):
    counterpart = {}
    for i, val in enumerate(nums):
        if val in counterpart:
            return [counterpart[val], i]
        else:
            counterpart[target-val] = i
