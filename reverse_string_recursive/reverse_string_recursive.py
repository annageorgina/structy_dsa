

#recursive
def reverse_string(s):
  if len(s) == 0:
    return ''
  return reverse_string(s[1:]) + s[0]
  #return s[-1] + reverse_string(s[:-1]) CAN BE EITHER OR !!! 


# You can either add the last char to the fron tor the first char to the end


# Time O(n^2): n function calls & n slices made
# Space O(n^2):  n function calls and n substrings made


  
print(reverse_string("abcdefg"))


def reverse_string(str):
  i = 0
  j = len(str) - 1 
  str = list(str)
  while j >= i:
    str[i], str[j] = str[j], str[i]
    i += 1
    j -= 1
  return ''.join(str)


def reverse_string(text):
  text = list(text)
  if len(text) == 0:
    return ''
  return text.pop() + reverse_string(''.join(text))


def reverse_string(text):
  if len(text) == 0:
    return ''
  return reverse_string(text[1:]) + text[0]
  
print(reverse_string(""))   

































#non recursive = swap the characters
def reverse_string_brute(s):
  lis_s = list(s)
  i = 0
  j = len(lis_s)-1
  while j > i:
    lis_s[i], lis_s[j] = lis_s[j], lis_s[i]
    i += 1
    j -= 1
  return ''.join(lis_s)

#recursive
def reverse_string_one(s):
  s = list(s)
  if len(s) == 0:
    return ''
  str_of_list = ''.join((s[:-1]))
  return s[-1] + reverse_string(str_of_list)

































