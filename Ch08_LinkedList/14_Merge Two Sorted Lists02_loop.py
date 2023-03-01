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

# list -> singly linked list : 마지막 요소부터 생성
llist1 = None
for i in range(len(list1) - 1, -1, -1):
    new = ListNode(list1[i])
    new.next = llist1
    llist1 = new

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
