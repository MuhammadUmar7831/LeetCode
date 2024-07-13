#https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/


class Solution(object):
    def findMatrix(self, nums):
        dic, res = {}, []
        for num in nums:
            dic[num] = dic[num] + 1 if dic.get(num) != None else 1 #store frequency of each number
        
        while max(dic.values()) > 0: #iteratinf till the max frequency is greater than 0
            _res = [] #list for single row
            for i in dic.keys(): #iterate for all keys
                if dic[i] > 0: #append those keys that are available
                    _res.append(i)
                    dic[i] -= 1 # reduce frequency
            res.append(_res) #append row to result
        return res