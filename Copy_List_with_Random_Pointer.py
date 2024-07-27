#https://leetcode.com/problems/copy-list-with-random-pointer

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        myListHead = Node(0)
        myListCurr = myListHead
        curr = head
        inc = 0
        mapping = {}

        while curr.next:
            myListCurr.val = curr.val
            mapping[inc] = myListCurr
            myListCurr.next = Node(0)

            myListCurr = myListCurr.next
            curr.val = inc
            curr = curr.next

            inc += 1
        
        myListCurr.val = curr.val
        myListCurr.next = None
        curr.val = inc
        mapping[inc] = myListCurr

        myListCurr = myListHead
        curr = head
        while myListCurr:
            myListCurr.random = mapping[curr.random.val] if curr.random != None else None
            myListCurr = myListCurr.next
            curr = curr.next
    
        return myListHead