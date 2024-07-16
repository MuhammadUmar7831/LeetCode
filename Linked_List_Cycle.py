#https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        p1 = head
        p2 = head.next.next if head.next else head.next
        while p2 != None and p1 != None:
            if p1 == p2:
                return True
            p1 = p1.next
            if p2.next:
                p2 = p2.next.next
            else:
                return False
        return False
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next 

        return False
        