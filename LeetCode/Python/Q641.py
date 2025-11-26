class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.l = 1
        self.r = 0
        self.queue = [0] * k
        self.n = 0

    def insertFront(self, value: int) -> bool:
        if(self.isFull()):
            return False
        l = (self.l + self.k - 1) % self.k
        self.l = l
        self.queue[l] = value
        self.n += 1
        return True

    def insertLast(self, value: int) -> bool:
        if(self.isFull()):
            return False
        r = (self.r + 1) % self.k
        self.r = r
        self.queue[r] = value
        self.n += 1
        return True

    def deleteFront(self) -> bool:
        if(self.isEmpty()):
            return False
        self.l = (self.l + 1) % self.k
        self.n -= 1
        return True

    def deleteLast(self) -> bool:
        if(self.isEmpty()):
            return False
        self.r = (self.r + self.k - 1) % self.k
        self.n -= 1
        return True

    def getFront(self) -> int:
        if(self.n == 0):
            return -1
        return self.queue[self.l]

    def getRear(self) -> int:
        if(self.n == 0):
            return -1
        return self.queue[self.r]

    def isEmpty(self) -> bool:
        return self.n == 0

    def isFull(self) -> bool:
        return self.n == self.k