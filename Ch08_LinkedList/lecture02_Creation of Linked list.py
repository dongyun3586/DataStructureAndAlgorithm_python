from Node import Node

tail = Node(tail=True)
node1 = Node('A')
node2 = Node('B')
node1.set_next(node2)
node2.set_next(tail)
head = Node(head=True, next=node1)

node = head.next
while node is not tail:
    print(node)
    node = node.next



