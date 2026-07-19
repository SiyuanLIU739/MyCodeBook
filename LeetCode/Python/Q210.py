from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0] * numCourses
        outs = [[] for i in range(numCourses)]

        for prerequisite in prerequisites:
            outs[prerequisite[1]].append(prerequisite[0])
            in_degrees[prerequisite[0]] += 1

        q = deque()
        order = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                q.append(i)
                order.append(i)

        while(q):
            course = q.popleft()
            for out in outs[course]:
                in_degrees[out] -= 1
                if(in_degrees[out] == 0):
                    q.append(out)
                    order.append(out)

        if(len(order) == numCourses):
            return order
        
        return []