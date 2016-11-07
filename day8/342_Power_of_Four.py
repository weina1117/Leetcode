"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 0 and num & 3 == 0:
            num >>= 2
        return num == 1

cases = [[44,12,35,36,37,38],[26,27,28,29,30]]
sol = Solution()
print [sol.isPowerOfFour(x) for x in cases]