"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

import collections
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return False if nums == [] else max(count for count in collections.Counter(nums).values()) >= 2


cases = [[1,2,3,4,5,5,5,5],[12,0,112,12,2]]
sol = Solution()
print [sol.containsDuplicate(x) for x in cases]