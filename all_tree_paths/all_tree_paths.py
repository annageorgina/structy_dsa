class Node:
c.right = f
e.left = g
e.right = h
f.right = i

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

def all_tree_paths(root):
  paths = _all_tree_paths(root)
  for path in paths:
    path.reverse()
  return paths

# outer array - collection of mini paths
# inner array the path 
def _all_tree_paths(root):
  if root is None:
    return []
    
  if root.left is None and root.right is None:
    return [[root.val]]

  all_paths = [] 
  left_paths =  _all_tree_paths(root.left)
  for path in left_paths:
    path.append(root.val)
    all_paths.append(path)
    
  right_paths =  _all_tree_paths(root.right)
  for path in right_paths:
    path.append(root.val)
    all_paths.append(path)
    
  return all_paths
#Time: O( n*log(n) )
#Space: O( n*log(n) )



# Not efficient 
# this uses the [::-1] notation but it creates a new variable = not space efficent ! 
def all_tree_paths_Wrong(root):
  paths = all_tree_paths(root)
  reversed_paths = []
  for path in paths:
    reversed_paths.append(path[::-1])  # Append the reversed path to the new list
  return reversed_paths
  
###
def all_tree_paths(root):
  paths = _all_tree_paths(root)
  for path in paths:
    path.reverse()
  return paths


def _all_tree_paths(root):
  if root is None: 
    return []

  if root.left is None and root.right is None:
    return [[root.val]]
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
h = Node('h')
i = Node('i')

a.left = b
a.right = c
b.left = d
b.right = e
def all_tree_paths_Wrong(root):
  paths = all_tree_paths(root)
  reversed_paths = []
  for path in paths:
    reversed_paths.append(path[::-1])  # Append the reversed path to the new list
  return reversed_paths
  
###
def all_tree_paths(root):
  paths = _all_tree_paths(root)
  for path in paths:
    path.reverse()
  return paths




def _all_tree_paths(root):
  if root is None: 
    return []


  if root.left is None and root.right is None:
    return [[root.val]]
  
  all_paths = []
  
  left_paths = _all_tree_paths(root.left)
  for path in left_paths:
    path.append(root.val)
    all_paths.append(path)


  right_paths = _all_tree_paths(root.right)
  for path in right_paths:
    path.append(root.val)
    all_paths.append(path)


  return all_paths

















































