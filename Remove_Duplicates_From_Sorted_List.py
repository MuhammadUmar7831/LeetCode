#https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class Solution(object):
    def deleteDuplicates(self, head):
        itr = head
        prev = ListNode("v")#dummy prev node the value is initiall v so that it unable to match for the first time
        while itr != None:
            if itr.val == prev.val: # if prev val is equal to the current node val
                prev.next = itr.next # skip the current node from the list
            else: # set the current node previous node
                prev = itr
            itr = itr.next # proceed to next node
        return head