#1.5 One Away created by stale2000 - https://repl.it/ISMs/2
#1.5 One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_away(str1, str2):
  edit_count = 0
  ptr1 = 0
  ptr2 = 0
  if abs(len(str1) - len(str2)) >= 2:
    return False
  while ptr1 < len(str1):
    if ptr1 >= len(str1) or ptr2 >= len(str2) or str1[ptr1] != str2[ptr2]:
      if len(str1) == len(str2):
        #char replace
        ptr1 += 1
        ptr2 += 1
        edit_count +=1
      elif len(str1) > len(str2):
        #char remove
        ptr1 += 1
        edit_count +=1
      elif len(str1) < len(str2):
        #char add
        ptr2 += 1
        edit_count +=1
    else:
      ptr1 += 1
      ptr2 += 1
    if edit_count > 1:
      return False
  
  return True

print(1 if one_away("aa", "a") == True else 0)
print(1 if one_away("aa", "aa") == True else 0)
print(1 if one_away("aaaa", "aa") == False else 0)
print(1 if one_away("bb", "aa") == False else 0)
print(1 if one_away("aa", "ab") == True else 0)
print(1 if one_away("aa", "aaa") == True else 0)
print(1 if one_away("aa", "aab") == True else 0)
print(1 if one_away("aa", "abb") == False else 0)