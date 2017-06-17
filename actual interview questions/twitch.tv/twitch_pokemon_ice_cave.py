# Pokemon ice cave question
#Imagine you are in the Pokemon game, in an ice cave puzzle.  You can move in any direction, but you slide, until you hit an obstacle.  What is the shortest amount of moves that you can do to get to the end

#this is breadth first search
# NOW, imagine that you want to find the smallest number of steps, that you have to take to get to the end

#this solution solves the shortest amount of steps, not moves!
from collections import deque
def min_steps(grid, x,y):
  
  queue = deque([])
  #popleft
  #append
  min_steps_so_far = None
  
  queue.append({'x':x, 'y':y, 'steps': 0})
  
  while(len(queue) > 0):
    new_queue = deque([])
    while(len(queue) > 0):
      loc = queue.popleft()
      if min_steps_so_far is not None and loc['steps'] >= min_steps_so_far:
        continue
      if grid[loc['x']][loc['y']] == 2:
        if min_steps_so_far is None:
          min_steps_so_far = loc['steps']
        elif loc['steps'] < min_steps_so_far:
          min_steps_so_far = loc['steps']
      else:
        #move right
        steps = 0
        for x_move in range(loc['x'], len(grid)):
          if x_move >= len(grid) - 1:
            break
          elif grid[x_move + 1][loc['y']] == 1:
            break
          elif grid[x_move][loc['y']] == 2:
            break
          steps += 1
        if steps > 0:
          new_queue.append({'x':x_move, 'y':loc['y'], 'steps': steps + loc['steps']})
        #move down 
        steps = 0
        for y_move in range(loc['y'], len(grid[loc['x']])):
          if y_move >= len(grid[loc['x']]) - 1:
            break
          elif grid[loc['x']][y_move + 1] == 1:
            break
          elif grid[loc['x']][y_move] == 2:
            break
          steps += 1
        if steps > 0:
          new_queue.append({'x':loc['x'], 'y':y_move, 'steps': steps + loc['steps']})
          
    queue = new_queue          
  
  return min_steps_so_far
      

print(1 if min_steps(
    [[0, 0, 1, 0],
    [0, 0, 2, 0],
    [1, 0, 0, 0]], 0, 0) == 3 else 0)