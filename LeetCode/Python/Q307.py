class NumArray:

    def __init__(self, nums: List[int]):
        self.n = 40000
        self.tree = [0] * 1000000 # > 4 * n to be safe
        for i in range(len(nums)):
            self.Update(i, nums[i], 0, self.n, 1)


    def update(self, index: int, val: int) -> None:
        self.Update(index, val, 0, self.n, 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumrange(left, right, 0, self.n, 1)
    
    def Update(self, index, val, l, r, pos):
        if(l == r):
            self.tree[pos] = val
            return
        
        mid = (l + r) // 2

        if(index <= mid):
            self.Update(index, val, l, mid, pos * 2)
        else:
            self.Update(index, val, mid + 1, r, pos * 2 + 1)
        
        self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]
        return
    
    def sumrange(self, s, t, l, r, pos):
        if(s <= l and t >= r):
            return self.tree[pos]
        
        mid = (l + r) // 2

        if(t <= mid):
            return self.sumrange(s, t, l, mid, pos * 2)
        elif(s > mid):
            return self.sumrange(s, t, mid + 1, r, pos * 2 + 1)
        else:
            return self.sumrange(s, t, l, mid, pos * 2) + self.sumrange(s, t, mid + 1, r, pos * 2 + 1)
        