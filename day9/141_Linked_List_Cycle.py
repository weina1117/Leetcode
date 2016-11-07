"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?


"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils.utils import ListNode
from utils.utils import get_list_head

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slowPointer = fastPointer = head

        while fastPointer and fastPointer.next:

            slowPointer, fastPointer = slowPointer.next, fastPointer.next.next

            if slowPointer == fastPointer:
                return True

        return False

"""
1->2->3
   ^__|
"""
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head.next
sol = Solution()
cases = [head]
print [sol.hasCycle(x) for x in cases]
