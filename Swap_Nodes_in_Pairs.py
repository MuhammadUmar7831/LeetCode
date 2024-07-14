#https://leetcode.com/problems/swap-nodes-in-pairs/description/

class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None: #edege cases (len=1,2)
            return head
        
        s, f = head, head.next # s(slow), f(fast) pointer with a delay of 1 node
        head = head.next #becuase in case of swap second node will be head
        prev = None #this pointer keep track of the tail of the last swapped pair to point it new head of newly swapped pair
        while s and f: #while any one of the fast or slow is not None
            s.next = f.next # next of fast is now next of slow (s->x, f->x)
            f.next = s # next of fast is now slow (f->s->x)
            if prev: #if prev is not None than set the prev (tail of last swap) to fast (head of new swap)
                prev.next = f
            prev = s # now set the prev to the tail of new swap
            s = s.next if s.next else None # proceed with next
            f = s.next if s and s.next else None # proceed with next
        return head