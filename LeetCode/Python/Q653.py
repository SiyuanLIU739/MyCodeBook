class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root, k: int) -> bool:
        array = []

        self.fill_array(root, array)

        l = 0
        r = len(array) - 1

        while(l < r):
            if(array[l] + array[r] == k):
                return True
            
            if(array[l] + array[r] > k):
                r -= 1
            else:
                l += 1
        
        return False



    def fill_array(self, root, a):
        if(root.left != None):
            self.fill_array(root.left, a)

        a.append(root.val)

        if(root.right != None):
            self.fill_array(root.right, a)



    def add_element(self, root, e):
        current = root

        while(True):
            if(current.val > e):
                # left son
                if(current.left == None):
                    current.left = TreeNode(e)
                    break
                else:
                    current = current.left
            
            else:
                if(current.right == None):
                    current.right = TreeNode(e)
                    break
                else:
                    current = current.right



    def build_tree(self, array):
        root = TreeNode(array[0])

        for i in range(1, len(array)):
            self.add_element(root, array[i])

        return root



    def __init__(self):
        array = [5,3,6,2,4,7]
        k = 9
        

        root = self.build_tree(array)

        print(self.findTarget(root, k))




if __name__ == "__main__":
    Solution()
