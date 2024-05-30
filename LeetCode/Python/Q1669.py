# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail = list2

        a_1 = list1
        b_1 = list1

        while(tail.next is not None):
            tail = tail.next

        for i in range(b + 3):
            if(i < a - 1):
                a_1 = a_1.next

            if(i < b + 1):
                b_1 = b_1.next

        a_1.next = list2
        tail.next = b_1

        return list1