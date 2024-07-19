#https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(combo, trg, index):
            if trg == 0:
                result.append(combo) # if the target for combo reaches 0 means it is a true combo
                return
            for i in range(index, len(candidates)):
                if trg - candidates[i] >= 0:#check for each candidate if it is capable of pickup or not
                    helper(combo + [candidates[i]], trg-candidates[i], index) #search for next pickable candidate in this combo
                index += 1 #increase to avoid duplicate combos
        helper([], target, 0)
        return result
        