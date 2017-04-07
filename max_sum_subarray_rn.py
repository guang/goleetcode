#!/bin/python3

def max_sum_subarray(array):
  if len(array) < 1:
    return
  ans = 0
  temp_sum = 0
  for i in array:
    temp_sum += i
    if temp_sum < 0:
      temp_sum = 0
    ans = max(ans, temp_sum)
  return ans
