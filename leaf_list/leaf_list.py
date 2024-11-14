  return leaves


# Time O(n)
# SPace O(n)


def leaf_list(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.val]
    return leaf_list(root.left) + leaf_list(root.right)


def leaf_list(root):
  leaves = []
  _leaf_list(root, leaves)
  return leaves


def _leaf_list(root, leaves):
  if root is None:
    return
  
  if root.left is None and root.right is None:
    leaves.append(root.val)
    
  _leaf_list(root.left, leaves)
  _leaf_list(root.right, leaves) 




print(leaf_list(a))






# DOES NOT WORK since we place the top level leaf first even if it isn't 'left first' !!!!! 
from collections import deque
def leaf_list_B(root):
  queue = deque([root])
  leaves = []


  if root is None:
    return []


  while queue:
    current = queue.popleft()
    if current.right is None and current.left is None:
      leaves.append(current.val)
      
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return leaves




def leaf_list(root):
  if root is None:
    return []
  stack = [root]
  leaves = []
  
  while stack:
    current = stack.pop()


    if current.right is None and current.left is None:
      leaves.append(current.val)


    if current.right is not None:
      stack.append(current.right)
    if current.left is not None:
      stack.append(current.left)
      
  return leaves
    













































