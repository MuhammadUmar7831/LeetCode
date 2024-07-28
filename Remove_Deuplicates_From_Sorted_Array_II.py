#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# better sapce O(n) time O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mapping = {}
        index = 0
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1
            if mapping[num] <= 2:
                nums[index] = num
                index += 1
        nums[index : ] = []
        return len(nums)
    
    
# optimal sapce O(1) time O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currCount = 0
        index = 0
        prev = None
        for num in nums:
            if num == prev:
                currCount += 1
            else:
                currCount = 1
            prev = num
            if currCount <= 2:
                nums[index] = num
                index += 1
        nums[index : ] = []
        return len(nums)