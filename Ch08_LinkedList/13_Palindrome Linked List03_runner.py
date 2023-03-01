'''
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list,
return true if it is a palindrome or false otherwise.
'''

from typing import Optional
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        # 런너 기법을 이용해 역순 연결리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 판단
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


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
