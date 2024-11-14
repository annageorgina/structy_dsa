

# Without using collections
def breadth_first_values(root):
  if root is None:
    return []
  queue = [root]
  values = [] 
  while queue:
    current = queue.pop(0)
    values.append(current.val)
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return values
#Time O(n^2) pop(0) has O(n) and then running O(n) 
#Space O(n) 

# using deque from collections !! -> double ended queue runs at O(1) time
from collections import deque  

def breadth_first_values_A(root):
  if root is None:
    return []
  queue = deque([root])
  current = root
  values = [] 
  while queue:
    current = queue.pop()
    values.append(current.val)
    if current.left is not None:
      queue.appendleft(current.left)
    if current.right is not None:
      queue.appendleft(current.right)
  return values

#Time O(n) 
#Space O(n)


#other method with popleft
def breadth_first_values(root):
  if root is None:
    return []
  queue = deque([root])
  current = root
  values = [] 
  while queue:
    current = queue.popleft()
    values.append(current.val)
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return values

# NO RECURSIVE VERSION IS POSSIBLE!!! 
  
print(breadth_first_values(a) )

from collections import deque
def breadth_first_values(root):
  if root is None:
    return []
  queue = deque([root])
  values = []

  while queue:
    current = queue.popleft()
    values.append(current.val)
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return values

























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

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
  values = [] 
  while queue:
    current = queue.popleft()
    values.append(current.val)
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return values


# NO RECURSIVE VERSION IS POSSIBLE!!! 
  
print(breadth_first_values(a) )


from collections import deque
def breadth_first_values(root):
  if root is None:
    return []
  queue = deque([root])
  values = []


  while queue:
    current = queue.popleft()
    values.append(current.val)
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return values













































