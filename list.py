class ListStack:
    def __init__(self):
        self.__stack = []  

    def push(self, item):
        self.__stack.append(item)
        print(f"{item} pushed into stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
            return None

        return self.__stack.pop()
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None

        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (bottom to top):", self.__stack)

s = ListStack()

s.push(10)
s.push(20)
s.push(30)
s.display()
print("Top element:", s.peek())
print("Popped element:", s.pop())

s.display()