#https://leetcode.com/problems/palindrome-number/description/

class Solution(object):
    def isPalindrome(self, x):
        if x < 0: #negative numbers are always palindrome
            return False
        _x = str(x) #converting x number to _x a string
        length = len(_x) #saving length so that len is not called multiple times

        for i in range(length // 2): #iterting half array
            if _x[i] != _x[length - i - 1]: #checking 1st with last 2nd with 2nd last...
                return False
        return True