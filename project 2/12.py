class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top element without removing it
        else:
            return None  # Or raise an exception if you prefer

    def traverse(self):
        for item in self.items:
            print(item)  # Print each item in the stack

S = Stack()
S.push(2)
S.push(3)
S.push(4)
S.push(6)
S.traverse()  # Should output: 2, 3, 4, 6

print(S.peek())  # Should output: 6