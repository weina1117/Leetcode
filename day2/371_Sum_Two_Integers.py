"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
cases = [
        ([589, 2]),
        ([400000, 1100998]),
        ([0, -78]),
        ([3490087, 523438]),
        ([34, 0]),
        ([0, -1]),
        ([98765438777, -9765557])
]

sol= Solution()
print[sol.getSum(x[0], x[1]) for x in cases]