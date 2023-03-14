from typing import *
from convert_list_to_linkedlist import *


class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if m == n:
            return head

        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(m-1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n-m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next


head = [1, 2, 3, 4, 5]
left = 2
right = 4  # Output: [1,4,3,2,5]

# head = [5]
# left = 1
# right = 1  # Output: [5]
head = convert_list_to_linkedlist1(head)

solution = Solution()
print_linkedlist(solution.reverseBetween(head, left, right))
