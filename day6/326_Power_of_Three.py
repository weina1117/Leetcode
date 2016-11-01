"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n / 3

        return True if n == 1 else False
cases = [1,2,3,4,5,6,7,8,9,112,224,356,68,97,17311,98702]
sol = Solution()
print [sol.isPowerOfThree(x) for x in cases]