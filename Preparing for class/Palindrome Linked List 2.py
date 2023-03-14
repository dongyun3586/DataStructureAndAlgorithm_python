from typing import *
from convert_list_to_linkedlist import *


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        rev = next = None

        while fast and fast.next:
            fast = fast.next.next
            next = slow.next
            slow.next = rev
            rev = slow
            slow = next
            # slow.next, rev, slow = rev, slow, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next

        return not rev


head = [1, 2, 2, 1]  # Output: true
# head = [1, 2]
head = convert_list_to_linkedlist(head)
solution = Solution()
print(solution.isPalindrome(head))
