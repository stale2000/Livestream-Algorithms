#Function to check if a number is prime. Function to find the prime factors of a number.  Find ALL the prime numbers up to N
#Twitch is_prime created by stale2000 - https://repl.it/IpZw/2

def create_sieve(n):
  arr = {}
  for x in range(2, n + 1):
    arr[x] = []
  
  for x in range(2, n + 1):
    if arr[x] == []:
      iter_prime = 2 * x 
      while iter_prime <= n:
        arr[iter_prime].append(x)
        iter_prime += x
  
  return arr
      

def get_factors(n, sieve):
  if n <= 1:
    return "not prime"
  
  if sieve[n] == []:
    return "prime"
  else:
    return sieve[n]


sieve = create_sieve(100)
print(1 if get_factors(1, sieve) == "not prime" else 0)
print(1 if get_factors(2, sieve) == "prime" else 0)
print(1 if get_factors(3, sieve) == "prime" else 0)
print(1 if get_factors(4, sieve) == [2] else 0)
print(1 if get_factors(6, sieve) == [2,3] else 0)
print(1 if get_factors(8, sieve) == [2] else 0)
print(1 if get_factors(15, sieve) == [3,5] else 0)