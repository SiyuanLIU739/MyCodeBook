# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        
        current = head
        nodes = {}
        while(current is not None):
            nodes[n] = current
            current = current.next
            n += 1

        if(n == 0):
            return head
        k = k % n
        if(k == 0):
            return head

        for i in range(n):
            nodes[i].next = None

        fakehead = ListNode(0, nodes[n - k])
        current = fakehead.next
        start = (n - k + 1) % n
        while(start != n - k):
            current.next = nodes[start]
            current = current.next
            start = (start + 1) % n

        return fakehead.next