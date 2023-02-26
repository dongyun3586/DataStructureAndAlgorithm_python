# https://leetcode.com/problems/two-sum/

from typing import List

# 정렬된 리스트가 제공되는 경우 가능한 방법
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while not left == right:
            # left + right가 target 보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]


nums = [2,7,11,15]
target = 9
# nums = [3,2,4]
# target = 6

solution = Solution()
print(solution.twoSum(nums, target))