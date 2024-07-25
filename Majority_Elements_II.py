#https://leetcode.com/problems/majority-element-ii

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        el1 = None
        el2 = None
        c1 = 0
        c2 = 0
        for num in nums:
            if el1 and num == el1:
                c1 += 1
            elif el2 and num == el2:
                c2 += 1
            elif c1 == 0:
                c1 = 1
                el1 = num
            elif c2 == 0:
                c2 = 1
                el2 = num
            else:
                c1 -= 1
                c2 -= 1

        c1 = c2 = 0
        for num in nums:
            if num == el1:
                c1 += 1
            elif num == el2:
                c2 += 1
        
        rtn = []
        if c1 > n // 3:
            rtn.append(el1)
        if c2 > n // 3:
            rtn.append(el2)
        return rtn

        