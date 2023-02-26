# https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            # left_max와 right_max 중 더 낮은 쪽인 높은 쪽으로 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume



height = [0,1,0,2,1,0,1,3,2,1,2,1]

solution = Solution()
print(solution.trap(height))