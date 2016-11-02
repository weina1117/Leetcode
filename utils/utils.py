"""
((((H,K)D,(F,I)G)B,E)A,((L,(N,Q)O)J,(P,S)M)C)
"""
from Queue import deque


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deserialize(data):
    def _deserialize_list(data):
        if not data:
            return None

        val = data.pop(0)
        if not val:
            return None

        node = TreeNode(int(val))
        node.left = _deserialize_list(data)
        node.right = _deserialize_list(data)
        return node

    if not data:
        return None

    return _deserialize_list(data.split(','))

tree = deserialize('1,2,3,4,5')
print tree
