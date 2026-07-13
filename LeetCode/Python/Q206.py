# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        
        current = head
        while(current is not None):
            nodes.append(current)
            current = current.next

        if(len(nodes) == 0):
            return None 
            
        nodes[0].next = None

        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]

        return nodes[-1]
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None):
            return None

        a = head
        if(a.next is None):
            return a
        
        b = a.next
        a.next = None
        if(b.next is None):
            b.next = a
            return b
        
        c = b.next
        while(c is not None):
            c = b.next
            b.next = a
            a = b
            b = c

        return a