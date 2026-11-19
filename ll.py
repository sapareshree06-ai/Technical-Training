class __Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.__head = None  

    def push(self, data):
        new_node = __Node(data)

        new_node.next = self.__head
        self.__head = new_node

        print(data, "pushed into stack")

    def pop(self):
        if self.__head is None:
            print("Stack Underflow! Stack is empty")
            return None

        popped = self.__head.data
        self.__head = self.__head.next

        return popped

    def peek(self):
        if self.__head is None:
            print("Stack is empty")
            return None

        return self.__head.data

    def display(self):
        if self.__head is None:
            print("Stack is empty")
            return

        current = self.__head

        print("TOP → ", end="")

        while current is not None:
            print(current.data, end=" → ")
            current = current.next

        print("None")

s = Stack()

s.push(15)
s.push(20)
s.push(30)
s.display()
print("Top element:", s.peek())
print("Popped element:", s.pop())
s.display()