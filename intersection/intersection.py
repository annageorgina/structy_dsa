# Not efficient enough ! 
def intersection(a, b):
  a = set(a)
  b = set(b)
  a_min = min(a)
  a_max = max(a)
  b_min = min(b)
  b_max = max(b)
  a_min = a_max < b_max
  inter = []
  if a_max < b_min or a_min > b_max :
    inter = []
  elif a_min:
    for element in a: 
      if b_min <= element <= a_max and element in b:
        inter.append(element)
  else:
    for element in a:
      if a_min <= element <= b_max and element in b:
        inter.append(element)  
  return inter
##########################################################################################


def intersection_b(a, b):
  set_a = set(a)
  return [ item for item in b if item in set_a ]
#Time: O(n+m)
#Space: O(n)


def intersection(lis_a, lis_b):
  set_a = set(lis_a)
  set_b = set(lis_b)
  final = []
  for ele in set_a:
    if ele in set_b:
      final.append(ele)
  return final 



















































