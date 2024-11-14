e = Node(6)
f = Node(12)


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12


# When using Recursivly think about what the return would be !! 
#depth recursively
def tree_value_count(root, target):
  if root is None:
    return 0
  left_tree = tree_value_count(root.left, target)
  right_tree = tree_value_count(root.right, target)
  match = 1 if root.val == target else 0 
  return match + left_tree + right_tree
#Time O(n)
#Space O(n)


#depth iteratively
def tree_value_count(root, target):
  if root is None:
    return 0
  stack = [root]
  count = 0 
  while stack:
    current = stack.pop()
    if current.val == target:
      count += 1 
    if current.left is not None:
      stack.append(current.left)
    if current.right is not None:
      stack.append(current.right)
  return count




#breadth
from collections import deque
def tree_value_count_A(root, target):
  if root is None:
    return 0
  queue = deque([root])
  count = 0
  while queue:
    current = queue.popleft()
    if current.val == target:
      count += 1
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return count 
#Time O(n)
#Space O(n)
  
print(tree_value_count(a,  12))




def tree_value_count(root, target):
  stack = [root]
  if root is None:
    return 0
  count = 0 


  while stack:
    current = stack.pop()
    if current.val == target:
      count += 1


    if current.right is not None:
      stack.append(current.right)
    if current.left is not None:
      stack.append(current.left)


  return count













































