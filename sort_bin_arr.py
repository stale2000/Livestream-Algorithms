#sort_bin_arr created by stale2000 - https://repl.it/IOUV/1
def sort_bin_arr(arr):
  ptr1 = 0
  ptr2 = len(arr) - 1
  
  while ptr1 < ptr2:
    if arr[ptr1] == 0:
      ptr1 += 1
    elif arr[ptr2] == 1:
      ptr2 -= 1
    else:
      arr[ptr1] = 0
      arr[ptr2] = 1
      ptr1 += 1
      ptr2 -= 1
  
  return arr

print(1 if sort_bin_arr([0,0]) == [0,0] else 0)
print(1 if sort_bin_arr([1,0]) == [0,1] else 0)
print(1 if sort_bin_arr([0]) == [0] else 0)
print(1 if sort_bin_arr([]) == [] else 0)
print(1 if sort_bin_arr([1,1]) == [1,1] else 0)
print(1 if sort_bin_arr([0,0,0,0,1,1,1,0]) == [0,0,0,0,0,1,1,1] else 0)
print(1 if sort_bin_arr([1,1,1,1,1,0,0,0,0]) == [0,0,0,0,1,1,1,1,1] else 0)
