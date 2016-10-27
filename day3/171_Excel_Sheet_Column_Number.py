"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28


At first it was confusing but I later figure out what the question is asking
for example if the input is 'CDA', and the values are 3,4,1
the index of each char in the string in reverse order plus one is 2, 1, 0

the formula is

result = value(char) * 26^(order(char))

so in this case.

result = 3 * (26^2) + 4 * (26^1) + 1 * 26^0 = 2133

This makes sense to me and hope my explanation is helpful

"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            coef = ord(s[-1-i])-64
            value = 26**i
            res += (coef*value)
        return res

cases = ['AA', 'ZH', 'AH', 'ZA', 'A', 'Z']
sol = Solution()
print [sol.titleToNumber(i) for i in cases]