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
            next = curr.next
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
        