#Write an efficient algorithm to compute the height of binary tree. The height or depth of a tree is number of edges or nodes on longest path from root node to leaf node.
#find tree height created by stale2000 - https://repl.it/IEHH/1

def find_h(node):
  left_h = 0
  right_h = 0
  if 'left' in node:
    left_h = find_h(node['left'])
  if 'right' in node:
    right_h = find_h(node['right'])

  return 1 + max(left_h, right_h)


print(1 if find_h({'left': {}, 'right': {}}) == 2 else 0)

print(1 if find_h({}) == 1 else 0)

print(1 if find_h({'left': {'left': {}}}) == 3 else 0)
print(1 if find_h({'right': {'right': {}}}) == 3 else 0)
print(1 if find_h({'left': {'right': {}}}) == 3 else 0)
