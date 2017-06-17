#Do the classic coin collection problem on a 2-dimensional  grid, moving only right and down

 #= 21
def max_path(hash_tbl, grid, x,y):
  key = str(x) +" " + str(y)
  if key in hash_tbl:
    return hash_tbl[key]
  
  val = grid[x][y]
  down = 0
  right = 0
  
  if y + 1 < len(grid[x]):
    right = max_path(hash_tbl, grid, x,y + 1)
  if x + 1 < len(grid):
    down = max_path(hash_tbl, grid, x + 1,y)
  
  val += max(right, down)
  hash_tbl[key] = val
  
  return val
  

hash_tbl = {}
print(1 if max_path(hash_tbl,
    [[1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]], 0, 0) == 21 else 0)