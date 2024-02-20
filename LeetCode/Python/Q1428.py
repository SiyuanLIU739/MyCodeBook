# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        row = dim[0]
        col = dim[1]

        if(not self.checkColumn(binaryMatrix, row, col - 1)):
            return -1

        return self.binarySearch(binaryMatrix, 0, col - 1, row)
                
    
    def checkColumn(self, binaryMatrix, row, targetC):
        for i in range(row):
            if(binaryMatrix.get(i, targetC) == 1):
                return True
        
        return False
    
    def binarySearch(self, binaryMatrix, l, r, row):
        if(l == r):
            return r
        
        mid = int((l + r) / 2)

        if(self.checkColumn(binaryMatrix, row, mid)):
            return self.binarySearch(binaryMatrix, l, mid, row)
        return self.binarySearch(binaryMatrix, mid + 1, r, row)