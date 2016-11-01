"""
Given an integer, write a function to determine if it is a power of two.
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return any(n == 2 ** i for i in range(32))
cases = [1,2,3,4,5,6,7,8,9,112,224,356,68,97,17311,98702]
sol = Solution()
print [sol.isPowerOfTwo(x) for x in cases]