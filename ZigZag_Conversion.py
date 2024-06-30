#https://leetcode.com/problems/zigzag-conversion/


def down_jump (numRows, currentRow): #downwards jump
    return (numRows - currentRow) * 2 - 1
def up_jump (numRows, currentRow): #upwards jump
    return ( 2 * (currentRow - 1) ) - 1
class Solution(object):
    
    def convert(self, s, numRows):
        if numRows == len(s) or numRows == 1: #extreme cases
            return s
        result  = ""
        #first row #handle the downwards jump for first as first row only make down jump
        i = 0
        currentRow = 1
        # down_jump = (numRows - currentRow) * 2 - 1
        # up_jump = ( 2 * (currentRow - 1) ) - 1
        while i < len(s):
            result += s[i]
            i = i + down_jump(numRows, currentRow) + 1

        #handle up and down both jumps because mid rows do both of them
        currentRow += 1
        i = 1
        while currentRow < numRows: 
            down_flag = True
            while i < len(s):
                result += s[i]
                if down_flag:
                    i = i + down_jump(numRows, currentRow) + 1
                    down_flag = False
                else:
                    i = i + up_jump(numRows, currentRow) + 1
                    down_flag = True
            currentRow += 1
            i = currentRow - 1

        #last row #handle the upwards jump for last row as last row only make down jump
        currentRow = numRows
        i = currentRow - 1
        while i < len(s):
            result += s[i]
            i = i + up_jump(numRows, currentRow) + 1
        return result
        """
        total rows =  3 | 3 | 4 | 4
        current row = 1 | 2 | 1 | 2
        downwards jump = (total rows - current row) * 2 - 1
        upwards jump = 2 * ( current row - 1) - 1
        :type s: str
        :type numRows: int
        :rtype: str
        """
        