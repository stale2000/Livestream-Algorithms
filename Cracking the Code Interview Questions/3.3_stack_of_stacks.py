#3.3 Stacks of stacks.  Define a operations for a stack of stacks, that has a maximum amount of items that can be in each individual stack.  It should act like a normal stack.  Max items per stack = 3
#stack_of_stacks created by stale2000 - https://repl.it/IYgl/4

#sos=stack of stacks
def sos_push(stack, val):
  if len(stack) == 0:
    stack.append([val])
  elif len(stack[len(stack) - 1]) == 3:
    stack.append([val])
  else:
    stack[len(stack) - 1].append(val)
    
  return True

def sos_pop(stack):
  if len(stack) == 0:
    return False
  elif len(stack[len(stack) - 1]) == 1:
    last_stack = stack.pop()
    return last_stack.pop()
  else:
    return stack[len(stack) - 1].pop()
  

stack1 = []
print(1 if sos_push(stack1,1) == True else 0)
print(1 if sos_pop(stack1) == 1 else 0)
print(1 if sos_push(stack1,1) == True else 0)
print(1 if sos_push(stack1,2) == True else 0)
print(1 if sos_push(stack1,3) == True else 0)
print(1 if sos_push(stack1,4) == True else 0)
print(1 if sos_pop(stack1) == 4 else 0)
print(1 if sos_pop(stack1) == 3 else 0)
print(1 if sos_pop(stack1) == 2 else 0)
print(1 if sos_pop(stack1) == 1 else 0)
