'''
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

from typing import Optional
from LinkedList import ListNode, convert_list_to_linkedlist, convert_linkedlist_to_list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.toReverseLinkedList(str(resultStr))

    def toList(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def reverseList(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next


        return prev

    def toReverseLinkedList(self, result):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node



l1 = [2,4,3]
l2 = [5,6,4]        # Output: [7,0,8]
l1 = convert_list_to_linkedlist(l1)
l2 = convert_list_to_linkedlist(l2)

solution = Solution()
head = solution.addTwoNumbers(l1, l2)

result = convert_linkedlist_to_list(head)
print(result)