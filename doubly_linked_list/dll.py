class Node:
    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, value=None) -> None:
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

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node

        elif self.length == 1:
            node.prev = self.head
            self.head.next = node
            self.tail = node
        else:
            temp = self.tail
            node.prev = temp
            self.tail.next = node
            self.tail = node

        # update length counter
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            node.next = temp
            temp.prev = node
            self.head = node

        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            next_to_head = self.head.next
            self.head = next_to_head
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def pop(self):
        if self.length == 0:
            return
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.tail
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
            self.length -= 1
            return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return

        elif index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - 1 - index):
                temp = temp.prev
            return temp

    def set_value(self, index, new_value):
        item = self.get(index)
        if item:
            item.value = new_value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("LinkedList index out of range")

        new_node = Node(value)

        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return

        current_node = self.get(index)
        previous_node = current_node.prev

        previous_node.next = new_node
        new_node.prev = previous_node
        new_node.next = current_node
        current_node.prev = new_node

        self.length += 1

    def remove(self, index):
        if self.length == 0:
            return 
        elif index < 0 or index > self.length:
            raise IndexError("LinkedList index out of range")
        elif index == 0:
            self.pop_first()
            return
        elif index == self.length:
            self.pop()
            return
        else:
            node_to_remove = self.get(index)
            prev = node_to_remove.prev
            prev.next = node_to_remove.next
            self.length -= 1
            

if __name__ == "__main__":
    dll = DoublyLinkedList(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
