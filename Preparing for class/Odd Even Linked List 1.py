from typing import *
from convert_list_to_linkedlist import *


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = odd.next

        odd.next = even_head
        return head


head = [1, 2, 3, 4, 5]  # Output: [1,3,5,2,4]
head = [2, 1, 3, 5, 6, 4, 7]  # Output: [2,3,6,7,1,5,4]

head = convert_list_to_linkedlist1(head)

solution = Solution()
print_linkedlist(solution.oddEvenList(head))
