class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isempty():
            return self.stack.pop()

    def isempty(self):
        return True if len(self.stack) == 0 else False


myStack = Stack()
lines = list(input().strip().split())
for line in lines:
    if line.isnumeric():
        myStack.push(int(line))
    elif line in "-+*":
        val2 = myStack.pop()
        val1 = myStack.pop()
        if line == "+":
            sol = val1 + val2
        elif line == "-":
            sol = val1 - val2
        elif line == "*":
            sol = val1 * val2
        myStack.push(sol)
print(myStack.pop())
