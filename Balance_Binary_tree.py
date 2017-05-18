#check if a tree is a balance binary tree
#Balance Binary tree created by stale2000 - https://repl.it/IEJc/1

def bal_tree(node):
  tree_h_obj = bal_tree_finder(node)
  if tree_h_obj['max_h'] - tree_h_obj['min_h'] > 1:
    return False
  else:
    return True
  

def bal_tree_finder(node):
  left_obj = {'min_h': 0, 'max_h': 0}
  right_obj = {'min_h': 0, 'max_h': 0}
  
  if 'left' in node:
    left_obj = bal_tree_finder(node['left'])

  if 'right' in node:
    right_obj = bal_tree_finder(node['right'])

  min_h = 1 + min(left_obj['min_h'], right_obj['min_h'])
  max_h = 1 + max(left_obj['max_h'], right_obj['max_h'])

  return {'min_h': min_h, 'max_h': max_h}



print(1 if bal_tree({'left': {}, 'right': {}}) == True else 0)
print(1 if bal_tree({}) == True else 0)
print(1 if bal_tree({'left': {'left': {}}}) == False else 0)
print(1 if bal_tree({'right': {'right': {}}}) == False else 0)
print(1 if bal_tree({'left': {'right': {}}}) == False else 0)
print(1 if bal_tree({'right': {}, 'left': {'left': {}}}) == True else 0)
print(1 if bal_tree({'right': {}, 'left': {'left': {'right': {}}}}) == False else 0)

