#2.5 Add up two linked lists that are in reverse order (1st digit is head)
#sum_list created by stale2000 - https://repl.it/ITus/2

def sum_list(node1, node2):
  return_node = {}
  carry = 0
  cur_node = None
  while node1 != None or node2 != None or carry != 0:
    dig1 = 0
    dig2 = 0
    if node1 != None:
      dig1 = node1['val']
      if 'next' in node1:
        node1 = node1['next']
      else:
        node1 = None
    if node2 != None:
      dig2 = node2['val']
      if 'next' in node2:
        node2 = node2['next']
      else:
        node2 = None
    sum_val = carry + dig1 + dig2
    new_node = {'val': sum_val % 10}
    carry = (sum_val - (sum_val % 10)) /10
    
    if return_node == {}:
      return_node = new_node
      cur_node = return_node
    else:
      cur_node['next'] = new_node
      cur_node = cur_node['next']
    
  
  return return_node


print(1 if sum_list({"val": 1, "next": {"val": 2}}, {"val": 1, "next": {"val": 2}}) == {"val": 2, "next": {"val": 4}} else 0)
print(1 if sum_list({"val": 9, "next": {"val": 8}}, {"val": 1, "next": {"val": 2}}) == {"val": 0, "next": {"val": 1, "next": {"val": 1}}} else 0)
print(1 if sum_list({"val": 1, "next": {"val": 2}}, {"val": 1}) == {"val": 2, "next": {"val": 2}} else 0)