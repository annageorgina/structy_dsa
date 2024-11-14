# Brute force
def palindrome_brute(s):
  i = 0 
  j = len(s)-1
  while j > i:
    if s[i] != s[j]:
      return False
    i += 1
    j -= 1
  return True


# Recursive
def palindrome(s):
  if len (s) == 0 or len(s) == 1:
    return True
  if s[0] == s[-1]:
    return palindrome(s[1:-1])
  return False


#Time O(n^2): n function calls & n string operations
# SPace O(n^2):n function calls & n subsstrings created




def palindrome(text):
  if len(text) <= 1:
    return True
  if text[0] != text[-1]:
    return False
  return palindrome(text[1:-1])


a = "kayak"
print(palindrome(a))











































