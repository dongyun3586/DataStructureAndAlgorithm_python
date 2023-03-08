# https://leetcode.com/problems/product-of-array-except-self/
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''
from typing import List
from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        p = 1
        # 왼쪽 요소들의 곱셈 결과
        for i in range(0, len(nums) - 1):  # [0, 1, 2]
            p = p * nums[i]
            left.append(p)
            # left = [1, 1, 2, 6]

        # 오른쪽 요소들의 곱셈 결과
        right: deque[int] = deque([1])
        p = 1
        for i in range(len(nums) - 1, 0, -1):
            p = p * nums[i]
            right.appendleft(p)
            # right = [24, 12, 4, 1]

        # 왼쪽 곱셈 결과와 오른쪽 곱셈 결과를 곱함.
        result = [left[i] * right[i] for i in range(len(nums))]
        # for i in range(len(nums)):
        #     result.append(left[i] * right[i])

        return result


nums = [1, 2, 3, 4]  # Output: [24,12,8,6]
# nums = [-1, 1, 0, -3, 3]  # Output: [0,0,9,0,0]

solution = Solution()
print(solution.productExceptSelf(nums))