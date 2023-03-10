# https://leetcode.com/problems/product-of-array-except-self/
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]
        p = 1
        # 왼쪽 요소들의 곱셈 결과
        for i in range(0, len(nums) - 1):
            p = p * nums[i]
            out.append(p)

        p = 1
        # 왼쪽 요소들의 곱셈 결과에 오른쪽 요소들의 곱셈 결과를 차례대로 곱셈
        for i in range(len(nums) - 1, 0, -1):
            p = p * nums[i]
            out[i - 1] = out[i - 1] * p

        return out


nums = [1, 2, 3, 4]  # Output: [24,12,8,6]
# nums = [-1, 1, 0, -3, 3]  # Output: [0,0,9,0,0]

solution = Solution()
print(solution.productExceptSelf(nums))
