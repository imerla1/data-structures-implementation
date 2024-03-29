from typing import Union


class Node:
    def __init__(self, value, next: Union[None, 'Node'] = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value: Union[None, int] = None) -> None:
        new_node = Node(value) if value is not None else None
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
        # TODO refactor it doesn't work
        # NOTE don't forget update length counter
        if self.head is None:
            return
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            temp, prev = self.head, self.head
            while (temp.next):
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
        self.length -= 1

    def prepend(self, value: int):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop_first(self):
        if self.head is None:
            return
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp

    def get(self, index: int):
        if index < 0 or index >= self.length:
            return
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index: int, value: int):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index: int, value: int):
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.prepend(value)
        elif (index) == self.length:
            self.append(value)
        else:
            node = Node(value)
            temp_prev_node = self.get(index-1)
            node.next = temp_prev_node.next
            temp_prev_node.next = node
            self.length += 1

    def remove(self, index):
        if index < 0 or index > self.length:
            return
        if self.head:
            if index == 0:
                self.pop_first()
            elif index == self.length - 1:
                self.pop()
            else:
                temp = self.get(index - 1)
                element_to_remove = self.get(index)
                temp.next = element_to_remove.next
                self.length -= 1


l = LinkedList(0)
l.append(1)
l.append(2)
l.append(3)
l.append(4)

