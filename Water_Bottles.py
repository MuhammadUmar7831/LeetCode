#https://leetcode.com/problems/water-bottles/

#space: O(1) time: O(log numExchange (numBottles))
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        empty = 0
        while numBottles:
            count += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange
        return count