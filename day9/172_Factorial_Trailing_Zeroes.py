"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        while n > 0:
            n /= 5
            r += n
        return r
cases = [10,12,13,15,19,20,4000,590,1000,650]
sol = Solution()
print [sol.trailingZeroes(x) for x in cases]