# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:
            next = curr.next #temp variable
            curr.next = prev 
            prev = curr
            curr = next 
        return prev 

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None 

        newHead = head

        if head.next:
            newHead = self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None

        return newHead
    

    def reverseListStack(self, head):
        stack = []

        while head != None:
            stack.append(head)
            head = head.next 

        dummy = ListNode()
        newHead = dummy

        while stack:
            current = stack.pop()
            newHead.next = ListNode(current.val)
            newHead = newHead.next

        return dummy.next


solution = Solution()


node1 = ListNode(1)
node2 = ListNode(2)

node1.next = node2 


print (solution.reverseListStack(node1))