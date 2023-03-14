'''
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

from typing import Optional
from LinkedList import *


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 역순 리스트로 변환
        l1 = self.to_list(self.revers_linkedlist(l1))
        l2 = self.to_list(self.revers_linkedlist(l2))

        # 리스트 -> 문자열 변환 -> 덧셈
        sum_str = int(''.join(map(str, l1))) + int(''.join(map(str, l2)))

        # 문자열 -> 역순 연결 리스트
        return self.str_to_reversed_linkedlist(str(sum_str))

    def revers_linkedlist(self, node):
        rev = None
        while node:
            node.next, rev, node = rev, node, node.next
        return rev

    def to_list(self, node):
        nums = []
        while node:
            nums.append(node.val)
            node = node.next
        return nums

    def str_to_reversed_linkedlist(self, sum_str: str)->Optional[ListNode]:
        next = None
        for i in sum_str:
            node = ListNode(i)
            node.next = next
            next = node
        return node


l1 = [2, 4, 3]
l2 = [5, 6, 4]  # Output: [7,0,8]
l1 = convert_list_to_linkedlist(l1)
l2 = convert_list_to_linkedlist(l2)

solution = Solution()
head = solution.addTwoNumbers(l1, l2)

result = convert_linkedlist_to_list(head)
print(result)
