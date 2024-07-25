#https://leetcode.com/problems/unique-paths/

# Brute Force (visit every path and add valid paths while discard invalid paths) #TL
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(row, col):
            if row == m  or col == n:
                return 0
            elif row == m-1 and col == n-1:
                return 1
            return helper(row + 1, col) + helper(row, col + 1)

        return helper(0,0)
        
 
# not revist the nodes       
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def helper(row, col):
            if row == m  or col == n:
                return 0
            elif row == m-1 and col == n-1:
                return 1
            key = f"{row},{col}"
            if not dp.get(key, False):
                dp[key] = helper(row + 1, col) + helper(row, col + 1)
            return dp[key]

        return helper(0,0)
        

#Optimal no of unique paths is actually combinations of Rows - 1 (Bottom Steps) and Cols - 1 Right Step
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        Bottom = m - 1
        Right = n - 1
        return math.comb(Right + Bottom, Right)
        