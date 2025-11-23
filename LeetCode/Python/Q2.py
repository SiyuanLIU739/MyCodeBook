# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        current = ans

        last = 0
        while(l1 is not None or l2 is not None):
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            val = (val1 + val2 + last) % 10
            node = ListNode(val)
            current.next = node

            last = (val1 + val2 + last) // 10
            current = node
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        if(last == 1):
            current.next = ListNode(last)

        return ans.next