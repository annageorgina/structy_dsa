def pair_product(numbers, target_product):
  key_map = {}
  for index, num in enumerate(numbers):
    complement = target_product/num
    if complement in key_map:
      return (key_map[complement], index)
    key_map[num] = index


# Time O(n)
# Space O(n)


















































def pair_product(nums, target):
  index_map = {}                                                     # { ele: index, .... }
  for i, ele in enumerate(nums):
    complement = target/ele
    if complement in index_map:
      return (index_map[complement], i)
    index_map[ele] = i 
  








print(pair_product([4, 7, 9, 2, 5, 1], 5))


































  