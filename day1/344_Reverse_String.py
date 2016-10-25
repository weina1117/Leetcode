"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = []
        for i in range(len(s)):
            lst.append(s[-(i + 1)])
        lst = ''.join(lst)
        return lst

cases = ['hello','world']
sol = Solution()
print [sol.reverseString(i) for i in cases]