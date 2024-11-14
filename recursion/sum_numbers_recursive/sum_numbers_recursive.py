

# Recursive = larger O
def sum_numbers_recursive(numbers):
  if len(numbers) == 0:
    return 0
  return numbers[0] + sum_numbers_recursive(numbers[1:])


def sum_numbers_recursive(nums):
  if nums == []:
    return 0
  num = nums.pop()
  return num + sum_numbers_recursive(nums)


#Time O(n^2) because n function calls and slicing time n 
#Space O(n^2) because n function calls and subarray length n 




def sum_numbers(numbers):
  a = 0
  for i in numbers:
    a += i
  return a


# O(n) 'for' array loop










############################################################
def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)






  











































