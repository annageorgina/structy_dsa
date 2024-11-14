def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)
#Time: O(n)
#Space: O(n)