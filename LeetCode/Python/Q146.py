class Node:
    def __init__(self, key, value, prev, nxt):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

        if(prev != None):
            prev.nxt = self
        if(nxt != None):
            nxt.prev = self
    
    def delNode(self):
        p = self.prev
        n = self.nxt

        p.nxt = n
        n.prev = p

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}

        self.head = Node(0, 0, None, None)
        self.tail = Node(0, 0, self.head, None)
        self.head.nxt = self.tail

        self.capacity = capacity
        self.len = 0

    def get(self, key: int) -> int:
        if(key in self.cache):
            node = self.cache[key]

            value = node.value

            node.delNode()

            self.cache[key] = Node(key, value, self.head, self.head.nxt)

            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #update 
        if(key in self.cache):
            self.get(key)
            self.cache[key].value = value
            return

        node = Node(key, value, self.head, self.head.nxt)     
        if(self.len == self.capacity):
            n = self.tail.prev
            n.delNode()
            self.cache.pop(n.key)
        else:
            self.len += 1
        self.cache[key] = node