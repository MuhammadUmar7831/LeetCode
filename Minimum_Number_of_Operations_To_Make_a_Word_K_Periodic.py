#https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

#brute force space: O(k) time: O(n/4)
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        noSubStr = len(word) // k
        mapping = {}
        i = 0
        mx = 0
        while i < len(word):
            mapping[word[i:i+k]] = mapping.get(word[i:i+k], 0) + 1
            if mx < mapping[word[i:i+k]]:
                mx = mapping[word[i:i+k]]
            i += k
        return noSubStr - mx
 
#same code written in short hand   
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        mapping = {}
        for i in range(0, len(word), k):
            mapping[word[i:i+k]] = mapping.get(word[i:i+k], 0) + 1
        
        return (len(word) // k) - max(mapping.values())