#https://leetcode.com/problems/permutations/

def helper(result, current, nums, size):
    if len(nums) == 0:
        result.append(current)
        return
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        helper(result, current + [nums[i]], new_nums, size)

class Solution(object):
    def permute(self, nums):
        result = []
        helper(result, [], nums, len(nums))
        return result
    

class Solution(object):
    def permute(self, nums):
        result = []
        def helper(current, nums):
            if len(nums) == 0:
                result.append(current)
                return
            for i in range(len(nums)):
                x = nums.pop(i)
                helper(current + [x], nums)
                nums.insert(i, x)
        
        helper([], nums)
        return result