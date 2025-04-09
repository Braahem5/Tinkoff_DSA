class Stack:
    def __init__(self):
        self.stack = []
        self.minEle = -1  # to track the min element

    def push(self, value):
        # if the stack is empty
        if not self.stack:
            self.minEle = value
            self.stack.append(value)
        elif value < self.minEle:
            self.stack.append(
                2 * value - self.minEle
            )  # we append a modified value if it is less than the minEle
            self.minEle = value  # then we update the minElement
        else:
            self.stack.append(value)  # here value is > than minElment

    def pop(self):
        if not self.stack:
            return

        top = self.stack.pop()

        # Minimum will change, if the minimum element
        # of the stack is being removed.
        if top < self.minEle:
            self.minEle = 2 * self.minEle - top  # to get the previous min element

    def minVal(self):
        if not self.stack:
            return

        return self.minEle

    def peek(self):
        if not self.stack:
            return

        top = self.stack[-1]

        return self.minEle if self.minEle > top else top


myStack = Stack()
n = int(input().strip())
for x in range(n):
    value = list(map(int, input().strip().split()))

    if len(value) == 1:
        t = value[0]
        val = None
    else:
        t, val = value

    if t == 1:
        myStack.push(val)
    elif t == 2:
        myStack.pop()
    elif t == 3:
        minimum = myStack.minVal()
        print(minimum)
