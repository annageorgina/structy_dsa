    return [ root.val ]  
  left_path = _path_finder(root.left, target)
  if left_path is not None:
    left_path.append(root.val)
    return left_path 
    
  right_path = _path_finder(root.right, target)
  if right_path is not None:
    right_path.append(root.val)
    return right_path
  
  return None
#Time O(n + n) = O

def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  return result[::-1]


def _path_finder(root, target):
  if root is None:
    return None
  if root.val == target:
    return [root.val]
  left_path = _path_finder(root.left, target)
  if left_path is not None:
    left_path.append(root.val)
    return left_path
  right_path = _path_finder(root.right, target)
  if right_path is not None:
    right_path.append(root.val)
    return right_path
  return None























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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# Recursivly think about what the return would be !! 

def path_finder(root, target):
  if root is None:
    return None
  if root.val == target:
    return [ root.val ]
    
  left_path = path_finder(root.left, target)
  if left_path is not None:
    return [root.val, *left_path] # unpacking list = O(n)
    
  right_path = path_finder(root.right, target)
  if right_path is not None:
    return [root.val, *right_path]
  
  return None
#Time O(n^2) append and recursion


def path_finder(root, target):
   result = _path_finder(root, target)
   if result is None:
     return None
   else:
    return result[::-1] #reverses a list in python


def _path_finder(root, target):
  if root is None:
    return None
  if root.val == target:
    return right_path
  
  return None
#Time O(n + n) = O


def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None




def _path_finder(root, target):
  if root is None:
    return None
  if root.val == target:
    return [root.val]
  left_path = _path_finder(root.left, target)
  if left_path is not None:
    left_path.append(root.val)
    return left_path
  right_path = _path_finder(root.right, target)
  if right_path is not None:
    right_path.append(root.val)
    return right_path
  return None













































