class Node:
    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, value: None) -> None:
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
