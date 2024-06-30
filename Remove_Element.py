#https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i:i+1] = [] #delete the matching values
            else:
                i += 1
        return len(nums)
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
# shortcut syntax      
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        nums[:] = [x for x in nums if x != val]
        return len(nums)
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        