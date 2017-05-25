#overlapping_interval_join created by stale2000 - https://repl.it/IORr/1
def interval_join(arr):
  return_arr = []
  
  if len(arr) <= 0:
    return []
  
  x = 0 
  cand_start = arr[x]['start']
  cand_end = arr[x]['end']
  x += 1

  while x < len(arr):
    if arr[x]['end'] <= cand_end:
      #do Nothing
      y= 1
    elif arr[x]['start'] <= cand_end:
      cand_end = arr[x]['end']
    else:
      return_arr.append({'start': cand_start, 'end': cand_end})
      cand_start = arr[x]['start']
      cand_end = arr[x]['end']
    
    x += 1
  
  return_arr.append({'start': cand_start, 'end': cand_end})
  return return_arr
    

print(1 if interval_join([{'start':1, 'end':3}, {'start':2, 'end':3}]) == [{'start':1, 'end':3}] else 0)
print(1 if interval_join([{'start':1, 'end':3}, {'start':3, 'end':3}]) == [{'start':1, 'end':3}] else 0)
print(1 if interval_join([{'start':1, 'end':3}, {'start':3, 'end':5}]) == [{'start':1, 'end':5}] else 0)
print(1 if interval_join([{'start':1, 'end':3}, {'start':4, 'end':5}]) == [{'start':1, 'end':3}, {'start':4, 'end':5}] else 0)
print(1 if interval_join([{'start':1, 'end':3}, {'start':4, 'end':5}]) == [{'start':1, 'end':3}, {'start':4, 'end':5}] else 0)
print(1 if interval_join([{'start':1, 'end':5}, {'start':2, 'end':3},{'start':4, 'end':6},{'start':7, 'end':8}, {'start':8, 'end':10}, {'start':12, 'end':15}]) == [{'start':1, 'end':6}, {'start':7, 'end':10}, {'start':12, 'end':15}] else 0)


