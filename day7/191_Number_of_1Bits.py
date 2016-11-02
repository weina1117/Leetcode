"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sol = Solution()
print [sol.hammingWeight(x) for x in cases]