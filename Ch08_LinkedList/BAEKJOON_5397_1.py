# https://www.acmicpc.net/problem/5397

class ListNode:
    def __init__(self, val=0, next=None, prev=None, head=False, tail=False):
        self.val = val
        self.next = next
        self.prev = prev
        self.head = head
        self.tail = tail


test_case = int(input())

pwd_strings = []
for _ in range(test_case):
    input_str = input()
    head = ListNode(head=True)
    tail = cursor = ListNode(tail=True)
    head.next = tail
    tail.prev = head

    # 입력된 문자열을 연결 리스트로 만들기
    for i in input_str:
        if i == '<':
            if cursor.prev is head:
                continue
            else:
                cursor = cursor.prev
        elif i == '>':
            if cursor is tail:
                continue
            else:
                cursor = cursor.next
        elif i == '-':
            if cursor.prev is head:
                continue
            else:
                prev_node = cursor.prev.prev
                prev_node.next = cursor
                cursor.prev = prev_node
        else:
            new_node = ListNode(i)
            prev_node = cursor.prev
            new_node.prev = prev_node
            new_node.next = cursor
            prev_node.next =new_node
            cursor.prev = new_node

    pwd_strings.append(head.next)

for node in pwd_strings:
    while node.val:
        print(node.val, end='')
        node = node.next
    print()



