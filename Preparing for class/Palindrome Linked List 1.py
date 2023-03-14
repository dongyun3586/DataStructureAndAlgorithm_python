from typing import *
from convert_list_to_linkedlist import *


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # convert linked list to list
        nums = convert_linkedlist_to_list(head)

        while len(nums) > 1:
            if nums.pop(0) != nums.pop():
                return False
        return True
        # return nums == nums[::-1]


head = [1, 2, 2, 1]  # Output: true
head = convert_list_to_linkedlist(head)
solution = Solution()
print(solution.isPalindrome(head))
