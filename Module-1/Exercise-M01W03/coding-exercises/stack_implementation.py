class MyStack():
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def push(self, value):
        if self.is_full():
            raise IndexError("Stack is full")
        self.stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]


if __name__ == "__main__":
    stack = MyStack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.is_full())
    print(stack.top())
    stack.push(4)
    stack.pop()
    print(stack.top())
    print(stack.is_empty())
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.is_empty())
