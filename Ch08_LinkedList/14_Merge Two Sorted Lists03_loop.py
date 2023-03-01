'''
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list,
return true if it is a palindrome or false otherwise.
'''

from typing import Optional
from UserDataType import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = list1, list2
        head = None

        # head 노드 결정
        if n1 and n2:
            if n1.val <= n2.val:
                head = n1
                n1 = n1.next
            else:
                head = n2
                n2 = n2.next
        elif n1:
            head = n1
            n1 = n1.next
        elif n2:
            head = n2
            n2 = n2.next

        node = head
        while n1 and n2:
            if n1.val <= n2.val:
                node.next = n1
                n1 = n1.next
                node = node.next
            else:
                node.next = n2
                n2 = n2.next
                node = node.next

        while n1:
            node.next = n1
            n1 = n1.next
            node = node.next

        while n2:
            node.next = n2
            n2 = n2.next
            node = node.next

        return head



list1 = [1,2,4]
list2 = [1,3,4]     # Output: [1,1,2,3,4,4]
# list1 = []
# list2 = []
# list1 = []
# list2 = [0]

# # list -> singly linked list : 첫 번재 요소부터 생성
llist1 = ListNode(list1[0]) if list1 else None
node = llist1
for i in range(1, len(list1)):
    node.next = ListNode(list1[i])
    node = node.next

llist2 = None
for i in range(len(list2) - 1, -1, -1):
    new = ListNode(list2[i])
    new.next = llist2
    llist2 = new


solution = Solution()
head = solution.mergeTwoLists(llist1, llist2)
result = []
node = head
while node:
    result.append(node.val)
    node = node.next

print(result)