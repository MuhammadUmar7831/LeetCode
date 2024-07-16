#https://leetcode.com/problems/sort-colors

class Solution(object):
    def sortColors(self, nums):
        dic = {}
        for n in nums:
            dic[n] = 1 if dic.get(n) == None else dic[n] + 1

        i = 0
        while dic.get(0):
            nums[i] = 0
            dic[0] -= 1
            i += 1
        
        while dic.get(1):
            nums[i] = 1
            dic[1] -= 1
            i += 1
        
        while dic.get(2):
            nums[i] = 2
            dic[2] -= 1
            i += 1

class Solution(object):
    def sortColors(self, nums):
        zero = 0
        one = 0
        for n in nums:
            if n == 0:
                zero += 1
            elif n == 1:
                one += 1
        i = 0
        while zero:
            nums[i] = 0
            zero -= 1
            i += 1
        
        while one:
            nums[i] = 1
            one -= 1
            i += 1 

        while i < len(nums):
            nums[i] = 2 
            i += 1      
            
class Solution(object):
    def sortColors(self, nums):
        nums.sort()