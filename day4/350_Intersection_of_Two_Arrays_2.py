"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

# 2 = 10
# 3 = 11
# 2 & 3 = 10 & 11 = 10

# & 1 0    | 1 0
# 0 0 0    1 1 1
# 1 1 0    0 1 0
#

import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        return list((counter1 & counter2).elements())

cases = [([1, 2, 3, 4], [3,4]),
         ([5, 6, 7, 8, 9, 10], [7, 9])]

sol = Solution()
print [sol.intersect(x[0], x[1]) for x in cases]
