from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = []
        for i in range(length):
            self.snaps.append({
                "snap_ids": [-1], 
                'vals': [0]
            })

        self.arr = [0] * length
        self.id = -1
        self.updated = set()

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        self.updated.add(index)

    def snap(self) -> int:
        self.id += 1

        for i in self.updated:
            if(self.arr[i] != self.snaps[i]['vals'][-1]):
                self.snaps[i]['snap_ids'].append(self.id)
                self.snaps[i]['vals'].append(self.arr[i])

        self.updated.clear()
        
        return self.id

    def get(self, index: int, snap_id: int) -> int:
        snap_ids = self.snaps[index]['snap_ids']
        vals = self.snaps[index]['vals']

        i = bisect_right(snap_ids, snap_id)
        i -= 1

        return vals[i]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)