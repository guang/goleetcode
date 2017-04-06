#!/bin/python3

def max_product_subarray(array):
  if len(array) < 1:
    return
  curr_max = array[0]
  curr_min = array[0]
  prev_max = array[0]
  prev_min = array[0]
  ans = array[0]
  for i in range(1, len(array)):
    curr_max = max(array[i]*prev_max, array[i]*prev_min, array[i])
    curr_min = min(array[i]*prev_max, array[i]*prev_min, array[i])
    ans = max(ans, curr_max)
    prev_max = curr_max
    prev_min = curr_min
  return ans
