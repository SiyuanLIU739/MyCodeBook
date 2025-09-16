# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(None, head)

        head = node

        while(node.next is not None):
            next = node.next

            if(next.val == val):
                node.next = next.next
            else:
                node = next

        return head.next