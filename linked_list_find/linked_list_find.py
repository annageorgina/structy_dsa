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


# Iterative
def linked_list_find_i(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True
    current = current.next
  return False
#Time O(n) loop of n 
# Space O(1) assigning n times 'current' to the same variable aka 1
  


# Recursive
def linked_list_find(head, target):
  if head is None:
    return False
  if head.val == target:
    return True
  return linked_list_find(head.next, target)


# Time O(n) n funtion calls 
# Space O(n) add the calls to the call stack








def linked_list_find(head, target):
  current = head 
  while current:
    if current.val == target:
      return True
    current = current.next
  return False 













































