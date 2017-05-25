#Given an array of integers, move all zeros present in the array to the end. The solution should maintain the relative order of items in the array.
# moves 0s to end of array created by stale2000 - https://repl.it/IEGJ/1

def move_zeros(arr):
  return_arr = []
  zero_arr = []
  
  for val in arr:
    if val == 0:
      zero_arr.append(val)
    else:
      return_arr.append(val)
  
  return return_arr + zero_arr

print(1 if move_zeros([10,0]) == [10,0] else 0)
print(1 if move_zeros([0]) == [0] else 0)
print(1 if move_zeros([2]) == [2] else 0)
print(1 if move_zeros([0, 2]) == [2, 0] else 0)
print(1 if move_zeros([0,1,0,0,0, 2]) == [1, 2, 0, 0, 0, 0] else 0)
print(1 if move_zeros([ 6, 0, 8, 2, 3, 0, 4, 0, 1 ]) == [6, 8, 2, 3, 4, 1, 0, 0, 0] else 0)
