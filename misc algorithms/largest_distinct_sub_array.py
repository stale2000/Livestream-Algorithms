#Find largest sub-array formed by consecutive distinct integers

def find_sub_arr(arr):
  hash = {}
  start = 0
  end = 0
  best_start = 0
  best_end = 0
  best_len = 1
  if len(arr) == 0:
    return []
  
  cur_start = 0
  cur_end = 0
  while cur_end < len(arr):
    
    if arr[cur_end] not in hash or hash[arr[cur_end]] == False:
      hash[arr[cur_end]] = True

      if 1 + cur_end - cur_start  > best_len:
        best_start = cur_start
        best_end = cur_end
        best_len = 1 + cur_end - cur_start
      cur_end += 1
    else:
      hash[arr[cur_start]] = False
      cur_start += 1
      
  return_arr = []
  x = best_start
  while x <= best_end:
    return_arr.append(arr[x]) 
    x += 1
  
  return return_arr
        

print(1 if find_sub_arr([ 2, 0, 2, 1, 4, 3, 1, 0 ]) == [ 0, 2, 1, 4, 3 ] else 0)
print(1 if find_sub_arr([ 1 ]) == [ 1 ] else 0)
print(1 if find_sub_arr([  ]) == [  ] else 0)
print(1 if find_sub_arr([ 1, 2, 3 ]) == [ 1, 2, 3] else 0)
print(1 if find_sub_arr([ 1, 2, 3, 2, 1 ]) == [ 1, 2, 3] else 0)
