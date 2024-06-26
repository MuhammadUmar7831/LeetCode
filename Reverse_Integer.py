#https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        st = str(x)
        neg = False
        if st[0] == "-": #to slice the minus if the number is negative and neg variable remember that x is negative
            st = st[1::]
            neg = True
        rtn = int(st[::-1]) # reverse the string
        if neg: #making number negative
            rtn = -1 * rtn

        if rtn > 2147483648 or rtn < -2147483648:  # checking 32 bit int contraint
            return 0
        return rtn
        