#https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/submissions/1308925632/

#brute force
class Solution(object): #return max number from the string
    def minPartitions(self, n):
        rtn = int(n[0])
        for s in n:
            if int(s) > rtn:
                rtn = int(s)
        return rtn
        """
        :type n: str
        :rtype: int
        """

class Solution(object):
    def minPartitions(self, n):
        return int(max(n))
        """
        :type n: str
        :rtype: int
        """

class Solution(object):
    def minPartitions(self, n):
        if "9" in n:
            return 9
        elif "8" in n:
            return 8
        elif "7" in n:
            return 7
        elif "6" in n:
            return 6
        elif "5" in n:
            return 5
        elif "4" in n:
            return 4
        elif "3" in n:
            return 3
        elif "2" in n:
            return 2
        elif "1" in n:
            return 1
        elif "0" in n:
            return 0
        