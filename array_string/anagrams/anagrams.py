







def str_dict(s):
  dict = {}
  for char in s:
    if char not in dict:
      dict[char] = 0
    dict[char] += 1
  return dict


def anagrams(s1, s2):
  return str_dict(s1) == str_dict(s2)




# Time complexity O(n+m)
# Space complexity O(n+m)


def anagrams(str1, str2):
  if len(str1) != len(str2):
    return False
  map_str1 = _char_map(str1)
  map_str2 = _char_map(str2)
  return map_str1 == map_str2


def _char_map(str):
  map_letter = {}
  for i in str:
    if i not in map_letter:
      map_letter[i] = 0
    map_letter[i] += 1
  return map_letter

