#https://leetcode.com/problems/string-to-integer-atoi/

#brute force
class Solution(object):
    def myAtoi(self, s):
        numerals = { #dictionary to check if the charecter is numeral or not
            '1': True,
            '2': True,
            '3': True,
            '4': True,
            '5': True,
            '6': True,
            '7': True,
            '8': True,
            '9': True,
            '0': True,
        }
        specials = {#dictionary to check if the charecter is one of these or not
            '+': True,
            '-': True,
            ' ': True
        }
        rtn = 0 #retu
        neg = False
        index = 0
        for char in s:
            if numerals.get(char) != None:
                rtn = (rtn * 10) + int(char)
            elif specials.get(char) == True:
                if index > 0:
                    break
                else:
                    neg = True if char == '-' else False
            else:
                break
            if char != ' ':
                index += 1
        print(rtn)
        rtn = -1 * rtn  if neg else rtn
        return 2147483647 if rtn >= 2147483648 else -2147483648 if rtn <= -2147483648 else rtn
        """
        :type s: str
        :rtype: int
        """
        
#optimized
class Solution(object):
    def myAtoi(self, s):
        i = 0
        size = len(s)
        while i < size and s[i] == ' ':
            i += 1
        rtn = 0
        if size <= i:
            return 0
        neg = False
        if s[i] == '-':
            neg = True
            i += 1
        elif s[i] == '+':
            i += 1
        while i < size:
            if s[i].isdigit():
                rtn = (rtn * 10) + int(s[i])
            else:
                break
            i += 1
        rtn = -1 * rtn if neg else rtn
        return 2147483647 if rtn >= 2147483648 else -2147483648 if rtn <= -2147483648 else rtn
        """
        :type s: str
        :rtype: int
        """
        