#https://leetcode.com/problems/missing-number/submissions/1331674987/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1=0
        sum2=len(nums)
        for i in range(len(nums)):
            sum1 += nums[i]
            sum2 += i
        return sum2 - sum1
