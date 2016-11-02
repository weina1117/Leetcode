"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1

cases = [14, 21, 60,50,11,4,5,6,7,8,9,11,12,13]
sol = Solution()
print [sol.isUgly(x) for x in cases]

