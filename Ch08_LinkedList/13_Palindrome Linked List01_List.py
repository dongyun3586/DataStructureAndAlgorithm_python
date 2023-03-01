'''
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list,
return true if it is a palindrome or false otherwise.
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        q = []
        node = head
        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


head = [1, 2, 2, 1]  # Output: true
# head = [1,2]            # Output: false

# # list -> singly linked list : 첫 번재 요소부터 생성
prev = ListNode(head[0])
node = prev
for i in range(1, len(head)):
    node.next = ListNode(head[i])
    node = node.next

# # list -> singly linked list : 마지막 요소부터 생성
# prev = None
# for i in range(len(head) - 1, -1, -1):
#     new = ListNode(head[i])
#     new.next = prev
#     prev = new

solution = Solution()
print(solution.isPalindrome(prev))
