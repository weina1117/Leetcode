"""
Reverse a singly linked list.
Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
from utils.utils import createLinkedList


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        newhead = self.reverseList(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return newhead

cases = [[1,2,3,4,5]]
sol = Solution()
print [str(sol.reverseList(createLinkedList(p))) for p in cases]
