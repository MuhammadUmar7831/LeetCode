#https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        sortedList = []
        for st in strs:
            t = list(st)
            t.sort()
            sortedList.append("".join(t))
        
        hashMap = {}
        for i in range(len(sortedList)):
            ele = sortedList[i]
            if hashMap.get(ele) == None:
                hashMap[ele] = [i]
            else:
                hashMap[ele].append(i)

        result = hashMap.values()
        for row in result:
            for i in range(len(row)):
                row[i] = strs[row[i]]

        return result
        
        
class Solution(object):
    def groupAnagrams(self, strs):
        sortedList = []
        hashMap = {}
        i = 0
        for st in strs:
            sortedSt = "".join(sorted(st))
            if hashMap.get(sortedSt) == None:
                hashMap[sortedSt] = [strs[i]]
            else:
                hashMap[sortedSt].append(strs[i])
            i += 1
        return hashMap.values()