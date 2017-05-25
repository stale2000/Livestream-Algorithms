#merge_two_arr_sorted created by stale2000 - https://repl.it/IOR9/0
def merge_sort_two_arrays(arr1, arr2):
  ptr1 = 0
  ptr2 = 0
  new_arr = []
  
  while(ptr1 < len(arr1) or ptr2 < len(arr2)):
    if (ptr1 < len(arr1) and (not  ptr2 < len(arr2) or arr1[ptr1] <= arr2[ptr2] )):
      new_arr.append(arr1[ptr1])
      ptr1 += 1
    if (ptr2 < len(arr2) and (not  ptr1 < len(arr1) or arr2[ptr2] <= arr1[ptr1] )):
      new_arr.append(arr2[ptr2])
      ptr2 += 1
  return new_arr

print(1 if merge_sort_two_arrays([1], [2]) == [1,2] else 0)
print(1 if merge_sort_two_arrays([1,3], [2]) == [1,2,3] else 0)
print(1 if merge_sort_two_arrays([1], [2,3,4,5]) == [1,2,3,4,5] else 0)
print(1 if merge_sort_two_arrays([1,2,5], [3,4]) == [1,2,3,4,5] else 0)
print(1 if merge_sort_two_arrays([], [3,4]) == [3,4] else 0)
