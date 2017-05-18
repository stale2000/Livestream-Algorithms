#Given an array of integers, find minimum sum sub-array of given size k.
#smallest sub arr of k created by stale2000 - https://repl.it/IEC7/1

def min_sum_array(k, arr):
  smallest = 0
  x = 0
  while x < k:
    smallest += arr[x]
    x += 1
  cur_sum = smallest
  
  while x < len(arr):
    cur_sum += arr[x]
    cur_sum -= arr[x-k]
    if cur_sum < smallest:
      smallest = cur_sum
    
    x += 1
  return smallest


print(1 if min_sum_array(1, [10,0]) == 0 else 0)
print(1 if min_sum_array(2, [10,0]) == 10 else 0)
print(1 if min_sum_array(2, [10,3]) == 13 else 0)
print(1 if min_sum_array(3, [10, 4, 2, 5, 6, 3, 8, 1]) == 11 else 0)
