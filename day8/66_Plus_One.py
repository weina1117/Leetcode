"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
    	    num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]

cases = [[9,3,0,1],[2,7,3,9]]
sol = Solution()
print [sol.plusOne(x) for x in cases]