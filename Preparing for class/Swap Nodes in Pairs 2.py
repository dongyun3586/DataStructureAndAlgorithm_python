from typing import *
from convert_list_to_linkedlist import *


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head


head = [1, 2, 3, 4]  # Output: [2,1,4,3]
head = convert_list_to_linkedlist1(head)

solution = Solution()
print_linkedlist(solution.swapPairs(head))
