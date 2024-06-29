#https://leetcode.com/problems/jump-game-ii/

class Solution(object):
    def jump(self, nums):
        steps = 0
        i = 0
        while i < len(nums) - 1:
            next_jump = nums[i]

            if i + 1 + next_jump >= len(nums):
                return steps + 1

            j = i + 1
            _max = j
            temp = j
            while j <= i + next_jump:
                if j + nums[j] > _max:
                    _max = j + nums[j]
                    temp = j
                j += 1
            i = temp
            steps += 1
        return steps
