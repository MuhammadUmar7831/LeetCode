#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

#brute force
class Solution(object):
    def removeDuplicates(self, nums):
        mapDic = {}
        index = 0
        for num in nums:
            if mapDic.get(num) == None: # check the flag if the number already present or not mapDic[num] give error so use get
                mapDic[num] = 1 #flag 1 for the number presence
                nums[index] = num #change the nums
                index += 1 #progress the index
        return len(mapDic) #length of dictionary is equal to the number of unique elements
        """
        :type nums: List[int]
        :rtype: int
        """
        
#optimize
class Solution(object):
    def removeDuplicates(self, nums):
        _index = 0 #keep track of the index to be modified
        for i in range(1, len(nums)):
            if nums[_index] != nums[i]: #check if the last modified index value is not equal to this i index value
                _index += 1 #increase the modified index first than modify list
                nums[_index] = nums[i]
        return _index + 1 # stores the number of unique elements
        """
        :type nums: List[int]
        :rtype: int
        """
        