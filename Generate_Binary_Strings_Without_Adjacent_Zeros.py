#https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

def backTrack(_str, rslt, n):
    if len(_str) == n:
        rslt.append(_str)
        return
    backTrack(_str + "1", rslt, n)
    if len(_str) == 0 or _str[-1] == "1":
        backTrack(_str + "0", rslt, n)
class Solution(object):
    def validStrings(self, n):
        result = []
        backTrack("", result, n)
        return result