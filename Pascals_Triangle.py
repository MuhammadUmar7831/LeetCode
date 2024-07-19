#https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            rtn = [[1], [1, 1]]
            for i in range(2, numRows):
                l = [1]*(i+1)
                j = 1
                while j < len(l)-1:
                    l[j] = rtn[i-1][j-1] + rtn[i-1][j]
                    j+=1
                rtn.append(l)
            return rtn