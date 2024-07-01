#https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif x == 0:
            return 0
        neg = True if n < 0 else False
        if neg:
            n = -n
        result = 0
        if n % 2:
            result = self.myPow(x, (n-1)//2) 
            result *= result
            result *= x
        else:
            result = self.myPow( x, n//2)
            result *= result
        return 1 / result if neg else result
        
        
class Solution(object):
    def myPow(self, x, n):
        return x ** n #by using built in method
        