#1.6 String Compression created by stale2000 - https://repl.it/ISOo/1
#1.6 String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

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