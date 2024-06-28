# https://leetcode.com/problems/rotate-array/


# optimized
class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        poped = nums[-k::]
        del nums[-k::]
        nums[0:0] = poped
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

# optimized
class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        if k == 0: #return if no rotate
            return
        nums[:0] = nums[-k:] # add the last k elements before start
        nums[-k:] = [] #skip from start to last elemets and replace the rest array with empty array 


#another appraoch
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        poped = nums[-k:] # store the last k elements to be added at start
        nums[k:] = nums[:-k] # skip first k elements and replace the rest of array from start to last k element in end
        nums[:k] = poped #replace the first k elements with poped
