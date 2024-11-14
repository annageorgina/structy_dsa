class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def create_linked_list(values):
  if values is None or len(values) == 0:
    return None
  head = Node(values[0])
  current = head
  count = 0 
  while count < len(values) -1 :
    count += 1
    current.next = Node(values[count])
    current = current.next
  return head


def creat_linked_list(values):
  dummy_head = Node(values[0])
  tail = dummy_head
  for ele in values:
    tail.next = Node(ele)
    tail = tail.next
  return dummy_head


def create_linked_list(values):
  if len(values) == 0:
    return None
  new_node = Node(values[0])
  new_node.next = create_linked_list(values[1:])
  return new_node   
    
    


create_linked_list(["h", "e", "y"])






def create_linked_list(values):
  if len(values) == 0:
    return 
  index = 0
  head = Node(values[0])
  current = head
  while index < len(values)-1:
    new_node = Node(values[index + 1])
    current.next = new_node
    index += 1
    current = current.next
  return head


print(create_linked_list([]))















































