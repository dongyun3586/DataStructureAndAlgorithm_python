from typing import *
from convert_list_to_linkedlist import *


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head
        while list1 or list2:
            # 비어있지 않고, 더 작은 노드가 list1
            if (not list1) or (list2 and list1.val > list2.val):
                list1, list2 = list2, list1

            node.next = list1
            node = node.next
            list1 = list1.next

        return head.next


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
