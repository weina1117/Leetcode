"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        first, second, curr = 1, 2, 0

        for step in range(2, n):
            curr = first + second
            first, second = second, curr

        return curr

cases = [3,10,5,7,21]
sol = Solution()
print [sol.climbStairs(x) for x in cases]