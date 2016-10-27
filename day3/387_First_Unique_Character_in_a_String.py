"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1

        for i, c in enumerate(s):
            if counter[c] == 1:
                return i

        return -1

cases = ['helloworld','Ilovepython']
sol = Solution()
print [sol.firstUniqChar(i) for i in cases]