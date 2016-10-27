from utils.utils import TreeNode, list_to_tree
"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def t(n):
            return n and (n.val, t(n.left), t(n.right))
        return t(p) == t(q)

cases = [list_to_tree('((((H,K)D,(F,I)G)B,E)A,((L,(N,Q)O)J,(P,S)M)C)')]
sol = Solution()
print [sol.isSameTree(x[0], x[1]) for x in cases]
