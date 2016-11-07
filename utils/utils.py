"""
((((H,K)D,(F,I)G)B,E)A,((L,(N,Q)O)J,(P,S)M)C)
"""
from Queue import deque


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def get_list_head(nums):
    if not nums:
        return None
    i = 0
    head = ListNode(nums[i])
    p = head
    i += 1
    while i < len(nums):
        p.next = ListNode(nums[i])
        i += 1
    return head


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def parse_list_to_tree(nums):
    if not nums:
        return []
    q = deque()
    q.append(nums[0])
    i = 1
    root = TreeNode(q[0])
    r = root
    while len(q) > 0:
        if i < len(nums) and nums[i]:
            q.append(nums[i])
            r.left = TreeNode(nums[i])
        if i+1 < len(nums) and nums[i+1]:
            q.append(nums[i+1])
            r.right = TreeNode(nums[i+1])
        q.popleft()
        r = TreeNode(q.popleft())
        i += 2
    return root
