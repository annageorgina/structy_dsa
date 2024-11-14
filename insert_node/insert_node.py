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

def insert_node(head, value, index):
  current = head
  new_node = Node(value)
  if index == 0:
    new_node.next = head
    return new_node
  while index > 1 :
    current = current.next
    index -= 1
  new_node.next = current.next
  current.next = new_node 
  return head
# Tome O(n)
# SPace O(1)

def insert_node(head, value, index):
  if index == 0:
    new_node = Node(value)
    new_node.next = head
    return new_node
  if head is None:
    return None
  if index == 1:
    new_node = Node(value)
    store_next = head.next
    head.next = new_node
    new_node.next  = store_next
    return head
  store_next = insert_node(head.next, value, index-1)
  return head
#Time: O(n)
#Space: O(n)
  
def insert_node(head, val, index):
  new_node = Node(val)
  if index == 0:
    new_node.next = head
    return new_node

  current = head
  while current is not None:
    if index == 1:
      current.next, new_node.next = new_node, current.next
      return head
    index -=1
    current = current.next
  return head
# T O(n)
# S O(1)




def insert_node(head, val, index):
  if index == 0:
    new_node = Node(val)
    new_node.next =  head
    return new_node
  if head is None:
    return None
    
  if index == 1:
    new_node = Node(val)
    head.next, new_node.next = new_node, head.next
    return


  insert_node(head.next, val, index - 1)
  return head


# T O(n)
# S O(n)


      
  
  


print(insert_node(a, 'x', 2))













































