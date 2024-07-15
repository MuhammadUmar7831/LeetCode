#https://leetcode.com/problems/compare-version-numbers/

class Solution(object):
    def compareVersion(self, version1, version2):
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        _max_len = max(len(version1), len(version2)) # get the max version length 
        
        for i in range(_max_len): # iterate the both version unptil max length
            v1 = 0 if i > len(version1) - 1 else int(version1[i]) # v1 subversion is 0 if index out of range else parse version into int
            v2 = 0 if i > len(version2) - 1 else int(version2[i]) # v2 subversion is 0 if index out of range else parse version into int

            if v1 > v2: # if v1 is greater return 1
                return 1
            elif v1 < v2: # if v2 is greater return -1
                return -1
        return 0 # # if v1 and v2 has same version