# https://leetcode.com/problems/add-two-numbers/


from typing import Optional
from LinkedList import *


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 시작 노드 만들기
        head = node = ListNode()

        # 현재 자리의 합계 구하기
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            # 10으로 나눈 몫과 나머지 구하기
            carry, val = divmod(sum + carry, 10)
            node.next = ListNode(val)
            node = node.next
        return head.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]  # Output: [7,0,8]
l1 = convert_list_to_linkedlist(l1)
l2 = convert_list_to_linkedlist(l2)

solution = Solution()
head = solution.addTwoNumbers(l1, l2)

result = convert_linkedlist_to_list(head)
print(result)
