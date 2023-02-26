# https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점(이전 높이보다 높은 지점)을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                # 왼쪽 벽이 없는 경우 나가기
                if not stack:
                    break

                # 이전과의 차이만큼 물 높이 추가
                distance = i - stack[-1] - 1
                # 왼쪽 벽과 오른쪽 벽 중 낮은 벽의 높이 - 벽 사이의 높이
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters

            stack.append(i)
        return volume


height = [0,1,0,2,1,0,1,3,2,1,2,1]

solution = Solution()
print(solution.trap(height))