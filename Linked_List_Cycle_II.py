#https://leetcode.com/problems/linked-list-cycle-ii/

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        while head:
            if dic.get(head):
                return head
            else:
                dic[head] = 1
            head = head.next
        return None      