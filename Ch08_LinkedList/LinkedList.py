from Node import Node


class SinglyLinkedList:
    node_head = ''
    node_tail = ''
    size = 0

    def __init__(self):
        self.node_tail = Node(tail=True)
        self.node_head = Node(head=True, next=self.node_tail)

    def insertAt(self, value, index_insert):
        node_new = Node(value=value)
        node_prev = self.get(index_insert - 1)
        node_new.set_next(node_prev.next)
        node_prev.set_next(node_new)
        self.size += 1

    def removeAt(self, index_remove):
        node_prev = self.get(index_remove - 1)
        node_remove = node_prev.get_next()
        node_prev.set_next(node_remove.get_next())
        self.size -= 1
        return node_remove.get_value()

    def get(self, index_retrieve):
        node_return = self.node_head
        for i in range(index_retrieve + 1):
            node_return = node_return.get_next()
        return node_return

    def print_status(self):
        node_current = self.node_head
        while node_current.get_next().is_tail() == False:
            node_current = node_current.get_next()
            print(node_current.get_value(), end=" ")
        print()

    def get_size(self):
        return self.size
