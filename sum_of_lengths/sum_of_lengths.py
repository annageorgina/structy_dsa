

# Brute force
def sum_of_lengths_brute_force(strings):
  all_len = 0
  for i in strings:
    all_len += len(i)
  return all_len
# Time & Space O(n) -> for loop of n 


#recursivly
def sum_of_lengths(strings):
  if len(strings) == 0:
    return 0
  return len(strings[0]) + sum_of_lengths(strings[1:])
#Time: O(n^2)
#Space: O(n^2)























































