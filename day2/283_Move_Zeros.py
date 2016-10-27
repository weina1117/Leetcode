"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0

        while 0 in nums:
            nums.remove(0)
            count+=1

        for i in range(count):
            nums.append(0)
        return nums


cases = [[0, 45, 0, 765], [5, 4, 4, 7, 0, 3, 12], [0, 876, 3]]

sol = Solution()
print [sol.moveZeroes(x) for x in cases]
