# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(k == 1):
            return head

        tail = head

        while(tail.next is not None):
            tail = tail.next

        fake_head = ListNode(0, head)
        fake_tail = ListNode()
        tail.next = fake_tail

        st = fake_head
        ed = None
        current = st
        while(current != fake_tail):
            count = 0
            while(count < k):
                count += 1
                current = current.next

                if(current == fake_tail):
                    break

            if(count < k or current == fake_tail):
                break

            ed = current.next
            print(st.val, ed.val)

            A = st.next
            st.next = current
            current = A
            B = A.next
            A.next = ed
            C = B.next
            while(B != ed):
                B.next = A
                A = B
                B = C
                C = C.next

            st = current

        current = fake_head
        while(current.next != fake_tail):
            current = current.next
        current.next = None

        return fake_head.next
