# How do you check if 2 binary trees ( not binary search  trees, elements are not ordered) have at least one element in common
# Twitch elem_common_tree created by stale2000 - https://repl.it/InmM/1

def tree_elem_in_common(tree1, tree2):
  hash_tbl1 = {}
  make_hash(tree1, hash_tbl1)
  
  hash_tbl2 = {}
  make_hash(tree2, hash_tbl2)
  
  for key in hash_tbl1:
    if key in hash_tbl2:
      return True
  
  return False
  
def make_hash(node, hash_tbl):
  hash_tbl[node['val']] = True
  
  if 'left' in node:
    make_hash(node['left'], hash_tbl)
  if 'right' in node:
    make_hash(node['right'], hash_tbl)
  


print(1 if tree_elem_in_common({'val': 1, 'left': {'val': 2}, 'right': {'val': 3}}, {'val': 1, 'left': {'val': 2}, 'right': {'val': 20}}) == True else 0)
print(1 if tree_elem_in_common({'val': 99, 'left': {'val': 5}, 'right': {'val': 3}}, {'val': 1, 'left': {'val': 2}, 'right': {'val': 20}}) == False else 0)
print(1 if tree_elem_in_common({'val': 99}, {'val': 1, 'left': {'val': 2}, 'right': {'val': 99}}) == True else 0)
print(1 if tree_elem_in_common({'val': 99}, {'val': 1, 'left': {'val': 2}, 'right': {'val': 200}}) == False else 0)