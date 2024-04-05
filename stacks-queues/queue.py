class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class Queue:
    def __init__(self, value = None) -> None:
        new_node = Node(value) if value is not None else None
        # deque
        self.front = new_node if new_node else None
        # enqueue, last
        self.rear = new_node if new_node else None
        self.length = 1 if new_node else 0

    def __len__(self):
        return self.length
    
    def __repr__(self) -> str:
        ret_str = "front -> "
        temp = self.front
        while temp is not None:
            ret_str += f"{temp.value} |"
            temp = temp.next
        ret_str += " -> rear"
        return ret_str


    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return
        item_to_pop = self.rear

        if self.length == 1:
            self.rear = None
            self.front = None
        else:
            self.front = self.front.next
        item_to_pop.next = None

            
        self.length -= 1
        return item_to_pop
        
        


q = Queue()
q.enqueue(5)
q.enqueue(25)
q.enqueue(99)