class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")


a.next = b
b.next = c
c.next = d


#Iterative
def linked_list_values_it(head):
  current = head
  lis = []
  while current is not None:
    lis.append(current.val)
    current = current.next      
  return lis
# Time: O(n)
# Space = O(n)
# n = number of nodes
      


# Recursive
def linked_list_values_re(head):
  if head == None:
    return []
  elif head.next == None:
    return [head.val]


  return [head.val] + linked_list_values(head.next)
# Time: O(n^2) -> n function calls and n list concatenation
# Space = O(n^2) -> n function calls and n lists created
# n = number of nodes


# Recursive with helper function
def linked_list_values(head):
  values = []
  _linked_list_values_helper(head, values)
  return values


def _linked_list_values_helper(head, values):
  if head == None:
    return
  values.append(head.val)
  _linked_list_values_helper(head.next, values)
# Time: O(n)
# Space = O(n)
# n = number of nodes




def linked_list_values(root):
  current = root
  values = []
  while current is not None:
    values.append(current.val)
    current = current.next
  return values




print(linked_list_values(a))
  
  


















































print(linked_list_values(a))