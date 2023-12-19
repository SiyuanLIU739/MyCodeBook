class MinStack:

    def __init__(self):
        self.indicator = -1
        self.ori = []
        self.min = []

    def push(self, val: int) -> None:
        self.indicator += 1
        self.ori.append(val)

        if(self.indicator == 0):
            self.min.append(val)
        else:
            self.min.append(val if (val < self.min[-1]) else self.min[-1])

    def pop(self) -> None:
        self.min.pop()
        self.ori.pop()

    def top(self) -> int:
        return self.ori[-1]

    def getMin(self) -> int:
        return self.min[-1]
        

