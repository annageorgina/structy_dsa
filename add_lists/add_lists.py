    self.next = None


def add_lists(head_1, head_2, carry = 0):
  if head_1 is None and head_2 is None and carry == 0:
    return None
  val_1 = 0 if head_1 is None else head_1.val
  val_2 = 0 if head_2 is None else head_2.val
  digit = (val_1 + val_2 + carry) % 10
  next_carry = (val_1 + val_2 + carry) // 10
  new_list = Node(digit)
  
  next_1 = None if head_1 is None else head_1.next
  next_2 = None if head_2 is None else head_2.next
  
  new_list.next = add_lists(next_1, next_2, next_carry)
  return new_list


# Time O(max(n,m) -> need to go recursively through all the add_lists
# Space O(max(n,m)) -> need to create at least max(n,m) node + whatever is carried but O(n +100 ) = O(n)


def add_lists(head_1, head_2):
  dummy_head = Node(None)
  val_1 = 0 if head_1 is None else head_1.val
  val_2 = 0 if head_2 is None else head_2.val
  head = dummy_head
  print(head.val, head.next)
  carry = 0 
  while val_1 > 0 or val_2 > 0 or carry > 0:
    digit = (val_1 + val_2 + carry) % 10
    carry = (val_1 + val_2 + carry) // 10
    head.next = Node(digit)
    head_1 = None if head_1 is None else head_1.next
    head_2 = None if head_2 is None else head_2.next
    val_1 = 0 if head_1 is None else head_1.val
    val_2 = 0 if head_2 is None else head_2.val
    head = head.next
  return dummy_head.next


# Time O(max(n,m)) loop however many times according to how long longest linked list is
#Space O(max(n,m)) - need to create at least max(n,m) nodes (adding constant can be removed)










number = 326
last_digit = number % 10      # This gives 6
remaining_number = number // 10  # This gives 32
print(remaining_number)




a1 = Node(1)
a2 = Node(2)
a3 = Node(6)
a1.next = a2
a2.next = a3
# 1 -> 2 -> 6


b1 = Node(4)
b2 = Node(5)
b3 = Node(3)
b1.next = b2
b2.next = b3


def add_lists(head_1, head_2):
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1
  dummy_head = Node(None)
  prev = dummy_head
  remainder = 0


  while head_1 is not None or head_2 is not None or remainder != 0:
    addition = remainder
    if head_1 is not None:
      addition += head_1.val
    if head_2 is not None:
      addition += head_2.val
    digit = addition % 10
    remainder = addition // 10
    current = Node(digit)
    prev.next = current
    if head_1 is not None:
      head_1 = head_1.next
    if head_2 is not None:
      head_2 = head_2.next
    prev = current


  return dummy_head.next
  
print(add_lists(a1, b1))
  
  
  













































