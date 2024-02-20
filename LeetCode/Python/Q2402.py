import heapq

class Meeting:
    def __init__(self, s, t) -> None:
        self.s = s
        self.t = t

    def __lt__(self, other):
        if(self.s == other.s):
            return self.t < other.t
        
        return self.s < other.s

class Room:
    def __init__(self, i, t) -> None:
        self.i = i
        self.t = t

    def __lt__(self, other):
        if(self.t == other.t):
            return self.i < other.i
        
        return self.t < other.t
    
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_count = [0] * n

        available_room = []
        for i in range(n):
            heapq.heappush(available_room, i)

        using_room = []

        meeting = []
        for meet in meetings:
            meeting.append(Meeting(meet[0], meet[1]))
        meeting.sort()

        for meet in meeting:
            s = meet.s
            t = meet.t
            while(len(using_room) != 0):
                if(using_room[0].t <= s):
                    heapq.heappush(available_room, using_room[0].i)
                    heapq.heappop(using_room)

            if(len(available_room) != 0):
                i = available_room[0]
                room_count[i] += 1

                heapq.heappop(available_room)
                heapq.heappush(using_room, Room(i, t))
            else:
                i = using_room[0].i
                room_count[i] += 1
                
                t = using_room[0].t + (t - s)

                heapq.heappop(using_room)
                heapq.heappush(using_room, Room(i, t))

        ans = 0
        ret = -1
        for i in range(n):
            if(room_count[i] > ans):
                ans = room_count[i]
                ret = i

        return ret