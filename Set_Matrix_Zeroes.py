#https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        copy = [row[:] for row in matrix]

        def setColZero(col: int)->None:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
        for i in range(len(matrix)):
            zero_row = [0]*len(matrix[i])
            for j in range(len(matrix[i])):
                if copy[i][j] == 0:
                    matrix[i] = zero_row
                    setColZero(j)
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows0 = [False]*len(matrix)
        cols0 = [False]*len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows0[i] = True
                    cols0[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if rows0[i] or cols0[j] :
                    matrix[i][j] = 0
                    
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols0 = [False]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    cols0[j] = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                matrix[i]=[0]*len(matrix[i])
            else:
                for j in range(len(matrix[i])):
                    if cols0[j]:
                        matrix[i][j] = 0
        
        