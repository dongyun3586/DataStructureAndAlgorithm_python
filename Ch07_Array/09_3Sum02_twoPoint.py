# https://leetcode.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 오름차순 정렬
        results = []

        for i in range(len(nums) - 2):
            # 중복되는 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # left, right를 설정하고 간격을 좁히면서 sum = 0 인 경우 찾기
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum == 0인 경우 정답으로 추가
                    results.append([nums[i], nums[left], nums[right]])

                    # left와 right 위치에 동일한 값이 있는 경우 다른 값이 나올 때까지 지나가기
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # while left < right and nums[right] == nums[right - 1]:
                    #     right -= 1
                    # right -= 1

        return results


# Result : Time Limit Exceeded
nums = [-1, 0, 1, 2, -1, -4]
nums = [-2,0,0,2,2]

solution = Solution()
print(solution.threeSum(nums))
