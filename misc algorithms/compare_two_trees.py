#Write an efficient algorithm to check if two binary trees are identical or not. i.e. if they have identical structure & their contents are also same.
#compare 2 trees created by stale2000 - https://repl.it/IEIA/1

def comp_tree(node1, node2):
  if node1['val'] != node2['val']:
    return False
  
  if 'left' in node1:
    if 'left' in node2:
      if comp_tree(node1['left'], node2['left']) == False:
        return False
    else:
      return False
  elif 'left' in node2:
    return False
  
  if 'right' in node1:
    if 'right' in node2:
      if comp_tree(node1['right'], node2['right']) == False:
        return False
    else:
      return False
  elif 'right' in node2:
    return False
  
  return True


print(1 if comp_tree({'val': 1, 'left': {'val': 2}, 'right': {'val': 3}}, {'val': 1, 'left': {'val': 2}, 'right': {'val': 3}}) == True else 0)
print(1 if comp_tree({'val': 1}, {'val': 1}) == True else 0)
print(1 if comp_tree({'val': 1}, {'val': 2}) == False else 0)
print(1 if comp_tree({'val': 1, 'left': {'val': 2}, 'right': {'val': 3}}, {'val': 1, 'left': {'val': 2}, 'right': {'val': 20}}) == False else 0)
print(1 if comp_tree({'val': 1, 'left': {'val': 30}, 'right': {'val': 3}}, {'val': 1, 'left': {'val': 2}, 'right': {'val': 3}}) == False else 0)
print(1 if comp_tree({'val': 1, 'left': {'val': 2}, 'right': {'val': 3}}, {'val': 7, 'left': {'val': 2}, 'right': {'val': 3}}) == False else 0)
print(1 if comp_tree({'val': 1, 'left': {'val': 2}, 'right': {'val': 3}}, {'val': 1}) == False else 0)

