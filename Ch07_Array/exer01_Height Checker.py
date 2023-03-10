from typing import *


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)

        count = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                count += 1
        return count


heights = [5, 1, 2, 3, 4]  # Output: 5

solution = Solution()
print(solution.heightChecker(heights))
