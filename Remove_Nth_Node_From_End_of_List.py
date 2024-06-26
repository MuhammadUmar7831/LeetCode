#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

#brute force

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        #each element is put in stack in LIFO than then pop up each element set the top Node next to the poped node for each node except the node to be deleted
        stack = [] # stack appraoch
        node = head
        while node:
            stack.append(node)
            node = node.next
        
        index = 1
        node = None
        while stack:
            if index != n:
                stack[-1].next = node
                node = stack.pop()
            else:
                stack.pop()
            index = index + 1
        return node
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
#optimized rather than traversing again the stack just use the list properties
  
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        if (len(stack) == n):
            return head.next
        prev = -n - 1
        nex_t = -n + 1
        if nex_t == 0:
            stack[prev].next = None
        else:
            stack[prev].next = stack[nex_t]
        return head
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        