#https://leetcode.com/problems/jewels-and-stones/

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        dic = {}
        count = 0
        for jewel in jewels:
            dic[jewel] = 1
        for stone in stones:
            if dic.get(stone) != None:
                count += 1
        return count
        