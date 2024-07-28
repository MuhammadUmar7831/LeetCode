#https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rtn = []
        def helper(combo, snum):
            if len(combo) == k:
                rtn.append(combo)
                return
            for i in range(snum, n+1):
                helper(combo + [i], i + 1)
        helper([], 1)
        return rtn