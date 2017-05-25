#1.2 Check Permutation created by stale2000 - https://repl.it/ISLE/0
#1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def check_perm(str1, str2):
  hash1 = {}
  hash2 = {}
  for val in str1:
    if val not in hash1:
      hash1[val] = 0
    hash1[val] += 1

  for val in str2:
    if val not in hash2:
      hash2[val] = 0
    hash2[val] += 1
  
  for val in hash1:
    if val not in hash2 or hash1[val] != hash2[val]:
      return False
      
  for val in hash2:
    if val not in hash1 or hash2[val] != hash1[val]:
      return False

  return True
    

print(1 if check_perm("a", "a") == True else 0)
print(1 if check_perm("aa", "a") == False else 0)
print(1 if check_perm("", "a") == False else 0)
print(1 if check_perm("acdefg", "gfedca") == True else 0)
print(1 if check_perm("acdefggf", "gfedca") == False else 0)
print(1 if check_perm("aabb", "aabb") == True else 0)
print(1 if check_perm("bb", "aabb") == False else 0)