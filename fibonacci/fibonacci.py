# 1, 1, 2, 3, 5, 8, 13, 21, …, each of which, 
# after the second, is the sum of the two previous numbers; that is, the nth Fibonacci number Fn = Fn − 1 + Fn − 2.


def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)
  
# Time: O(2^n) 2 recursion calls for each n = Exponential
# Space: O(n): Height of the recursion tree - represents maximum stack consumed





