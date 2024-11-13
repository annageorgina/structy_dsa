def compress_one(s):
  ele_before = ''
  compressed = ''
  factor = 0
  for index, ele in enumerate(s):
    if ele == ele_before:
      factor += 1 
    else:
      compressed += factor_char(factor, ele_before)
      factor = 1
    ele_before = ele
    if index == len(s)-1:
      compressed += factor_char(factor, ele_before)
      
  return compressed


def factor_char(factor, ele_before):
  if factor > 1:
    return str(factor) + ele_before
  else:
    return ele_before




def compress(s):
  s += '!' # Token characters to cover last loop insead of doing another conditional loop
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[j] == s[i]:
      j += 1
    else:
      if j-i > 1:
        result.append(str(j-i))
      result.append(s[i])
      i = j    
  return ''.join(result)




# c c a a a t s s s
# 0 1 2 3 4 5 6 7 8 


def compress(s):
  s += '&'
  i = 0
  j = 0
  final = []
  while j < len(s):
    if s[i] != s[j]:
      if (j - i) > 1:
        final.append(str(j - i))
      final.append(s[i])
      i = j
    j += 1
  return ''.join(final)
      




































  


 
  

