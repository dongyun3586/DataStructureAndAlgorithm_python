from typing import *
from LinkedList import *


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        prev.next = head

        while head and head.next:
            # 인접한 두 개 위치 바꾸기
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b   # 이전 노드가 바뀐 첫 번째 노드 가리키기

            # 다음 작업을 위한 세팅
            head = head.next
            prev = prev.next.next
        return root.next


head = [1, 2, 3, 4]  # Output: [2,1,4,3]
head = convert_list_to_linkedlist(head)

solution = Solution()
print_linkedlist(solution.swapPairs(head))
