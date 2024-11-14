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

# breadth - Me 
from collections import deque
def tree_levels(root):
  if root is None:
    return []
  queue = deque([root, None])
  all_levels = []
  level = []
  while queue:
    current = queue.popleft()
    if current is None:
      all_levels.append(level)
      level = []
      if len(queue) != 0:
        queue.append(None)
    else:
      level.append(current.val)
      if current.left is not None:
        queue.append(current.left)
        
      if current.right is not None:
        queue.append(current.right)
  return all_levels

# breadth - Alvin
def tree_levels(root):
  if root is None:
    return []

  queue = deque([(root, 0)])
  levels = []
  while queue:
    current, level_num = queue.popleft()

    if len(levels) == level_num:
      levels.append([current.val])
    else:
      levels[level_num].append(current.val)

    if current.left is not None:
      queue.append((current.left, level_num + 1))
    if current.right is not None:
      queue.append((current.right, level_num + 1))
    
  return levels

# depth iterative
def tree_levels(root):
  if root is None:
    return []
  all_levels = []
  stack = [(root, 0)]
  while stack:
    current, level_num = stack.pop()
    if len(all_levels) == level_num:
      all_levels.append([current.val])
    else:
      all_levels[level_num].append(current.val)
      
    if current.left is not None:
      stack.append((current.left, level_num + 1))
      
    if current.right is not None:
      stack.append((current.right, level_num + 1))
    
  return all_levels

# depth recursive
def tree_levels(root):
  all_levels = []
  level_num = 0
  _tree_levels(root, all_levels, level_num)
  return all_levels


def _tree_levels(root, all_levels, level_num):
  if root is None:
    return []

  if level_num == len(all_levels):
    all_levels.append([root.val])
  else:
    all_levels[level_num].append(root.val)

  _tree_levels(root.left, all_levels, level_num + 1)
  _tree_levels(root.right, all_levels, level_num + 1)
  
    
    
    
 
print(tree_levels(a))


from collections import deque
def tree_levels(root):
  if root is None:
    return []
  queue = deque([(root, 0)])
  all_levels = []
  while queue:
    current, level_num = queue.popleft()
    if len(all_levels) == level_num:
      all_levels.append([current.val])
    else:
      all_levels[level_num].append(current.val)
    if current.left is not None:
      queue.append((current.left, level_num + 1))
    if current.right is not None:
      queue.append((current.right, level_num + 1))
  return all_levels




print(tree_levels(a))
  
    
  














































  