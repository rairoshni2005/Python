class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        # Add an element to the top of the stack
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            # Remove and return the element from the top of the stack
            popped_item = self.items.pop()
            print(f"Popped: {popped_item}")
            return popped_item
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            # Return the element from the top of the stack without removing it
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek.")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack Size:", stack.size())
print("Top Element:", stack.peek())

stack.pop()
stack.pop()
stack.pop()

print("Stack Size after Popping:", stack.size())
