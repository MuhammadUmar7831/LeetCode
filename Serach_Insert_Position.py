#https://leetcode.com/problems/search-insert-position/

#brute force O(n)
# class Solution(object):
#     def searchInsert(self, nums, target):
#         index = 0
#         for i in range(0, len(nums)): # iterating the whole list
#             if (nums[i] >= target):
#                 return index
#             else:
#                 index+=1 # incrementing index till the nums[i] reaches the number equal to the target or number grater than target
#         return index

#optimized solution O(log n) simple binary search
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid  # Target found, return its index
            elif nums[mid] < target:
                left = mid + 1  # Target is in the right half
            else:
                right = mid - 1  # Target is in the left half

        return left  # Target not found, return the insert position
        