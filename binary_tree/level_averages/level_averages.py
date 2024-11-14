

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


from collections import deque
def level_averages(root):
  if root is None:
    return []
  queue = deque([(root, 0)])
  level_avgs = []
  node_count = 0
  while queue:
    current, level_num = queue.popleft()
    if level_num == len(level_avgs):
      if level_num > 0:
        level_avgs[level_num - 1] = level_avgs[level_num - 1]/ node_count
        node_count = 0
      level_avgs.append(current.val)
    else: 
      level_avgs[level_num] += current.val
    node_count += 1
    
    if current.left is not None:
      queue.append((current.left, level_num + 1))
      
    if current.right is not None:
      queue.append((current.right, level_num + 1))


  level_avgs[-1] = level_avgs[-1]/node_count    


  
  return level_avgs


print(level_averages(a))


  




from statistics import mean


from collections import deque
def level_averages(root):
  if root is None:
    return []
  queue = deque([(root, 0)])
  level_sums = []
  node_count = 0
  while queue:
    current, level_num = queue.popleft()
    if level_num == len(level_sums):
      level_sums.append([current.val])
    else: 
      level_sums[level_num].append(current.val)
    node_count += 1
    
    if current.left is not None:
      queue.append((current.left, level_num + 1))
      
    if current.right is not None:
      queue.append((current.right, level_num + 1))   
  level_avgs = []
  for level in level_sums:
    level_avgs.append(mean(level))
  return level_avgs


print(level_averages(a))



































