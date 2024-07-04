#https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        f = head
        s = head.next
        while s != None:
            g = ListNode(hcfnaive(f.val, s.val), s)
            f.next = g
            f = s
            s = s.next
        return head
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        