# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        if(head is None):
            return None
        
        nodes.append(head)
        while(head.next is not None):
            nodes.append(head.next)
            head = head.next

        if(len(nodes) == 1):
            return None
        
        if(len(nodes) == n):
            return nodes[1]
        
        if(n == 1):
            nodes[-2].next = None
        else:
            k = len(nodes) - n
            nodes[k - 1].next = nodes[k + 1]
        
        return nodes[0]