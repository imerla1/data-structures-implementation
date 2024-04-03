class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def ___len__(self):
        return self.height
    
    def __repr__(self):
        string_value = "top\n↓"
        temp = self.top
        while temp is not None:
            string_value += f"\n{temp.value}"
            temp = temp.next
            if temp:
                string_value += "\n↓"
        string_value += "\nbottom"
        return string_value


    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = Node
        else:
            temp = self.top
            new_node.next = temp
            self.top = new_node
        self.height += 1


stack = Stack(5)
stack.push(444)