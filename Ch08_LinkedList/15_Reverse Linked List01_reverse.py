'''
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

from typing import Optional
from UserDataType import ListNode, convert_list_to_linkedlist, convert_linkedlist_to_list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)



head = [1,2,3,4,5]      # Output: [5,4,3,2,1]
head = convert_list_to_linkedlist(head)


solution = Solution()
head = solution.reverseList(head)

result = convert_linkedlist_to_list(head)
print(result)