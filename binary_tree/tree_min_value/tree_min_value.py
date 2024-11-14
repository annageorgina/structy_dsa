class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def tree_min_value(root):
  stack = [root]
  min_val = root.val
  while stack:
    current = stack.pop()
    min_val = min(current.val, min_val)
    if current.left:
      stack.append(current.left)
    if current.right:
      stack.append(current.right)
  return min_val


def tree_min_value(root, min_val = None):
  if root is None:
    return min_val
  if min_val is None:
    min_val = root.val
  left_min = tree_min_value(root.left, root.val)
  right_min = tree_min_value(root.right, root.val)
  return min(left_min, right_min)


def tree_min_value_A(root):
  if root is None:
    return float("inf")
  left_min = tree_min_value(root.left)
  right_min = tree_min_value(root.right)
  return min(root.val, left_min, right_min)


from collections import deque
def tree_min_value_A(root):
  queue = deque([root])
  min_value = root.val
  while queue:
    current = queue.pop()
    min_value = min(current.val, min_value)
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return min_value




def tree_min_value(root):
  if root is None:
    return None
  queue = deque([root])


  min_val = root.val
  while queue:
    current = queue.popleft()
    if current.val < min_val:
      min_val = current.val


    if current.left is not None: 
      queue.append(current.left)
    if  current.right is not None:
      queue.append(current.right)


  return min_val













































