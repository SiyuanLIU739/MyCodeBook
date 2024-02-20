class MyQueue:

    def __init__(self):
        self.stack = [[], []]

    def push(self, x: int) -> None:
        pushStack = self.stack[0]
        pushStack.append(x)

    def pop(self) -> int:
        popStack = self.stack[1]

        if(len(popStack) == 0):
            self.fillPop()

        return popStack.pop()

    def peek(self) -> int:
        popStack = self.stack[1]

        if(len(popStack) == 0):
            self.fillPop()

        return popStack[-1]

    def empty(self) -> bool:
        pushStack = self.stack[0]
        popStack = self.stack[1]
        return ((len(pushStack) + len(popStack)) == 0)

    def fillPop(self):
        pushStack = self.stack[0]
        popStack = self.stack[1]

        while(len(pushStack) != 0):
            popStack.append(pushStack.pop())