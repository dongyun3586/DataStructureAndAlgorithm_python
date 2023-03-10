from typing import *


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums2 = [i for i in range(1, len(nums) + 1)]

        result = []
        idx = 0
        for i in range(len(nums2)):
            while 0 < idx < len(nums2) and nums[idx] == nums[idx - 1]:
                idx += 1
            if idx >= len(nums2) or nums2[i] != nums[idx]:
                result.append(nums2[i])
            else:
                idx += 1

        return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]  # Output: [5,6]
# nums = [1, 1]  # Output: [2]

solution = Solution()
print(solution.findDisappearedNumbers(nums))
