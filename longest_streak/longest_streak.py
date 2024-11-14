  return longest_streak(head.next, max_streak, streak)
  
  
  

#print(longest_streak(a))


def longest_streak(head):
  current = head 
  max_streak = 0 
  streak = 1
  
  if current is None:
    return 0
  if current.next is None:
    return 1
    
  while current.next is not None:
    if current.val == current.next.val:
      streak+=1
      if max_streak < streak:
        max_streak = streak
    else: 
      streak = 1
    current = current.next
  return max_streak
# T O(n)
# S O(1)

def longest_streak(head):
  if head is None:
    return 0
  return _longest_streak(head)


def _longest_streak(head, max_streak=None, streak=None):
  if streak is None:
    streak = 1
  if max_streak is None:
    max_streak = streak
  if head.next is None:
    return max_streak
  if head.val == head.next.val:
    streak += 1
    if streak > max_streak:
      max_streak = streak
  else:
    streak = 1
  return _longest_streak(head.next, max_streak, streak)
    

def longest_streak(head):
  prev = None
  streak = 0
  max_streak = 0
  current = head

  while current is not None:
    if prev is None:
      streak = 1
      max_streak = 1
    elif prev.val == current.val:
      streak += 1
      if max_streak < streak:
        max_streak = streak
    elif prev.val != current.val:
      streak = 1
    prev, current = current, current.next
  return max_streak



print(longest_streak(a))
























class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9


def longest_streak_i(head):
  current = head 
  count = 1
  max_count = 0
  while current is not None:
    if current.next is not None and current.val == current.next.val:
      count += 1
    else:
      if count > max_count:
        max_count = count
      count = 1 
    current = current.next
  return max_count

def longest_streak_i2(head):
  current = head 
  prev_val = None
  streak = 0 
  max_streak = 0 
  while current is not None:
    if current.val == prev_val:
      streak += 1
    else:
      streak = 1
    prev_val = current.val
    max_streak = max(max_streak, streak)
    current = current.next
  return max_streak

#Time O(n) while loop
#Space: O(1)

def longest_streak(head, max_streak = 0, streak = 1):
  if head is None:
    return max_streak
  if head.next is None:
    return max(streak, max_streak)
  elif head.next.val == head.val:
    streak += 1
  else:
    max_streak = max(max_streak, streak)
    streak = 1
  max_streak = max(max_streak, streak)
  return longest_streak(head.next, max_streak, streak)
  
  
  

#print(longest_streak(a))


def longest_streak(head):
  current = head 
  max_streak = 0 
  streak = 1
  
  if current is None:
    return 0
  if current.next is None:
    return 1
    
  while current.next is not None:
    if current.val == current.next.val:
      streak+=1
      if max_streak < streak:
        max_streak = streak
    else: 
      streak = 1
    current = current.next
  return max_streak
# T O(n)
# S O(1)

def longest_streak(head):
  if head is None:
    return 0
  return _longest_streak(head)


def _longest_streak(head, max_streak=None, streak=None):
  if streak is None:
    streak = 1
  if max_streak is None:
    max_streak = streak
  if head.next is None:
    return max_streak
  if head.val == head.next.val:
    streak += 1
    if streak > max_streak:
      max_streak = streak
  else:
    streak = 1
  return _longest_streak(head.next, max_streak, streak)
    


def longest_streak(head):
  prev = None
  streak = 0
  max_streak = 0
  current = head


  while current is not None:
    if prev is None:
      streak = 1
      max_streak = 1
    elif prev.val == current.val:
      streak += 1
      if max_streak < streak:
        max_streak = streak
    elif prev.val != current.val:
    prev, current = current, current.next
  return max_streak






print(longest_streak(a))















































