from typing import Union


class Node:
    def __init__(self, value, next: Union[None, 'Node'] = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1