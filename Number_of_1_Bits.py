#https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        count = 1 # initialize with because for each binary number there is atleast one on(1 value bit) bit
        while n>1: # while n is greater than 1
            count+=n%2 # add the reminder in count (add 1 if bit is otherwise 0 causing no change)
            n//=2 # integer divide the number
        return count
        
        
class Solution(object):
    def hammingWeight(self, n):
        return len((str(bin(n)).replace("0", "").replace("b", "")))#convert number to binary using bin than typecast to str than replace 0's and b's with empty string and return length of string