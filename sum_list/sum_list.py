class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)


a.next = b
b.next = c
c.next = d
d.next = e


# 2 -> 8 -> 3 -> -1 -> 7


# Iterative
def sum_list_i(head):
  current = head
  my_sum = 0 
  while current is not None:
    my_sum += current.val
    current = current.next
  return my_sum


#Time O(n): n loops
# Space O(1): my_sum is created




# recursive
def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)
#Time O(n): n loops
# Space O(n): my_sum n iterations


# NOT MOST EFFICIENT
# recursive with helper 
# recursive
def sum_list_r_he(head):
  my_sum = 0
  return _sum_list_helper(head, my_sum)
  


def _sum_list_helper(head, my_sum):
  print('my_sum',my_sum)
  if head is None:
    return my_sum
  my_sum += head.val
  return _sum_list_helper(head.next, my_sum)
  
print(sum_list(a))




def sum_list(head):
  current = head 
  sum_vals = 0
  while current:
    sum_vals += current.val
    current = current.next 
  return sum_vals
# T O(n) while thorugh n
#S O(1) addition 


def sum_list(head):
  if head is None: 
    return 0 
  return head.val + sum_list(head.next)
# T O(n) n function calls 
# S O(n) n iteractions 













































