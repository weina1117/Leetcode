"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<=1:
            return 0
        max_profit=0
        low_price=prices[0]
        for i in range(1,n):
            low_price=min(low_price,prices[i])
            max_profit=max(max_profit, prices[i]-low_price)
        return max_profit

cases = [[8,7,6,5,5,4,3,2],[10,20,50,40,60,5,100],[100,102,90,80,50,51,49,10]]
sol =  Solution()
print [sol.maxProfit(x) for x in cases]