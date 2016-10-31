"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return True if Counter(s) == Counter(t) else False

cases = [('abc','cba',),
         ('aaabbbcccddd', 'abcdef',),
         ('helloworld', 'helo',)
         ]
sol = Solution()
print[sol.isAnagram(str[0], str[1]) for str in cases]