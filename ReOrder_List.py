#https://leetcode.com/problems/reorder-list/

# brute force space: O(n) time: O(n)
class Solution(object):
    def reorderList(self, head):
        stack = []
        ptr = head
        while ptr:
            stack.append(ptr)
            ptr = ptr.next
        ptr = head
        while ptr and ptr.next:
            temp = ptr.next
            if temp == stack[-1]:
                break
            ptr.next = stack.pop()
            ptr.next.next = temp
            ptr = temp
            stack[-1].next = None
        
# Better space: O(1) time(O(2n))  
def reverse(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev
class Solution(object):
    def reorderList(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalf = reverse(slow.next)
        slow.next = None
        
        slow = head
        fast = secondHalf
        
        while fast:
            temp1 = slow.next
            temp2 = fast.next
            
            slow.next = fast
            fast.next = temp1
            
            slow = temp1
            fast = temp2