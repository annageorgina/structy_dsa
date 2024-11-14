def most_frequent_char(s):
  dict = {}
  for char in s:
    if char not in dict:
      dict[char] = 0
    dict[char] += 1


  best = None
  for char in dict:
    if best is None or dict[char] > dict[best]:
      best = char
    
  return best


## Time complexity O(n+n) = O(n)
## Space complexity O(n) we create a n dict 


























































def most_frequent_char(s):
  max_count = s[0] 
  char_map = { s[0]: 1}
  for i in s:
    if i not in char_map:
      char_map[i] = 0
    char_map[i] += 1
    if char_map[max_count] <= char_map[i]:
      max_count = i 
  return max_count


print(most_frequent_char('riverbed'))
  