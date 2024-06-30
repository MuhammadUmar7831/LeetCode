#https://leetcode.com/problems/search-in-rotated-sorted-array/description/

#brute force
class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while(left<right):
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid
            
            if nums[left]>nums[right]:
                # mid in pivot and target in pivot
                if nums[mid]>=nums[left] and target>=nums[left]:
                    if nums[mid]>target:
                        right = mid
                    else:
                        left = mid + 1
                    

                # mid in pivot and target not in pivot
                elif nums[mid]>=nums[left] and target<nums[left]:
                    left = mid + 1

                # mid not in pivot target not in pivot
                elif nums[mid]<nums[left] and target<nums[left]:
                    if nums[mid]>target:
                        right = mid
                    else:
                        left = mid + 1

                # mid not in pivot target in pivot
                elif nums[mid]<nums[left] and target>=nums[left]:
                    right = mid
                
                else:
                    right = mid

            else:
                if nums[mid]<target:
                    left = mid + 1
                else:
                    right = mid

        
        if nums[left]==target:
            return left
        return -1
        