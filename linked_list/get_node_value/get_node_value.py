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
def get_node_value_i(head, index):
  current = head
  current_index = 0
  while current is not None:
    if current_index == index:
      return current.val
    current = current.next
    current_index += 1
  return None
#Time O(n) n loops 
#Space O(1) onmy assign current_index & current and mutate the same variable


#Recursive
def get_node_value(head, index):
  if index == 0 :
    return head.val
  if head is None:
    return None
  return get_node_value(head.next, index - 1)


# Time O(n) n functions called
# Space O(n) storing each call on the call stack (remember they go backwards too)
    


# a -> b -> c -> d
# 0    1    2    3
# b -> c -> d
# 0    1    2 
# c -> d
# 0    1 


def get_node_value(head, target):
  current = head 
  while target > 0:
    target -= 1
    if current.next is not None:
      current = current.next
    else:
      return None
  return current.val
# T O(n)
# S O(1) onmy assign current




def get_node_value(head, target):
  if head is None:
    return None
  if target == 0:
    return head.val 
  return get_node_value(head.next, target - 1)
# T O(n)
# S O(n) call stack




    
  















































