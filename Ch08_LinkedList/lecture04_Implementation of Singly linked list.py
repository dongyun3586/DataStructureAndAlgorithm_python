from SinglyLinkedList import SinglyLinkedList

list1 = SinglyLinkedList()
list1.insertAt('A', 0)
list1.insertAt('C', 1)
list1.insertAt('D', 2)
list1.insertAt('E', 2)
list1.print_status()

list1.insertAt('B', 1)
list1.print_status()

list1.removeAt(3)
list1.print_status()