#2.6 Find if a linked list is a palindrome
#palindrome_linked_list created by stale2000 - https://repl.it/ITvt/2

def palindrome_linked_list(node):
  
  prev_node = None
  cur_node = node
  while cur_node != None:
    new_node = {'val': cur_node['val']}
    if prev_node != None:
      new_node['next'] = prev_node
    prev_node = new_node
    
    if 'next' in cur_node:
      cur_node = cur_node['next']
    else:
      cur_node = None
  
  new_head = prev_node
  
  cur_node = node
  cur_rev_node = new_head
  
  while cur_node != None and cur_rev_node != None:
    if cur_node['val'] != cur_rev_node['val']:
      return False
    
    if 'next' in cur_node:
      cur_node = cur_node['next']
      cur_rev_node = cur_rev_node['next']
    else:
      cur_node = None
      cur_rev_node = None
  
  return True
  

print(1 if palindrome_linked_list({"val": 1, "next": {"val": 2}}) == False else 0)
print(1 if palindrome_linked_list({"val": 1, "next": {"val": 2, "next": {"val": 1}}}) == True else 0)
print(1 if palindrome_linked_list({"val": 1, "next": {"val": 2, "next": {"val": 2, "next": {"val": 1}}}}) == True else 0)
print(1 if palindrome_linked_list({"val": 1, "next": {"val": 2, "next": {"val": 2, "next": {"val": 3}}}}) == False else 0)