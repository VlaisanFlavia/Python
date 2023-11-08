from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)

print(queue.peek())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
