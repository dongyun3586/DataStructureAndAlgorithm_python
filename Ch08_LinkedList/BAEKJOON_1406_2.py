# https://www.acmicpc.net/problem/1406

class ListNode:
    def __init__(self, val=0, next=None, prev=None, head=False, tail=False):
        self.val = val
        self.next = next
        self.prev = prev
        self.head = head
        self.tail = tail


head = ListNode(head=True)
tail = cursor = ListNode(tail=True)
head.next = tail
tail.prev = head

input_str = input()
# 입력된 문자열을 연결 리스트로 만들기
for i in input_str:
    new_node = ListNode(i)
    prev_node = cursor.prev
    new_node.prev = prev_node
    new_node.next = cursor
    prev_node.next = new_node
    cursor.prev = new_node

command_count = int(input())

for _ in range(command_count):
    command = input().split()
    if command[0] == 'P':
        new_node = ListNode(command[1])
        prev_node = cursor.prev
        new_node.prev = prev_node
        new_node.next = cursor
        prev_node.next = new_node
        cursor.prev = new_node
    elif command[0] == 'L' and cursor is not head.next:
        cursor = cursor.prev
    elif command[0] == 'B' and cursor is not head.next:
        prev_node = cursor.prev.prev
        prev_node.next = cursor
        cursor.prev = prev_node
    elif command[0] == 'D' and cursor is not tail:
        cursor = cursor.next

node = head.next
while node is not tail:
    print(node.val, end='')
    node = node.next
