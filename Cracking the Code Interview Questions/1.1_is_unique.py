#1.1 Is Unique created by stale2000 - https://repl.it/ISJY/1
#1.1 Is Unique: Deterimine if a string has unique characters

def unique_chars(string):
  hash = {}
  
  for val in string:
    if val in hash:
      return False
    hash[val] = True
  
  return True
  
  
print(1 if unique_chars("a") == True else 0)
print(1 if unique_chars("aa") == False else 0)
print(1 if unique_chars("") == True else 0)
print(1 if unique_chars("acdefg") == True else 0)
print(1 if unique_chars("acdefggf") == False else 0)
