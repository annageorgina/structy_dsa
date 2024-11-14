      tree_height += 1
      # If there are still nodes to process, add another level marker
      if queue:
        queue.append(None)
    else: 
      if current.left is not None:
        queue.append(current.left)
      if current.right is not None:
        queue.append(current.right)
  return tree_height - 1






  


print(how_high(a))


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

from collections import deque
def how_high(root):
  queue = deque([(root, 0)])
  if root is None:
    return -1 

  while queue:
    current, level_num = queue.popleft()
    if current.left is not None:
      queue.append((current.left, level_num + 1))
    if current.right is not None:
      queue.append((current.right, level_num + 1))
      
    

  return level_num
    


print(how_high(a))





















class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
def how_high(node):
  if node is None:
    return -1
  right_height = how_high(node.right)
  left_height = how_high(node.left)
  return 1 + max(right_height, left_height)
# time O(n)
# space O(n) call stack

from collections import deque
def how_high_A(node):
  if node is None:
    return -1
  if node.left is None and node.right is None:
    return 0
  queue = deque([node, None])
  tree_height = 0
  while queue:
    current = queue.popleft()
    if current is None:
      # End of a level, increment the height
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g


from collections import deque
def how_high(root):
  queue = deque([(root, 0)])
  if root is None:


  while queue:
    current, level_num = queue.popleft()
    if current.left is not None:
      queue.append((current.left, level_num + 1))
    if current.right is not None:
      queue.append((current.right, level_num + 1))
      
    


  return level_num
    




print(how_high(a))









































