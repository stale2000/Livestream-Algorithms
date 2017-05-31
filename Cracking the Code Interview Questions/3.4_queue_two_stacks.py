#3.4  Make a queue with 2 stacks.  
#queue using 2 stacks created by stale2000 - https://repl.it/IYh8/4

def q_stack_enque(inbox, val):
  inbox.append(val)
  return True

def q_stack_deque(inbox, outbox):
  if len(outbox) == 0:
    for x in range(0, len(inbox)):
      outbox.append(inbox.pop())
      
  return outbox.pop()
    


stack_inbox = []
stack_outbox = []
print(1 if q_stack_enque(stack_inbox,1) == True else 0)
print(1 if q_stack_deque(stack_inbox, stack_outbox) == 1 else 0)
print(1 if q_stack_enque(stack_inbox, 10) == True else 0)
print(1 if q_stack_enque(stack_inbox, 3) == True else 0)
print(1 if q_stack_enque(stack_inbox, 4) == True else 0)
print(1 if q_stack_deque(stack_inbox, stack_outbox) == 10 else 0)
print(1 if q_stack_deque(stack_inbox, stack_outbox) == 3 else 0)
print(1 if q_stack_enque(stack_inbox, 9) == True else 0)
print(1 if q_stack_deque(stack_inbox, stack_outbox) == 4 else 0)
print(1 if q_stack_deque(stack_inbox, stack_outbox) == 9 else 0)