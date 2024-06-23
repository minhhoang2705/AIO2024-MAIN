class MyQueue():
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise IndexError("Queue is full")
        self.queue.append(value)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]


if __name__ == "__main__":
    queue = MyQueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.is_full())
    print(queue.front())
    queue.enqueue(4)
    queue.dequeue()
    print(queue.front())
    print(queue.is_empty())
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue.is_empty())
