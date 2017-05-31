#3.5 Sort stack.  Sort a stack, using only another temp stack as your additional datastructure.  
#sort_stack created by stale2000 - https://repl.it/IYj4/3

def sort_stack(stack):
  temp_stack = []
  
  for x in range(0, len(stack)):
    largest = 0

    for num_left in range(0, len(stack) - x):
      val = stack.pop()
      if val > largest:
        largest = val
      temp_stack.append(val)

    stack.append(largest)
    added = False

    for num_left in range(0, len(temp_stack)):
      val = temp_stack.pop()
      if val == largest and not added:
        added = True
        continue
      stack.append(val)
  
  return list(reversed(stack))

print(1 if sort_stack([1,4,3,6,2,5]) == [1,2,3,4,5,6] else 0)
print(1 if sort_stack([6,5,4,3,2,1]) == [1,2,3,4,5,6] else 0)
print(1 if sort_stack([1,2,3,4,5,6]) == [1,2,3,4,5,6] else 0)
print(1 if sort_stack([1,1,3,6,2, 5]) == [1,1,2,3,5,6] else 0)