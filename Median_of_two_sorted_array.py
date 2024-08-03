
#Brute force space O(n+m) time: O(n+m)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=(nums1 + nums2)
        nums3.sort()
        return nums3[len(nums3)//2] if len(nums3) % 2 else (nums3[len(nums3)//2] + nums3[(len(nums3)-1)//2])/2
    
#space O((n+m)/2) time: O((n+m)/2)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        total = n + m
        mid = total // 2
        nums3 = []
        p1 = 0
        p2 = 0
        while p1 < n or p2 < m:
            if len(nums3) == mid+1:
                break
            if p1 < n and p2 < m and nums1[p1] < nums2[p2]:
                nums3.append(nums1[p1])
                p1 += 1
            elif p1 < n and p2 < m and nums1[p1] >= nums2[p2]:
                nums3.append(nums2[p2])
                p2 += 1
            elif p1 < n:
                nums3.append(nums1[p1])
                p1 += 1
            else:
                nums3.append(nums2[p2])
                p2 += 1
        return nums3[-1] if total % 2 else (nums3[-1] + nums3[-2]) / 2

#More better sapce: O(1) time: O((n+m)/2)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        total = n + m
        mid = total // 2
        last = None
        secondLast = None
        p1 = 0
        p2 = 0
        while p1 < n or p2 < m:
            if p1 + p2 == mid+1:
                break
            if p1 < n and p2 < m and nums1[p1] < nums2[p2]:
                secondLast = last 
                last = nums1[p1]
                p1 += 1
            elif p1 < n and p2 < m and nums1[p1] >= nums2[p2]:
                secondLast = last 
                last = nums2[p2]
                p2 += 1
            elif p1 < n:
                secondLast = last 
                last = nums1[p1]
                p1 += 1
            else:
                secondLast = last 
                last = nums2[p2]
                p2 += 1
        return last if total % 2 else (last + secondLast) / 2

# merged the if elif
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        total = n + m
        mid = total // 2
        last = None
        secondLast = None
        p1 = 0
        p2 = 0
        while p1 < n or p2 < m:
            if p1 + p2 == mid+1:
                break
            if (p1 < n and p2 < m and nums1[p1] < nums2[p2]) or (p1 < n and p2 == m):
                secondLast = last 
                last = nums1[p1]
                p1 += 1
            else:
                secondLast = last 
                last = nums2[p2]
                p2 += 1
        return last if total % 2 else (last + secondLast) / 2
