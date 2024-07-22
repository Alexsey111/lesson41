class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Удаление из пустого стека")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Запрос элемента из пустого стека")
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    stack = Stack()

    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.is_empty())
    print("Текущий верхний элемент:", stack.peek())
    print("Размер стека:", stack.size())
    print("Удаленный элемент:", stack.pop())
    print("Размер стека после удаления:", stack.size())
