#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        start = 0 #start pointer
        end = len(nums)-1 #end pointer
        while start < end:
            mid = (start + end)//2 #finding mid
            if start == mid: #break in case the start and mid collide
                break
            if nums[mid] > nums[end]: #check if the right half is unsorted
                start = mid #select he right half
            else: #the left half is unsorted
                end = mid-1 #select left half

        return nums[end] if nums[end] < nums[start] else nums[start] #return max of start and end index
    
    
class Solution(object):
    def findMin(self, nums):
        start = 0 #start pointer
        end = len(nums)-1 #end pointer
        ans = nums[0] #take first index initially as answer
        while start <= end: #loop till end is greater than start
            mid = (start + end)//2 # find mid
            if nums[start] <= nums[mid]: #if left half is sorted
                ans = min(ans, nums[start]) #update min
                start = mid + 1 #eliminate left half (sorted half)
            else: # if right is sorted
                ans = min(ans, nums[mid]) #update min
                end = mid - 1 #eliminate right half (sorted half)
        return ans