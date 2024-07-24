#https://leetcode.com/problems/search-a-2d-matrix/submissions/1331712700/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][len(matrix[i])-1]: # find the row whcih may potentially have the target
                for j in range(len(matrix[i])):
                    if target == matrix[i][j]:
                        return True
        return False
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][len(matrix[i])-1]: 
                s = 0 # binary search
                e = len(matrix[i]) - 1
                while s <= e:
                    m = (s + e) // 2
                    if matrix[i][m] == target:
                        return True
                    elif matrix[i][m] < target:
                        s = m + 1
                    else:
                        e = m - 1
                return False
        return False