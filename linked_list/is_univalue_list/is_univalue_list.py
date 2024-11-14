class Node:
   def __init__(self, val):
     self.val = val
     self.next = None


a = Node(7)
b = Node(7)
c = Node(7)


a.next = b
b.next = c


def is_univalue_list_i(head):
  current = head
  while current is not None:
    if current.val != head.val:
      return False
    current = current.next
  return True


def is_univalue_list(head):
  if head.next is None:
    return True
  if head.val != head.next.val:
    return False
  return is_univalue_list(head.next)
  
    
    
print(is_univalue_list(a))




def is_univalue_list(head):
  current = head
  while current:
    if current.val != head.val:
      return False
    current = current.next
  return True




def is_univalue_list(head):
  if head.next is None:
    return True
  if head.val != head.next.val:
    return False
  return is_univalue_list(head.next)
  
  











































