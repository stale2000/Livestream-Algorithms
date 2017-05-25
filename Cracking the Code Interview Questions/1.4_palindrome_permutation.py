#1.4 Palindrome Permutation created by stale2000 - https://repl.it/ISLp/1
#1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
def palin_perm(string):
  hash = {}
  
  for val in string:
    if val not in hash:
      hash[val] = 0
    hash[val] += 1
  
  odd_count = 0
  
  for val in hash:
    if hash[val] % 2 == 1:
      odd_count += 1
  
  if len(string) % 2 == 0 and odd_count > 0:
    return False
  if len(string) % 2 == 1 and odd_count != 1:
    return False
  
  return True
  

print(1 if palin_perm("a") == True else 0)
print(1 if palin_perm("aa") == True else 0)
print(1 if palin_perm("aaa") == True else 0)
print(1 if palin_perm("aba") == True else 0)
print(1 if palin_perm("aaac") == False else 0)
print(1 if palin_perm("adcc") == False else 0)
print(1 if palin_perm("rrdaa") == True else 0)