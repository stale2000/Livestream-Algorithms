#find kth end element linked list created by stale2000 - https://repl.it/IGTc/1
#find kth node from end of linked list
def kth_node(k, node):
  cur_node = node
  list_length = 0
  while True:
    list_length += 1
    if "next" not in cur_node:
      break
    cur_node = cur_node["next"]
  
  cur_node = node
  n = 0
  while n < list_length - k - 1:
    cur_node = cur_node["next"]
    n += 1
  
  return cur_node["val"]
  



print(1 if kth_node(1, {"val": 1, "next": {"val": 2}}) == 1 else 0)
print(1 if kth_node(0, {"val": 1, "next": {"val": 2}}) == 2 else 0)
print(1 if kth_node(0, {"val": 2}) == 2 else 0)
print(1 if kth_node(1, {"val": 1, "next": {"val": 2, "next": {"val": 3}}}) == 2 else 0)
print(1 if kth_node(2, {"val": 1, "next": {"val": 2, "next": {"val": 3}}}) == 1 else 0)
