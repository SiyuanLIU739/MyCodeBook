# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = [False]

        sum = head.val
        lastSeen = {head[0]: [0], 0: [-1]}

        node = head.next
        i = 1
        while(node is not None):
            s = sum + node.val
            flag.append(False)

            if(s not in lastSeen.keys()):
                lastSeen[s] = [i]
            else:
                for j in range(lastSeen[s][-1] + 1, i + 1):
                    flag[j] = True
                lastSeen[s].append(i)

            sum = s
            i += 1
            node = node.next

        ans = []
        for j in range(i):
            if(flag[j]):
                head = head.next
                continue
            else:
                ans.append(head)
                head = head.next

        if(len(ans) == 0):
            return None
        
        head = ans[0]
        node = ans[0]
        node.next = None
        for j in range(1, len(ans)):
            node.next = ans[i]
            node = ans[i]

        return head

