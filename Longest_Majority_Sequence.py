#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        umap = {}
        for num in nums:
            umap[num] = umap.get(num, 0) + 1
        
        mx = 1
        for num in nums:
            if umap.get(num, False):
                if not umap.get(num-1, False):# only check for those elements that can start a seqeunce
                    val = num + 1
                    l = 1
                    while umap.get(val, False):
                        val += 1
                        l += 1
                    mx = max(mx, l)
                
        return mx