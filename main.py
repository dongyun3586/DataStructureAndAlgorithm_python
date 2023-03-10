from typing import *
from LinkedList import *
from collections import deque


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = deque()
        node = head
        while node:
            result.append(node.val)
            node = node.next

        while len(result) > 1:
            if result.popleft() != result.pop():
                return False

        # return result == result[::-1]
        return True


head = [1, 2, 2, 1]  # Output: true
head = convert_list_to_linkedlist(head)

# 출력 해보기
node = head
while node is not None:
    print(node.val, end=' ')
    node = node.next

solution = Solution()
print(solution.isPalindrome(head))
