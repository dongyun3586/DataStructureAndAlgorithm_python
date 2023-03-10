# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i


nums = [2, 7, 11, 15]
target = 9
# nums = [3, 2, 4]
# target = 6
# nums = [3, 2, 2]
# target = 4

solution = Solution()
print(solution.twoSum(nums, target))
