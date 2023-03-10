# https://leetcode.com/problems/array-partition/
'''
Given an integer array nums of 2n integers,
group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized.
Return the maximized sum.
'''
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum


# Result : Time Limit Exceeded
nums = [1, 4, 3, 2]  # 4
nums = [6, 2, 6, 5, 1, 2]  # 9

solution = Solution()
print(solution.arrayPairSum(nums))
