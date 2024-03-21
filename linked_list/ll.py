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

    def __repr__(self) -> None:
        string_value = ""
        temp = self.head
        while temp is not None:
            string_value += str(temp.value) + "-"
            temp = temp.next
        return string_value
    
    def __len__(self) -> int:
        return self.length
    

    def append(self, value: int):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        



l = LinkedList(3)
l.append(5)
