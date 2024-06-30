#https://leetcode.com/problems/merge-sorted-array/


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2 #skip the first m elements and replace the rest with nums2 array
        nums1.sort() # sort the merged array
        