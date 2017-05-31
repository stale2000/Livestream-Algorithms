#2.1 remove all duplicates from the given linked list
def remove_dups(node):
  head = None
  cur_new_node = {}
  hash = {}
  
  cur_node = node
  while cur_node != None:
    if cur_node['val'] in hash:
      x=1
    else:
      new_node = {'val': cur_node['val']}
      hash[new_node['val']] = True
      if head == None:
        head= new_node
        cur_new_node = head
      else:
        cur_new_node['next'] = new_node
        cur_new_node = cur_new_node['next']
    
    if 'next' in cur_node:
      cur_node = cur_node['next']
    else:
      break
      
  return head

print(1 if remove_dups({"val": 1, "next": {"val": 2}}) == {"val": 1, "next": {"val": 2}} else 0)
print(1 if remove_dups({"val": 1, "next": {"val": 1}}) == {"val": 1} else 0)
print(1 if remove_dups({"val": 1, "next": {"val": 2, "next": {"val": 1}}}) == {"val": 1, "next": {"val": 2}} else 0)