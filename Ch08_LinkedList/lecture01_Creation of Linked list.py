class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return self.val


head = ListNode("Monday")
e2 = ListNode("Tuesday")
e3 = ListNode("Wednesday")

head.next = e2  # Link first Node to second node
e2.next = e3    # Link second Node to third node

node = head
while node is not None:
    print(node, end=' ')
    node = node.next
