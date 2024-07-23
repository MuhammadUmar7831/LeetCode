#https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            maximum = max(curr_sum, maximum)
            if curr_sum < 0:
                curr_sum = 0
                
        return maximum
        