from typing import *
from convert_list_to_linkedlist import *


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nums = self.convert_linkedlist_to_list(head)
        left, right = left - 1, right - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        head = self.convert_list_to_linkedlist1(nums)

        return head

    def convert_list_to_linkedlist1(self, nums: List[int]) -> ListNode:
        # 첫 번재 요소를 ListNode로 만들기
        head = ListNode(nums[0]) if nums else None
        # 나머지 요소를 연결하여 LinkedList 만들기
        node = head
        for i in range(1, len(nums)):
            node.next = ListNode(nums[i])
            node = node.next
        return head

    def convert_linkedlist_to_list(self, node: Optional[ListNode]) -> List[int]:
        nums = []
        while node:
            nums.append(node.val)
            node = node.next
        return nums


head = [1, 2, 3, 4, 5]
left = 2
right = 4  # Output: [1,4,3,2,5]

# head = [5]
# left = 1
# right = 1  # Output: [5]
head = convert_list_to_linkedlist1(head)

solution = Solution()
print_linkedlist(solution.reverseBetween(head, left, right))
