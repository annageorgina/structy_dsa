      break
    prev = current
    current = current.next
  return head
# Time O(n) traversing though linked list
# SPace O(1) assigned one previous node 

# Think about it as a 'leap of faith' the head.next is assigned to the result of the recursive function !
def remove_node_A(head, target_val):
  if head is None:
    return head
  if head.val == target_val:
    return head.next
  head.next = remove_node_A(head.next, target_val)
  return head 
# Time O(n)
# Space O(n)    

  
      

print(remove_node(a, "c"))
print(c.val, c.next)
  
  



def remove_node(head, target):
  dummy_head = Node(None)
  prev = dummy_head
  current = head
  prev.next = current

  while current is not None:
    if current.val == target:
      prev.next = current.next
      break
    prev, current = current, current.next
  return dummy_head.next

#T O(n)
# S O(1)


def remove_node(head, target):
  if head is None:
    return head
  if head.val == target:
    return head.next
  head.next = remove_node(head.next, target)
  return head
# T O(n)
# S O(n)

  





















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

def remove_node_iterative(head, target_val):
  dummy_head = Node(None)
  if head.val == target_val:
    next = head.next
    head.next = None
    return next
  else:
    dummy_head.next = head
    prev = dummy_head
    current = head
    next = head.next if head is not None else None
    while current is not None:
      if current.val == target_val:
        prev.next = next
        current.next = None
        return dummy_head.next
      prev = current
      current = next
      next = next.next if next is not None else None
    return dummy_head.next

def remove_node(head, target_val, og_head = None, prev = None):
  if og_head is None:
    og_head = head if head.val != target_val else head.next
  if head is None:
    return og_head
  if head.val != target_val:
    remove_node(head.next, target_val, og_head, head)
  else:
    store_next = head.next
    head.next = None
    if prev is not None:
      prev.next = store_next
  return og_head
  print(head.val)

##### ABOVE I WAS ALSO TAKING OFF THE DELETED NODE FROM THE NEXT NODE! BUT iT ISN4T NECESSARILY NEEDED!! 

# here we only reroute the prev to the current.next
def remove_node_a(head, target_val):
  current = head 
  prev = None
  if head.val == target_val:
    return head.next
  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      break
    prev = current
    current = current.next
  return head
# Time O(n) traversing though linked list
# SPace O(1) assigned one previous node 

# Think about it as a 'leap of faith' the head.next is assigned to the result of the recursive function !
def remove_node_A(head, target_val):
  if head is None:
    return head
  if head.val == target_val:
    return head.next
  head.next = remove_node_A(head.next, target_val)
  return head 
# Time O(n)
# Space O(n)    

  
      

print(remove_node(a, "c"))
print(c.val, c.next)
  
  



def remove_node(head, target):
  dummy_head = Node(None)
  prev = dummy_head
  current = head
  prev.next = current


  while current is not None:
    if current.val == target:
      prev.next = current.next
      break
    prev, current = current, current.next
  return dummy_head.next


#T O(n)
# S O(1)




def remove_node(head, target):
  if head is None:
    return head
  if head.val == target:
    return head.next
  head.next = remove_node(head.next, target)
  return head
# T O(n)


  












































  

