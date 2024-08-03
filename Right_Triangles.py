#https://leetcode.com/problems/right-triangles/

#space: O(n*m) time:O(2(n*m))
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        rows = [0]*n
        cols = [0]*m
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    count += (rows[i]-1)*(cols[j]-1)
        
        return count