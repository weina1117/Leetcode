"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(1, rowIndex+1):
            row = [x+y for x,y in zip([0]+row, row+[0])]
        return row
cases = [1,2,3,4]
sol = Solution()
print [sol.getRow(x) for x in cases]