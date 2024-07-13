#https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

class Solution(object):
    def mergeNodes(self, head):
        mdfList = ListNode()
        mdfHead = mdfList
        mergedSum = 0
        head = head.next
        while head != None:
            mergedSum += head.val
            if head.val == 0:
                mdfList.val = mergedSum
                if head.next != None:
                    mdfList.next = ListNode()
                mdfList = mdfList.next
                mergedSum = 0
            head = head.next
        return mdfHead
        
        
class Solution(object):
    def mergeNodes(self, head):
        p1 = head
        p2 = head.next
        _sum = 0
        while p2:
            if p2.val == 0:
                p1 =  p1.next
                p1.val = _sum
                _sum = 0
            _sum += p2.val
            p2 = p2.next
        p1.next = None
        return head.next
         
        