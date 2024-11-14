class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


a = Node(3)
b = Node(11)
c = Node(10)
d = Node(4)
e = Node(-2)
f = Node(1)


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


# Breadth first !!! 
# first breadth goes through the levels and then it goes from the left to the right
from collections import deque
def bottom_right_value(root):
  queue = deque([root])
  while queue:
    current = queue.popleft()
    current_val = current.val
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return current_val
#Time: O(n)
#Space: O(n)    


from collections import deque
def bottom_right_value(root):
  queue = deque([(root, 0)])


  while queue:
    current, level_num = queue.popleft()


    if current.left is not None:
      queue.append((current.left, level_num + 1))
    if current.right is not None:
      queue.append((current.right, level_num + 1))




  return current.val
















































  