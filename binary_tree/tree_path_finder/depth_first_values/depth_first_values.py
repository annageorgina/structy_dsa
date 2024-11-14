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


#      a
#    /   \
#   b     c
#  / \     \
# d   e     f


def depth_first_values(root):
  if root is None:
    return []
    
  values = []
  stack = [root]
  while stack:
    current = stack.pop()
    values.append(current.val)
    if current.right is not None:
      stack.append(current.right)
    if current.left is not None:
      stack.append(current.left)
  return values
#n = number of nodes
#Time: O(n)
#Space: O(n)


def depth_first_values(root):
  if root is None:
    return []
  left_values = depth_first_values(root.left) # [b, d, e]
  right_values = depth_first_values(root.right) # [c, f]
  return [root.val, *left_values, *right_values]
  # splat operator = * adds the values into the list
  #return [root.val] + left_values + right_values
#n = number of nodes
#Time: O(n^2) - 2 recursive functions for each node
#Space: O(n)  
  


  
print(depth_first_values(a))








def depth_first_values(root):
  if root is None:
    return []
  stack = [root]
  values = []
  while stack:
    current = stack.pop()
    values.append(current.val)
    if current.right is not None:
      stack.append(current.right)


    if current.left is not None:
      stack.append(current.left)
  return values 


def depth_first_values(root):
  if root is None:
    return []
  return [root.val, *depth_first_values(root.left), *depth_first_values(root.right)]
    











































