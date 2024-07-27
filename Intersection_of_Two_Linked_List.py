#https://leetcode.com/problems/intersection-of-two-linked-lists

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA = 0
        sizeB = 0
        ptrA = headA 
        ptrB = headB
        while ptrA.next:
            sizeA += 1
            ptrA = ptrA.next
        while ptrB.next:
            sizeB += 1
            ptrB = ptrB.next
        if ptrA != ptrB:
            return None
        sizeA += 1
        sizeB += 1
        ptrA = headA
        ptrB = headB
        if sizeA > sizeB:
            skip = sizeA - sizeB
            while skip:
                ptrA = ptrA.next
                skip -= 1
        elif sizeA < sizeB:
            skip = sizeB - sizeA
            while skip:
                ptrB = ptrB.next
                skip -= 1
        while ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next
        return ptrA