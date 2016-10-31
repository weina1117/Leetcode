"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
import collections

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Need to import "collections" library.
        # Sum all even occurrences.
        evenSum = sum(count for count in collections.Counter(s).values() if count % 2 == 0)
        # Convert all odd occurences to even and sum.
        # We need to add 1 at last because we can put a single letter at the middle.
        convertOddSumToEvenSum = sum(count-1 for count in collections.Counter(s).values() if count % 2 == 1)
        # Check whether the string only contains letters that have even occurances
        oddSum = sum(count for count in collections.Counter(s).values() if count % 2 == 1)
        return evenSum + convertOddSumToEvenSum + 1 if oddSum != 0 else evenSum

cases = ['aaabbbcccddd', 'bccccdd']
sol = Solution()
print [sol.longestPalindrome(x) for x in cases]
