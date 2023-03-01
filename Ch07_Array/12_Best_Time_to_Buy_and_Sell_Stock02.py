# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(price, min_price)
            profit = max(price - min_price, profit)

        return profit


prices = [7, 1, 5, 3, 6, 4]     # Output: 5
prices = [7, 6, 4, 3, 1]        # Output: 0

solution = Solution()
print(solution.maxProfit(prices))
