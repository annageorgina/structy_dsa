class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(0)
f = Node(-13)
g = Node(-1)
h = Node(-2)


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h


# Root to leaf so needs to be depth first ! 
# Paths better to use recursively
def max_path_sum(root):
  if root is None:                                 # this makes sure empty path is not preferered over a path with negatives val nodes for example 
    return float("-inf")
  if root.left is None and root.right is None:     # this is leaf node! 
    return root.val
  max_right = max_path_sum(root.right)
  max_left = max_path_sum(root.left)
  return max(root.val + max_left, root.val + max_right)


# Time O(n) recursive call for each node of the tree (comparison so linear )
# Space O(n) due to call stack 


    
def max_path_sum(root):
  if root is None:
    return float('-inf')
  if root.left is None and root.right is None:
    return root.val
  left_max = max_path_sum(root.left)
  right_max = max_path_sum(root.right)
  return max(root.val + left_max, root.val + right_max)
  
  















































