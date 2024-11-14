def five_sort_old(nums):
  num_fives = 0
  new = []
  for index, ele in enumerate(nums):
    if ele != 5:
      new.append(ele)
    else:
      num_fives += 1
  if num_fives > 0:
    new += num_fives * [5]
  return new
  
def five_sort(nums):
  i = 0
  j = len(nums)-1
  while j > i:
    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  return nums
#Time: O(n)
#Space: O(1)








def five_sort(nums):
  i = 0 
  j = len(nums) - 1
  while j > i:
    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] =  nums[j], nums[i]
    else:
      i += 1
  return nums







































