#1.3 URLify created by stale2000 - https://repl.it/ISLL/1
#1.3 URLify: Write a method to replace all spaces in a string with '%20'. 

def urlify(string):
  return_str = ""
  
  for val in string:
    if " " == val:
      return_str += "%20"
    else:
      return_str += val
  
  return return_str

print(1 if urlify("") == "" else 0)
print(1 if urlify("a") == "a" else 0)
print(1 if urlify("aa") == "aa" else 0)
print(1 if urlify("a a") == "a%20a" else 0)
print(1 if urlify("a a ") == "a%20a%20" else 0)
print(1 if urlify(" ") == "%20" else 0)