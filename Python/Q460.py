class Node:
    def __init__(self, prev, nxt, frequency):
        self.keys = []
        self.n_keys = 0

        self.prev = prev
        self.nxt = nxt

        self.frequency = frequency

        if(prev != None):
            prev.nxt = self
        if(nxt != None):
            nxt.prev = self

    def getkeys(self):
        return self.n_keys
    
    def key(self):
        return self.keys[0]
    
    def addkey(self, key):
        self.keys.append(key)
        self.n_keys += 1
    
    def delkey(self, key):
        self.keys.remove(key)
        self.n_keys -= 1

    def delnode(self):
        prev = self.prev
        nxt = self.nxt

        prev.nxt = nxt
        nxt.prev = prev

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0

        self.head = Node(None, None, None)
        self.tail = Node(self.head, None, None)
        self.head.nxt = self.tail

        self.k_v = {}
        self.k_f = {}
        self.f_n = {}

    def get(self, key: int) -> int:
        if(key not in self.k_v.keys()):
            return -1
        
        # update frequency
        frequency = self.k_f[key]
        newFrequency = frequency + 1
        self.k_f[key] = newFrequency

        fNode = self.f_n[frequency]

        # upd new frequency node
        newfNode = None
        if(newFrequency in self.f_n.keys()):
            newfNode = self.f_n[newFrequency]
        else:
            newfNode = Node(fNode, fNode.nxt, newFrequency)
        newfNode.addkey(key)
        self.f_n[newFrequency] = newfNode

        # upd old frequency node
        if(fNode.getkeys() == 1):
            fNode.delnode()

            self.f_n.pop(frequency)
        else:
            fNode.delkey(key)

        return self.k_v[key]
        

    def put(self, key: int, value: int) -> None:


        # insert a key
        if(key not in self.k_v.keys()):
            # get a capacity for this value
            if(self.count == self.capacity):
                # no capacity at all
                if(self.count == 0):
                    return
                
                #delete a key

                frequency = self.head.nxt.frequency
                fNode = self.head.nxt
                k = fNode.key()
                self.k_v.pop(k)
                self.k_f.pop(k)

                if(fNode.getkeys() == 1):
                    # 1 least frequently used value, del the node
                    fNode.delnode()

                    #remove f-n
                    self.f_n.pop(frequency)

                else:
                    # del the head of the frequency 
                    fNode.delkey(k)
                
                self.count -= 1

            self.k_v[key] = value

            frequency = 1
            self.k_f[key] = frequency

            fNode = None
            if(frequency in self.f_n.keys()):
                fNode = self.f_n[frequency]
            else:
                fNode = Node(self.head, self.head.nxt, frequency)
            fNode.addkey(key)
            self.f_n[frequency] = fNode

            self.count += 1

        else:
            # no need to extra space

            self.k_v[key] = value
            
            frequency = self.k_f[key]
            newFrequency = frequency + 1
            self.k_f[key] = newFrequency

            fNode = self.f_n[frequency]

            # upd new frequency node
            newfNode = None
            if(newFrequency in self.f_n.keys()):
                newfNode = self.f_n[newFrequency]
            else:
                newfNode = Node(fNode, fNode.nxt, newFrequency)
            newfNode.addkey(key)
            self.f_n[newFrequency] = newfNode

            # upd old frequency node
            if(fNode.getkeys() == 1):
                fNode.delnode()

                self.f_n.pop(frequency)
            else:
                fNode.delkey(key)


import pandas as pd

df1 = pd.DataFrame()
df2 = pd.DataFrame()

df = df1.pivot_table()