#https://leetcode.com/problems/two-sum/description/

#brute force (n^2)
# class Solution(object):
#     def twoSum(self, nums, target):
#         ans = []
#         for i in range(0, len(nums)):
#             print(nums[i])
#             for j in range(i + 1, len(nums)):
#                 if (nums[i] + nums[j] == target):
#                     ans.append(i)
#                     ans.append(j)
#                     return ans
 
 #fast solution O(n)
class Solution(object):
    def twoSum(self, nums, target):
        hash_table = {}
        nums_size = len(nums)
    
        for i in range(nums_size):
            hash_table[nums[i]] = i
    
        for i in range(nums_size):
            complement = target - nums[i]
        
            if complement in hash_table and hash_table[complement] != i:
                return [hash_table[complement], i]
    
        return []
               