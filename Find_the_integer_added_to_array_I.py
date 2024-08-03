#https://leetcode.com/problems/find-the-integer-added-to-array-i

#space: O(1) time:O(nlog(n))
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        return nums2[0] - nums1[0]
    
#space: O(1) time: O(n+m)
def findMin(nums):
    _min = nums[0]
    for num in nums:
        if num < _min:
            _min = num
    return _min
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return findMin(nums2) - findMin(nums1)
    
#space: O(1) time:O(n+m)
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return (sum(nums2) - sum(nums1)) // len(nums1) 

#space: O(1) time:O(n)
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        sum = 0
        n = len(nums1)
        for i in range(n):
            sum = sum + nums2[i] - nums1[i]
        return sum // n