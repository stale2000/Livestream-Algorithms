#Linked List Palindrome created by stale2000 - https://repl.it/IGWs/1
#Given a linked list, check if linked list is palindrome or not.
#racecar

def check_palindrome(node):
  rev_arr = reverse(node)
  
  x=0
  while x < len(rev_arr):
    if rev_arr[x] != node['val']:
      return False
    
    x += 1
    if 'next' in node:
      node = node['next']
  
  return True

def reverse(node):
  new_arr = []
  if "next" in node:
    new_arr = reverse(node['next'])
  new_arr.append(node['val'])
  return new_arr
    

print(1 if check_palindrome({"val": 1, "next": {"val": 2}}) == False else 0)
print(1 if check_palindrome({"val": 1}) == True else 0)
print(1 if check_palindrome({"val": 1, "next": {"val": 1}}) == True else 0)
print(1 if check_palindrome({"val": 1, "next": {"val": 2, "next": {"val": 1}}}) == True else 0)
print(1 if check_palindrome({"val": 1, "next": {"val": 2, "next": {"val": 3}}}) == False else 0)
