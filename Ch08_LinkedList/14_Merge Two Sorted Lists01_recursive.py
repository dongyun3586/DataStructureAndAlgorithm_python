'''
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list,
return true if it is a palindrome or false otherwise.
'''
from typing import Optional
from LinkedList import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1


list1 = [1, 2, 4]
list2 = [1, 3, 4]  # Output: [1,1,2,3,4,4]
# list1 = []
# list2 = []
# list1 = []
# list2 = [0]

# region 리스트 -> 링크드리스트 변환
# 첫 번재 요소부터 생성
llist1 = ListNode(list1[0]) if list1 else None
node = llist1
for i in range(1, len(list1)):
    node.next = ListNode(list1[i])
    node = node.next

# 마지막 요소부터 생성
llist2 = None
for i in range(len(list2) - 1, -1, -1):
    new = ListNode(list2[i])
    new.next = llist2
    llist2 = new
# endregion

solution = Solution()
head = solution.mergeTwoLists(llist1, llist2)

# region 링크드리스트 -> 리스트 변환
result = []
node = head
while node:
    result.append(node.val)
    node = node.next

print(result)
# endregion
