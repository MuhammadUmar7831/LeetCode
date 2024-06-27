#https://leetcode.com/problems/4sum/
#https://www.youtube.com/watch?v=fRJ7TitfanE

#O(n^3)
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        size = len(nums)
        lst = []
        
        for i in range(size - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, size - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, size - 1
                while k < l:
                    _sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if _sum == target:
                        lst.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1 
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1 
                        k += 1
                        l -= 1
                    elif _sum < target:
                        k += 1
                    else:
                        l -= 1
        
        return lst
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
#optimized
import bisect

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        nums = sorted(count)
        
        result = []
        
        start = 0
        end = len(nums) - 1
        
        if abs(target - nums[start]) < abs(target - nums[end]):
            end = bisect.bisect_right(nums, -(nums[start]*3) + target)
            if end == len(nums):
                end -= 1
        else:
            start = bisect.bisect_left(nums, -(nums[end]*3) + target)
        
        while start <= end:
            
            first_num = nums[start]
            adjusted_target = target - first_num
            count[first_num] -= 1
            
            if count[first_num] <= 0:
                start += 1
            
            for i in range(start, end + 1):
                num = nums[i]
                
                if count[num] > 1:
                    if adjusted_target - (2 * num) == num:
                        if num == first_num:
                            if count[num] >= 3:
                                count[num] = 3
                                result.append([num,num,num,num])
                        else:
                            if count[num] >= 3:
                                result.append([first_num,num,num,num])
                    else:            
                        if adjusted_target - (2 * num) in count and count[adjusted_target - (2 * num)] > 0:
                            result.append([first_num, num, num, adjusted_target - (2 * num)])

                    
                two_sum = -num
                
                left = bisect.bisect_left(nums, (two_sum - nums[-1]) - abs(adjusted_target), i + 1)
                right = bisect.bisect_right(nums, ((two_sum + adjusted_target) // 2), left)

                
                for k in range(left,right):
                    k_num = nums[k]
                    j = two_sum - k_num + adjusted_target
                    
                    if j in count and j != k_num and j != first_num and count[j] > 0:
                        result.append([first_num, num, k_num, j])
        
            if count[first_num] > 0:
                start += 1
            
            if start >= end:
                break
            
            if abs(nums[start]) < abs(nums[end]):
                end = bisect.bisect_right(nums, -(nums[start]*3) + target, start, end)
                if end == len(nums):
                    end -= 1
                
            else:
                start = bisect.bisect_left(nums, -(nums[end]*3) + target, start, end)
            
            count[first_num] = 0
        return result