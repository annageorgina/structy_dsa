def uncompress_one(s):
  temp = ''
  for index, ele in enumerate(s):
    if index % 2 == 0:
      temp += int(ele)* (s[index+1])
  return temp


# Above doesn't work since the pattern isn't always 1 number 1 char ! 


def uncompress_two(s):
  temp = ''
  factor = ''
  for index, ele in enumerate(s):
    if ele.isalpha():
      temp += int(factor)*ele
      factor = ''
    else:
      factor +=ele
  return temp




def uncompress(s):
  numbers='0123456789'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      result.append(int(s[i:j]) * s[j])
      j += 1
      i = j 
  return ''.join(result) 


















  
# n number of groups of alpha and number
# m max number of the group
# Time complexity O(nm)
# SPace Complexity O(nm)




def uncompress(str):
  i = 0
  j = 0
  numbers = "123456789"
  final = []
  while j < len(str):
    if str[j] not in numbers:
      final.append( int(str[i:j]) * str[j])
      j+= 1
      i = j 
    else:
      j+= 1
  return ''.join(final)


print(uncompress("2c3a1t"))
    


      
      
  

















































