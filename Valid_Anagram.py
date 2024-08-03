#https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping = {}
        for letter in s:
            mapping[letter] = mapping.get(letter, 0) + 1
        for letter in t:
            mapping[letter] = mapping.get(letter, 0) - 1
        for val in mapping.values():
            if val != 0:
                return False 
        return True
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        