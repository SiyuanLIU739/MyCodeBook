# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 1
        mid = 1
        midNode = head

        while(head.next is not None):
            cnt += 1
            head = head.next

            if(self.midCnt(cnt) != mid):
                mid += 1
                midNode = midNode.next

        return midNode
    
    def midCnt(self, cnt):
        return cnt // 2 + 1
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        i = 0
        mid = head

        while (head is not None):
            i += 1
            if(i % 2 == 0):
                mid = mid.next
            head = head.next

        return mid