from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_list_to_linkedlist(lst: List) -> Optional[ListNode]:
    head = ListNode(lst[0])
    node = head
    for i in range(1, len(lst)):
        node.next = ListNode(lst[i])
        node = node.next
    return head

# def convert_list_to_linkedlist(lst: List) -> Optional[ListNode]:
#     node = None
#     for i in range(len(lst) - 1, -1, -1):
#         new = ListNode(lst[i])
#         new.next = node
#         node = new
#     return node


def convert_linkedlist_to_list(node: Optional[ListNode]) -> List:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def print_linkedlist(node: Optional[ListNode]):
    while node:
        print(node.val, end=' ')
        node = node.next
