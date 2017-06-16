#Traverse an ordered binary tree with nodes containing  strings. Write a function for breadth first search traversal to find a string in the tree. 
#twitch search bin tree string created by stale2000 - https://repl.it/InjF/1

def search_tree_str(tree, string):
  
  cur_node = tree
  while cur_node != None:
    if cur_node['val'] == string:
      return True
    
    elif cur_node['val'] > string:
      if 'left' in cur_node:
        cur_node = cur_node['left']
      else:
        break
    else:
      if 'right' in cur_node:
        cur_node = cur_node['right']
      else:
        break
  
  return False
    


print(1 if search_tree_str({'val': "cat", 'left': {'val': "apple"}, 'right': {'val': "fox"}}, "apple" ) == True else 0)
print(1 if search_tree_str({'val': "cat", 'left': {'val': "apple"}, 'right': {'val': "fox"}}, "dog" ) == False else 0)
print(1 if search_tree_str({'val': "cat", 'left': {'val': "apple"}, 'right': {'val': "fox"}}, "fox" ) == True else 0)
