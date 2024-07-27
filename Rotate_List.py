# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        size = 0
        ptr = head
        while ptr.next:
            size += 1
            ptr = ptr.next
        tail = ptr
        size += 1
        k = k % size
        
        ptr = head
        curr = 1

        while (size - k) != curr:
            curr += 1
            ptr = ptr.next
        
        tail.next = head
        head = ptr.next
        ptr.next = None

        return head