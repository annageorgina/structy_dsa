# Basic brute force
def pair_sum_one(numbers, target_sum):
  for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
      if i == j:
        pass
      elif numbers[i] + numbers[j] == target_sum:
        return (i,j)
## Time complexity: O(n^2)
## Space complexity: constant O(1)


def pair_sum_two(numbers, target_sum):
  key_map= {}
  for num_index in range(0, len(numbers)):
    complement = target_sum - numbers[num_index]
    if complement in key_map:
      return(key_map[complement], num_index)
    else:
      key_map[numbers[num_index]] = num_index 


def pair_sum(numbers, target_sum):
  key_map= {}
  for index, num in enumerate(numbers):
    complement = target_sum - num
    if complement in key_map:
      return(key_map[complement], index)
    key_map[num] = index 


# Time O(n) 
# Space O(n)


     
    
    
    


  
  










































      
  


      