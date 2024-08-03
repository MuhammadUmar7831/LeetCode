#https://leetcode.com/problems/sort-list

# brute force space: O(n) time: O(2n)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        ptr = head
        while ptr:
            nums.append(ptr.val)
            ptr = ptr.next
        nums.sort()
        ptr = head
        for num in nums:
            ptr.val = num
            ptr = ptr.next
        return head