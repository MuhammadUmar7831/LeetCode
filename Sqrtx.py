# https://leetcode.com/problems/sqrtx/

#brute force
class Solution(object):
    def mySqrt(self, x):
        if x <= 1: #return x for x = 1 and 0
            return x
        n = 1 #start from 1
        while n * n <= x: #iterate until you n square is less than or equal to x
            if n * n == x: #check square of every number
                return n 
            n += 1# increment
        return n - 1 #return n-1 to round down

#optimized
class Solution(object):
    def mySqrt(self, x):
        if x <= 1:
            return x 
        start = 1
        end = x
        while start < end: #binary search for sqrt
            mid = (start + end)// 2
            print(mid)
            if mid * mid > x:
                end = mid
            else:
                start = mid + 1
        return start-1
        """
        :type x: int
        :rtype: int
        """
        