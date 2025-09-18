# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead = None
        evenHead = None
        oddtail = oddHead
        eventail = evenHead

        while(head is not None):
            if(head.val % 2 == 0):
                # first node
                if(evenHead is None):
                    evenHead = head
                    eventail = head
                else:
                    eventail.next = head
                    eventail = head
            else:
                if(oddHead is None):
                    oddHead = head
                    oddtail = oddHead
                else:
                    oddtail.next = head
                    oddtail = head
            head = head.next

        if(oddHead is None):
            return evenHead
        
        oddtail.next = evenHead.next
        return oddHead