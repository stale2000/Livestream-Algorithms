#3.2 min stack.  Implement a stack with min operations, push, and pop.
#min stack created by stale2000 - https://repl.it/IYfs/6

def min_stack_push(stack, val):
  if len(stack) == 0:
    obj = {'val': val, 'min_so_far': val}
  else:
    obj = {'val':val, 'min_so_far': min(val, min_stack_min(stack))}
  
  stack.append(obj)
    
  return True

def min_stack_pop(stack):
  if len(stack) > 0:
    return stack.pop()['val']

def min_stack_min(stack):
  if len(stack) > 0:
    return stack[len(stack) - 1]['min_so_far']

stack1 = []
print(1 if min_stack_push(stack1,1) == True else 0)
print(1 if min_stack_min(stack1) == 1 else 0)
print(1 if min_stack_pop(stack1) == 1 else 0)
print(1 if min_stack_push(stack1, 10) == True else 0)
print(1 if min_stack_push(stack1, 3) == True else 0)
print(1 if min_stack_min(stack1) == 3 else 0)
print(1 if min_stack_push(stack1, 4) == True else 0)
print(1 if min_stack_min(stack1) == 3 else 0)
print(1 if min_stack_pop(stack1) == 4 else 0)
print(1 if min_stack_pop(stack1) == 3 else 0)
print(1 if min_stack_min(stack1) == 10 else 0)