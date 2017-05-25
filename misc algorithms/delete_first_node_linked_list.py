#Delete first node in linked list
#Delete first Node Linked List created by stale2000 - https://repl.it/IGTZ/1

def pop_node(node):
  #
  if "next" not in node:
    return None
  
  return node["next"]

print(1 if pop_node({"val": 1, "next": {"val": 2}}) == {"val": 2} else 0)

print(1 if pop_node({"val": 2}) == None else 0)
print(1 if pop_node({"val": 1, "next": {"val": 2, "next": {"val": 3}}}) == {"val": 2, "next": {"val": 3}} else 0)
