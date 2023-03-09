class Node:
    next = None
    value = ''
    head = False
    tail = False

    def __init__(self, value='', next=None, head=False, tail=False):
        self.next = next
        self.value = value
        self.head = head
        self.tail = tail

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def is_head(self):
        return self.head

    def is_tail(self):
        return self.tail

    def __str__(self):
        return self.value
