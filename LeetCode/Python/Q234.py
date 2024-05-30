# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []

        current = head

        while(current is not None):
            vals.append(current.val)
            current = current.next

        l = 0
        r = len(vals) - 1

        while(l < r):
            print(l, r)
            if(vals[l] != vals[r]):
                return False
            l += 1
            r -= 1
            
        return True