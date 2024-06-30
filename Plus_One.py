#https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        carry = 0
        i = len(digits) - 1
        digits[i] += 1
        if digits[i] >= 10:
            carry += 1
            digits[i] = digits[i] % 10
        i -= 1
        while i > -1:
            digits[i] = digits[i] + carry
            if digits[i] >= 10:
                carry = digits[i] // 10
                digits[i] = digits[i] % 10
            else:
                carry = 0
            i -= 1
        if carry > 0:
            digits[:0] = [carry]
        return digits
    
    
class Solution(object):
    def plusOne(self, digits):
        s = ''.join(str(x) for x in digits)
        s = int(s) + 1
        s = str(s)
        s = [int(x) for x in s]
        return s
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        

class Solution(object):
    def plusOne(self, digits):
        return [int(x) for x in str(int(''.join(str(x) for x in digits)) + 1)]
        