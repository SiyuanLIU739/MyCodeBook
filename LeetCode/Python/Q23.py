# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from bisect import bisect_left

class CompNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        fakehead = ListNode()
        current = fakehead

        heap = []
        for l in lists:
            if(l is not None):
                heap.append(CompNode(l))
        heap = sorted(heap)

        while(len(heap) != 0):
            top = heap.pop(0).node
            current.next = top
            current = top

            top = top.next
            if(top is not None):
                top = CompNode(top)
                index = bisect_left(heap, top)
                heap.insert(index, top)

        return fakehead.next
