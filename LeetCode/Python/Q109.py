# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while(head is not None):
            nums.append(head.val)
            head = head.next

        return self.buildTree(nums)
    
    def buildTree(self, nums):
        if(len(nums) == 0):
            return None
        
        mid = len(nums) // 2
        return TreeNode(nums[mid], self.buildTree(nums[: mid]), self.buildTree(nums[mid + 1: ]))

        