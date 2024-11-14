class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


#Depth first
def tree_sum(root):
  if root is None:
    return 0
  left_sum = tree_sum(root.left)
  right_sum = tree_sum(root.right)
  return root.val + left_sum + right_sum
#Time: O(n)
#Space: O(n)


def tree_sum(root):
  stack = [root]
  sum = 0
  while stack:
    current = stack.pop()
    if current is not None:
      sum += current.val
      if current.left:
        stack.append(current.left)
      if current.right:
        stack.append(current.right)
  return sum


#breadth first
from collections import deque


def tree_sum(root):
  if root is None:
    return 0
  queue = deque([root])
  sum = 0
  while queue:
    current = queue.popleft()
    sum += current.val
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return sum
#Time: O(n)
#Space: O(n)


def tree_sum(root):
  if root is None:
    return 0
  stack = [root]
  sum = 0


  while stack:
    current = stack.pop()
    sum += current.val
    if current.left is not None:
      stack.append(current.left)
    if current.right is not None:
      stack.append(current.right)
  return sum















































