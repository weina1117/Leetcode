"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        return int((sqrt(1+8*n) - 1) / 2)

cases = [5,8,20,300,568,711,911,10000]
sol = Solution()
print [sol.arrangeCoins(x) for x in cases]