class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def __init__(self):
        self.ans = -(3 * 10000 * 1000 + 1)



    def maxPathSum(self, root) -> int:
        self.find_path_max(root, 0)

        return self.ans
    


    def find_path_max(self, root, father_sum):
        this_sum = father_sum + root.val
        self.ans = self.max(self.ans, root.val)

        left_sum = right_sum = -(3 * 10000 * 1000 + 1)

        if(root.left != None):
            left_sum = self.find_path_max(root.left, this_sum)
            self.ans = self.max(left_sum - father_sum, self.ans)

        if(root.right != None):
            right_sum = self.find_path_max(root.right, this_sum)
            self.ans = self.max(right_sum - father_sum, self.ans)

        if(root.left != None and root.right != None):
            self.ans = self.max(self.ans, left_sum + right_sum - 2 * father_sum - root.val)

        return self.max(self.max(left_sum, right_sum), this_sum)
        




    def max(self, a, b):
        if(a > b):
            return a
        return b
    
    def min(self, a, b):
        if(a > b):
            return b
        return a
    


def build_tree(tree):
    root = TreeNode(tree[0])

    l = []
    l.append(root)

    for i in range(1, len(tree), 2):
        father = l.pop(0)

        left_son = right_son = None

        if(tree[i] != None):
            left_son = TreeNode(tree[i])
            l.append(left_son)
        if(tree[i + 1] != None):
            right_son = TreeNode(tree[i + 1])
            l.append(right_son)
        father.left = left_son
        father.right = right_son

    return root




def main():
    tree = [-2, 1, None]

    root = build_tree(tree)

    sol = Solution()
    print(sol.maxPathSum(root))



if __name__ == "__main__":
    main()
