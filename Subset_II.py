#https://leetcode.com/problems/subsets-ii/


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rtn = []
        def helper(curr ,index):
            curr.sort()
            if curr not in rtn:
                rtn.append(curr)
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                helper(curr+[nums[i]], i+1)
        helper([], 0)
        return rtn
    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rtn = []
        nums.sort()
        def helper(curr ,index):
            if curr not in rtn:
                rtn.append(curr)
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                helper(curr+[nums[i]], i+1)
        helper([], 0)
        return rtn
    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rtn = set()
        nums.sort()
        def helper(curr ,index):
            rtn.add(tuple(curr))
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                helper(curr+[nums[i]], i+1)
        helper([], 0)
        return rtn