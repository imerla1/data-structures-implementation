from typing import Union


class Node:
    def __init__(self, value, next: Union[None, 'Node'] = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value: Union[None, int] = None) -> None:
        new_node = Node(value) if value else None
        self.head = new_node if new_node else None
        self.tail = new_node if new_node else None
        self.length = 1 if new_node else 0

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

    def pop(self):
        if self.head is None:
            return
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp

        new_tail_index = self.length - 1
        temp_tail = self.tail
        temp = self.head
        new_tail = None
        for _ in range(new_tail_index):
            new_tail = temp
            temp = temp.next
        self.tail = new_tail
        self.length -= 1
        return temp_tail

    def prepend(self, value: int):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
    


l = LinkedList(6)
l.append(5)
l.append(6)
l.append(235)
l.append(54)
