from typing import *
from LinkedList import *


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            if not list2:
                return None
            else:
                return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        node = head
        while list1 and list2:
            if list1.val <= list2.val:
                node.next, node = list1, list1
                list1 = list1.next
            else:
                node.next, node = list2, list2
                list2 = list2.next

        while list1:
            node.next, node = list1, list1
            list1 = list1.next

        while list2:
            node.next, node = list2, list2
            list2 = list2.next

        return head


list1 = [1, 2, 4]
list2 = [1, 3, 4]  # Output: [1,1,2,3,4,4]
list1 = []
list2 = [0]
list1 = convert_list_to_linkedlist(list1)
list2 = convert_list_to_linkedlist(list2)

solution = Solution()
result = solution.mergeTwoLists(list1, list2)
print_linkedlist(result)
