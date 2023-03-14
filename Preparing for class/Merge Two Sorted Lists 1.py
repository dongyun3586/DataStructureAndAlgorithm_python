from typing import *
from convert_list_to_linkedlist import *


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # empty linked list 처리
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        # head 노드 설정
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        # 둘 중 하나가 빌때까지 추가
        node = head
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        # 남은 노드 추가
        if list1:
            node.next = list1
        if list2:
            node.next = list2

        return head


list1 = [1, 2, 4]
list2 = [1, 3, 4]  # Output: [1,1,2,3,4,4]
# list1 = []
# list2 = []
# list1 = []
# list2 = [0]

list1 = convert_list_to_linkedlist1(list1)
list2 = convert_list_to_linkedlist1(list2)

solution = Solution()
print_linkedlist(solution.mergeTwoLists(list1, list2))
