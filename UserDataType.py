from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_list_to_linkedlist(lst: List) -> Optional[ListNode]:
    linked_list = None

    for i in range(len(lst) - 1, -1, -1):
        new = ListNode(lst[i])
        new.next = linked_list
        linked_list = new

    return linked_list


def convert_linkedlist_to_list(node: Optional[ListNode]) -> List:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
