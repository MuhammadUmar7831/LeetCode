#https://leetcode.com/problems/jump-game/description/

#optimized
class Solution(object):
    def canJump(self, nums):
        last_good_step = len(nums) - 1 # contain the good step from the end from we can reach end initiated with last step
        for i in range(len(nums) - 2, -1, -1): # for loop to iterate backwards
            if i + nums[i] >= last_good_step: # check if the current step can be a last good step
                last_good_step = i
        return last_good_step == 0 #return true if last good step is the initial step otherwise false
        """
        :type nums: List[int]
        :rtype: bool
        """
        