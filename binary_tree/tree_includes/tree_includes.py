class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


#Depth iteratively
def tree_includes(root, target):
  stack = [root]
  if root is None:
    return False
  while stack:
    current = stack.pop()
    if current.val == target:
      return True
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)
  return False
#Time O(n)
#Space O(n)


#Breadth
from collections import deque
def tree_includes(root,target):
  queue = deque([root])
  if root is None:
    return False 
  while queue:
    current = queue.popleft()
    if current.val == target:
      return True
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return False


#Time O(n) - while loop 
#Space O(n) - queue 


 #Depth - recursively
def tree_includes(root, target):
  if root is None:
    return False
  if root.val == target:
    return True
  return tree_includes(root.left, target) or tree_includes(root.right, target)








def tree_includes(root, target):
  if root is None:
    return False
  if root.val == target:
    return True
  return tree_includes(root.left, target) or tree_includes(root.right, target)















































