class ProductOfNumbers:

    def __init__(self):
        self.last0 = -1
        self.prod = [1]

    def add(self, num: int) -> None:
        if(num == 0):
            self.last0 = len(self.prod)
            self.prod.append(0)
        else:
            if(self.prod[-1] == 0):
                self.prod.append(num)
            else:
                self.prod.append(self.prod[-1] * num)

    def getProduct(self, k: int) -> int:
        ed = len(self.prod) - 1
        st = ed - k + 1

        if(self.last0 >= st):
            return 0

        if(self.last0 == st - 1):
            return self.prod[ed]

        return self.prod[ed] // self.prod[st - 1]  
