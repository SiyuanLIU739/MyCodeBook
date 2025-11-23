# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakehead = ListNode()
        current = fakehead

        nodes = {}
        while(head is not None):
            if(head.val not in nodes.keys()):
                nodes[head.val] = []
            nodes[head.val].append(head)
            head = head.next

        vals = list(nodes.keys())
        vals.sort()

        for val in vals:
            if(len(nodes[val]) == 1):
                current.next = nodes[val][0]
                nodes[val][0].next = None
                current = current.next

        return fakehead.next