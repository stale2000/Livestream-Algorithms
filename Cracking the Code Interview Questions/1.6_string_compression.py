#1.6 String Compression created by stale2000 - https://repl.it/ISOo/1
#1.6 String Compression: Compress a string, such that if there are repeated characters, the repeated characters are replace with the character, and the number of times that it is repeated.  EX: aaabb becomes a3,b2

def str_compress(string):
  return_str = ""
  
  prev_char = ""
  count = 0
  for val in string:
    if val != prev_char:
      if prev_char != "":
        return_str += prev_char
        return_str += str(count)
      prev_char = val
      count = 0
    count += 1
  if prev_char != "":
    return_str += prev_char
    return_str += str(count)
    
  
  if len(return_str) < len(string):
    return return_str
  else:
    return string

print(1 if str_compress("a") == "a" else 0)
print(1 if str_compress("aa") == "aa" else 0)
print(1 if str_compress("aabcccccaaa") == "a2b1c5a3" else 0)
print(1 if str_compress("aaa") == "a3" else 0)
print(1 if str_compress("aaabb") == "a3b2" else 0)
