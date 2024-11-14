class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")


a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


# a -> b -> c -> d -> e -> f
# f -> e -> d -> c -> b -> a


#iterative
def reverse_list(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev, current = current, next
  return prev


#Time O(n) : while loop 
# Space O(1) only store 3 variables regardless of length of the linked list


def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)
#n = number of nodes
#Time: O(n)
#Space: O(n)






def reverse_list(head):
  previous = None
  current = head
  while current is not None:
    next = current.next
    current.next = previous
    previous, current = current, next
  return previous
# T O(n)
# S O(1)


def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev 
  return reverse_list(next, head)






def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)


print(reverse_list(a))
  
  
  
  
  














































  

