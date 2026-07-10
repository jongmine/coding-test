class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# node = Node(5)
# print(node.data, node.next)
#
# next_node = Node(3)
# node.next = next_node


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # LinkedList의 가장 끝에 있는 노드에 새로운 노드를 연결
    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = Node(value)

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()



