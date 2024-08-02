#https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i = 0
        small = []
        equal = []
        large = []
        while i < len(nums):
            if nums[i] < pivot:
                small.append(nums[i])
            elif nums[i] > pivot:
                large.append(nums[i])
            else:
                equal.append(nums[i])
            i+=1
        return small + equal + large