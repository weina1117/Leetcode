"""
Given an array of size n, find the majority element. The majority element is the element that appears more than [n/2] times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""

from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elem_count = Counter(nums)
        for element in nums:
            if elem_count[element] > len(nums)/2:
                return element
        return -1
cases = [[1,2,3,4,5,5,5,5],[12,0,112,12,2],
         [1,2,3,4,5,6,7],[3,2,2,2,2,1]]
sol = Solution()
print [sol.majorityElement(x) for x in cases]
