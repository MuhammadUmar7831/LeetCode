#https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution(object):
    def findArray(self, pref):
        arr = [0] * len(pref)
        arr[0] = pref[0]
        for i in range(1, len(pref)):
            arr[i] = pref[i-1]^pref[i]
        return arr
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        