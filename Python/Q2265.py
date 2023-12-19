class Solution:
    ans = 0
    def transverse(self, root):
        if(root == None):
            return (0, 0)
        
        nNodes = 1
        sumVal = root.val

        leftNodes, leftVal = self.transverse(root.left)
        rightNodes, rightVal = self.transverse(root.right)

        nNodes = nNodes + leftNodes + rightNodes
        sumVal = sumVal + leftVal + rightVal

        avg = (int)(nNodes/sumVal)

        if(avg == root.val):
            self.ans += 1
        
        return (nNodes, sumVal)
    
    def averageOfSubtree(self, root) -> int:
        self.transverse(root)
        return self.ans