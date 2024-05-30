# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        current = head

        nodes = []

        while(current is not None):
            nodes.append(current)
            current = current.next

        newNodes = []
        l = 0
        r = len(nodes) - 1

        for i in range(len(nodes)):
            if(i % 2 == 0):
                newNodes.append(nodes[l])
                l += 1
            else:
                newNodes.append(nodes[r])
                r -= 1

        newNodes.append(current)

        for i in range(len(newNodes) - 1):
            newNodes[i].next = newNodes[i + 1]

        
