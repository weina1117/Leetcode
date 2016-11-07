"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

"""
class Solution(object):
    def __init__(self):
        self.cur_max = 0
        self.cur_sol = []
        self.pos = {}

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        last, now = 0, 0

        for i in nums: last, now = now, max(last + i, now)

        return now

    def rob1(self, nums):
        """
        is
        maximize sum(nums[i] i \in [0, len(num)-1])
        subject to: i-j >= 2 i \in is, j \in is
        [1, 2, 3, 4, 5]
        :param nums:
        :return:
        """
        if not self.pos:
            for i, val in enumerate(nums):
                self.pos[val] = i
            print self.pos
        if not nums:
            return
        valid = True
        n = len(nums)
        for i in range(n-1):
            if self.pos[nums[i+1]] - self.pos[nums[i]] == 1:
                valid = False
                break
        if valid:
            if self.cur_max < sum(nums):
                self.cur_sol = nums
                self.cur_max = sum(nums)
            return sum(nums)
        else:
            return max([self.rob1(nums[0:i]+nums[i+1:n]) for i in range(0, n)])

cases = [[10, 1120,30,1140,5000000000],[1000000000000000005,25,113,112230000,11]]
sol = Solution()
print [sol.rob(x) for x in cases]
print [sol.rob1(cases[1])]
print sol.cur_sol
