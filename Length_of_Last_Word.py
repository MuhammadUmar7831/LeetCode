#https://leetcode.com/problems/length-of-last-word/description/

#only oprimized solution no brute force solution
class Solution(object):
    def lengthOfLastWord(self, s):
        lastWordEnd = len(s) - 1
        
        # Skip trailing spaces
        while lastWordEnd >= 0 and s[lastWordEnd] == ' ':
            lastWordEnd -= 1
        
        length = 0
        
        # Count the length of the last word
        while lastWordEnd >= 0:
            if s[lastWordEnd] == ' ':
                break
            length += 1
            lastWordEnd -= 1
        
        return length
        