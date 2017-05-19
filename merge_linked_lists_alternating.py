#Merge linked list alternating created by stale2000 - https://repl.it/IGUz/1
#Given two linked lists, merge their nodes together into first list by taking nodes alternately between the two lists
def merge_alt_lists(node1, node2):
  x=1
  new_list_head = {}
  
  cur_new_list = new_list_head
  while node1 is not None or node2 is not None:
    if node1 is not None:
      cur_new_list['val'] = node1['val']
      cur_new_list['next'] = {}
      prev_node = cur_new_list
      cur_new_list = cur_new_list['next']
      if 'next' in node1:
        node1 = node1['next']
      else:
        node1 = None

    if node2 is not None:
      cur_new_list['val'] = node2['val']
      cur_new_list['next'] = {}
      prev_node = cur_new_list
      cur_new_list = cur_new_list['next']
      if 'next' in node2:
        node2 = node2['next']
      else:
        node2 = None
  del prev_node['next']
  
  return new_list_head

print(1 if merge_alt_lists({"val": 1, "next": {"val": 2}}, {"val": 3, "next": {"val": 4}}) == {"val": 1, "next": {"val": 3, "next": {"val": 2, "next": {"val": 4}}}} else 0)
print(1 if merge_alt_lists({"val": 1}, {"val": 3}) == {"val": 1, "next": {"val": 3}} else 0)
print(1 if merge_alt_lists({"val": 1, "next": {"val": 2}}, {"val": 3}) == {"val": 1, "next": {"val": 3, "next": {"val": 2, }}} else 0)
