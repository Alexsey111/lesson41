class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.queue[0]

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    queue = Queue()

    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.is_empty())
    print("Текущий первый элемент:", queue.front())
    print("Размер очереди:", queue.size())
    print("Удаленный элемент:", queue.dequeue())
    print("Размер очереди после удаления:", queue.size())
