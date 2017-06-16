#how you would replace space characters with URL-encoded “%20”.  That is: “Hello World Twitch” would become “Hello%20World%20Twitch”
#Twitch - replace space created by stale2000 - https://repl.it/Inid/1

def replace_space(string):
  str_arr = string.split(" ")
  return "%20".join(str_arr)


print(1 if replace_space("Hello World Twitch") == "Hello%20World%20Twitch" else 0)
print(1 if replace_space("Hello") == "Hello" else 0)
print(1 if replace_space("Hello\n") == "Hello\n" else 0)