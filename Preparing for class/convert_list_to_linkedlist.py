from typing import *
from LinkedList import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_list_to_linkedlist1(nums: List[int]) -> ListNode:
    # 첫 번재 요소를 ListNode로 만들기
    head = ListNode(nums[0]) if nums else None
    # 나머지 요소를 연결하여 LinkedList 만들기
    node = head
    for i in range(1, len(nums)):
        node.next = ListNode(nums[i])
        node = node.next
    return head


def convert_list_to_linkedlist2(nums: List[int]) -> ListNode:
    # 첫 번재 요소를 ListNode로 만들기
    next = None
    # 나머지 요소를 연결하여 LinkedList 만들기
    for i in range(len(nums) - 1, -1, -1):
        node = ListNode(nums[i])
        node.next = next
        next = node
    return next


def print_linkedlist(head: Optional[ListNode]):
    while head:
        print(head.val, end=' ')
        head = head.next


def convert_linkedlist_to_list(node: Optional[ListNode]) -> List[int]:
    nums = []
    while node:
        nums.append(node.val)
        node = node.next
    return nums


# head = [1, 2, 2, 1]
# head = []
# print(head)
# head = convert_list_to_linkedlist1(head)
# print_linkedlist(head)
