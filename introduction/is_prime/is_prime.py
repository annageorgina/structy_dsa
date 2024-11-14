# To remember 
# % Remainder after division - the decimal part
# // modulus of division - the closest int 


from math import sqrt
def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
      return False
  return True




from math import sqrt
def is_prime(num):
  if num < 2:
    return False
  i = 2
  while i < int((sqrt(num)+1)):
    if num % i == 0:
      return False
    i += 1
  return True


#Time & Space: O(n) 
# (actually O(sqrt(n)) but simplifies to O(n))
  



























































