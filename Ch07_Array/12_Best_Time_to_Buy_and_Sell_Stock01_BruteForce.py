# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price


prices = [7, 1, 5, 3, 6, 4]  # Output: 5
# prices = [7, 6, 4, 3, 1]  # Output: 0

solution = Solution()
print(solution.maxProfit(prices))
