#sub_arr_sum created by stale2000 - https://repl.it/IOVO/1

def sub_arr_sum(arr, k_sum):
  x=1
  start = 0
  end = 0
  while start < len(arr):
    sum = 0 
    while end < len(arr):
      sum += arr[end]
      if sum == k_sum:
        return True
      end += 1
    start +=1
    end = start
  return False

print(1 if sub_arr_sum([0], 1) == False else 0)
print(1 if sub_arr_sum([0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10], 15) == True else 0)
print(1 if sub_arr_sum([0, 5, -7, 1, -100, 7, 6, 1, 4, 1, 16], 15) == False else 0)
print(1 if sub_arr_sum([0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10], -3) == True else 0)
print(1 if sub_arr_sum([0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10], 1000) == False else 0)
print(1 if sub_arr_sum([0, 5, -7, 7, 6, 1, 4, 1, 10], -3) == False else 0)
