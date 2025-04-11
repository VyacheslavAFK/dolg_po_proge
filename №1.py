class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.count = 0

    def push(self, value):
        if self.count < self.size:
            self.stack.append(value)
            self.count += 1
            return f"Элемент {value} добавлен"
        else:
            return "Стек переполнен"

    def pop(self, index=0):
        if self.stack:
            item = self.stack[index]
            self.stack.pop(index)
            return f"{item} - удалён"
        else:
            return "В списке нет элементов!"

    def top(self):
        if self.stack:
            return f"Элемент на вершине стека - {self.stack[0]}"
        else:
            return "стек пуст (проверка вершины стека)"

    def is_empty(self):
        if not self.stack:
            return "стек пуст (проверка заполненности стека)"
        else:
            return "в стеке есть элементы"


stack = Stack(5)

print(stack.top(), "\n")
print(stack.is_empty(), "\n\n")
for i in range(1, 8):
    print(stack.push(i))
print(stack.stack, "\n\n")

print(stack.top(), "\n")
print(stack.is_empty(), "\n\n")

for i in range(7):
    print(stack.pop())
print(stack.stack, "\n\n")

print(stack.top(), "\n")
print(stack.is_empty())
