#https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        transponse = [[0]*len(matrix) for _ in range(len(matrix))] #initialize empty matrix for transpose
        j = 0
        for row in matrix: # take transpose of matrix
            i = 0
            while i < len(matrix):
                transponse[i][j] = row[i]
                i += 1
            j += 1
        j = 0
        for i in range(len(matrix)): # for each row store the reverse of each row of transpose
            matrix[i] = transponse[i][::-1]
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        