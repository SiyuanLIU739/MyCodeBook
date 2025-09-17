# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        fakehead = ListNode(0, head)

        i = 0
        head = fakehead
        midtail = None
        start = None
        end = None
        midhead = None

        pointer = fakehead
        while(pointer is not None):

            if(i == left - 1):
                midtail = pointer
            if(i == left):
                start = pointer
            if(i == right):
                end = pointer
            if(i == right + 1):
                midhead = pointer
                break

            i += 1
            pointer = pointer.next

        current = start
        next = start.next
        while(next != midhead):
            nextnext = next.next
            next.next = current
            current = next
            next = nextnext

        midtail.next = end
        start.next = midhead

        return fakehead.next