# Time: O(min(n, m))
# Space: O(1)  
 

# Recursive
def zipper_lists_r(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1
  pre_1_next = head_1.next   #b
  pre_2_next = head_2.next   #y
  # a.next,     x.next      = x,      zipperlist( (b->c), (y->z) )
  head_1.next , head_2.next = head_2, zipper_lists(pre_1_next, pre_2_next)
  # zipper_lists(b, y)
  return head_1
  
print(zipper_lists(a, x))
  


def zipper_list(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1
  next = head_1.next
  head_1.next = head_2
  zipper_list(head_2, next)
  return head_1


# T O(n) 
# S O(n)


def zipper_lists(head_1, head_2):
  ref_node = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0 
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      #even count - need to take a node from list 2
      ref_node.next = current_2 # a->x
      current_2 = current_2.next # transverse list 2 to y
    else:
      #odd count - need to take a node from list 1 
      ref_node.next = current_1 #x->b
      current_1 = current_1.next #transverse list 1 to c
    ref_node = ref_node.next
    count += 1
  if current_1 is not None:
    ref_node.next = current_1 #if 'leftovers' on lis1 add to the ref_node
  if current_2 is not None:
    ref_node.next = current_2 #if leftovers on lis2 add to the ref_node
  return head_1 



def zipper_node(head_1, head_2):
  ref_node = head_1
  current_1 = head_1.next
  current_2 = head_2 
  count = 0 
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      ref_node.next = current_2
      current_2 = current_2.next 
    else:
      ref_node.next = current_1
      current_1 = current_1.next
    count += 1
      
    
  

  return head_1
    
    
  
    
  

  
  



















x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

#iterative
def zipper_lists(head_1, head_2):
  ref_node = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0 
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      #even count - need to take a node from list 2
      ref_node.next = current_2 # a->x
      current_2 = current_2.next # transverse list 2 to y
    else:
      #odd count - need to take a node from list 1 
      ref_node.next = current_1 #x->b
      current_1 = current_1.next #transverse list 1 to c
    ref_node = ref_node.next
    count += 1
  if current_1 is not None:
    ref_node.next = current_1 #if 'leftovers' on lis1 add to the ref_node
  if current_2 is not None:
    ref_node.next = current_2 #if leftovers on lis2 add to the ref_node
  return head_1 
# n = length of list 1
# m = length of list 2
    if count % 2 == 0:
      #even count - need to take a node from list 2
      ref_node.next = current_2 # a->x
      current_2 = current_2.next # transverse list 2 to y
    else:
      #odd count - need to take a node from list 1 
      ref_node.next = current_1 #x->b
      current_1 = current_1.next #transverse list 1 to c
    count += 1
  if current_1 is not None:
    ref_node.next = current_1 #if 'leftovers' on lis1 add to the ref_node
  if current_2 is not None:
    ref_node.next = current_2 #if leftovers on lis2 add to the ref_node
  return head_1 






def zipper_node(head_1, head_2):
  ref_node = head_1
  current_1 = head_1.next
  current_2 = head_2 
  count = 0 
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      ref_node.next = current_2
      current_2 = current_2.next 
    else:
      ref_node.next = current_1
      current_1 = current_1.next
    count += 1
      
    
  


  return head_1
    
    
  
    
  


  
  

























