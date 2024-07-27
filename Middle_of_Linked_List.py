#https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        single = head
        double = head
        while double and double.next:
            single = single.next
            double = double.next
            if double:
                double = double.next
            else:
                return single
        return single
        
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        single = double = head
        while double and double.next:
            single = single.next
            double = double.next.next
        return single
        