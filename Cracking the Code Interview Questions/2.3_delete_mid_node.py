#2.3 Delete a given middle node in a linked list
#delete_mid_node created by stale2000 - https://repl.it/ITup/0

def delete_mid_node(node):
  
  node['val'] = node['next']['val']
  
  if 'next' in node['next']:
    node['next'] = node['next']['next']
  else:
    del node['next']
  
  
  return


node1 = {"val": 1, "next": {"val": 2, "next": {"val": 3}}}
delete_mid_node(node1['next'])
print(1 if node1 == {"val": 1, "next": {"val": 3}} else 0)

node2 = {"val": 1, "next": {"val": 2, "next": {"val": 3, "next": {"val": 4}}}}
delete_mid_node(node2['next'])
print(1 if node2 == {"val": 1, "next": {"val": 3, "next": {"val": 4}}} else 0)