#For a given binary tree, assign the sibling pointer of each node. A sibling is always the node to its immediate right on the same level of the tree.
#Twitch sibling tree linked list created by stale2000 - https://repl.it/InkD/1

from collections import deque
def sib_tree(tree):
  queue = deque([])
  #.popleft()
  #.append()
  
  return_arr = []
  queue.append(tree)
  
  while len(queue) > 0:
    new_queue = deque([])
    linked_head = None
    cur_node = None
    while len(queue) > 0:
      pop_node = queue.popleft()
      new_node = {'val': pop_node['val']}
      
      if linked_head == None:
        linked_head = new_node
        cur_node = linked_head
      else:
        cur_node['next'] = new_node
        cur_node = new_node
      
      if 'left' in pop_node:
        new_queue.append(pop_node['left'])
      if 'right' in pop_node:
        new_queue.append(pop_node['right'])
    if linked_head != None:
      return_arr.append(linked_head)
    queue = new_queue
  return return_arr
  
  

print(1 if sib_tree({'val': 1, 'left': {'val': 2}, 'right': {'val': 3}}) == [{'val': 1}, {'val': 2, 'next': {'val': 3}}] else 0)
print(1 if sib_tree({'val': 1, 'right': {'val': 3}}) == [{'val': 1}, {'val': 3}] else 0)
print(1 if sib_tree({'val': 1, 'left': {'val': 2, 'left': {'val':4}}, 'right': {'val': 3}}) == [{'val': 1}, {'val': 2, 'next': {'val': 3}}, {'val': 4}] else 0)
print(1 if sib_tree({'val': 1, 'left': {'val': 2, 'right': {'val':4}}, 'right': {'val': 3, 'right': {'val':6}}}) == [{'val': 1}, {'val': 2, 'next': {'val': 3}}, {'val': 4, 'next': {'val':6}}] else 0)

