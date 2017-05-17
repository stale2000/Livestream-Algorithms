#Find pair with given sum in the array

#finds pairs that add up to 10
def find_pair(arr):
  hash = {}
  for val in arr:
    if val not in hash:
      hash[val] = 0
    hash[val] += 1
  
  for val in arr:
    converse = 10 - val
    if converse in hash:
      if converse == val:
        if hash[converse] >= 2:
          return True
      elif hash[converse] >= 1:
        return True
  return False
        
    
  

print(1 if find_pair([8, 7, 2, 5, 1]) == True else 0)
print(1 if find_pair([2,8]) == True else 0)
print(1 if find_pair([10,0]) == True else 0)
print(1 if find_pair([5, 5]) == True else 0)
print(1 if find_pair([5, 1]) == False else 0)
print(1 if find_pair([10]) == False else 0)
print(1 if find_pair([1]) == False else 0)
print(1 if find_pair([]) == False else 0)
print(1 if find_pair([1,2,3,4]) == False else 0)
