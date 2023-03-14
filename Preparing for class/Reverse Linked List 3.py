from typing import *
from convert_list_to_linkedlist import *


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode=None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)



head = [1, 2, 3, 4, 5]  # Output: [5,4,3,2,1]
head = convert_list_to_linkedlist1(head)

solution = Solution()
print_linkedlist(solution.reverseList(head))
