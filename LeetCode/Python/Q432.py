class AllOne:

    def __init__(self):
        self.min = 100000
        self.max = 0
        self.key2count = {}
        self.count2key = {}


    def inc(self, key: str) -> None:
        count = 0
        if(key not in self.key2count.keys()):
            count = 1
            self.key2count[key] = count

            if(count not in self.count2key.keys()):
                self.count2key[count] = set()
            self.count2key[count].add(key)

        else:
            self.key2count[key] += 1
            count = self.key2count[key]
            self.count2key[count - 1].remove(key)
            if(count not in self.count2key.keys()):
                self.count2key[count] = set()
            self.count2key[count].add(key)

        if(self.max < count):
            self.max = count

        if(self.min > count):
            self.min = count
        else:
            st = self.min
            while(st <= 50000 and (st not in self.count2key.keys() or len(self.count2key[st]) == 0)):
                st += 1
            self.min = st

    def dec(self, key: str) -> None:
        count = self.key2count[key]
        self.key2count[key] -= 1
        self.count2key[count].remove(key)

        count -= 1
        if(count not in self.count2key.keys()):
            self.count2key[count] = set()
        self.count2key[count].add(key)

        if(count + 1 == self.min):
            if(count != 0):
                self.min = count
            else:
                st = 1
                while(st <= 50000 and (st not in self.count2key.keys() or len(self.count2key[st]) == 0)):
                    st += 1
                self.min = st
        
        if(count == self.max - 1):
            if(len(self.count2key[count + 1]) == 0):
                self.max = count


        

    def getMaxKey(self) -> str:
        if(self.max > 0):
            key = self.count2key[self.max].pop()
            self.count2key[self.max].add(key)
            return key
        return ""


    def getMinKey(self) -> str:
        if(self.min > 50000):
            return ""
        key = self.count2key[self.min].pop()
        self.count2key[self.min].add(key)
        return key