from bisect import bisect_left

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        
        ans = 0
        while(len(people) > 0):
            ans += 1

            p = people.pop(0)
            if(len(people) == 0):
                break

            w = limit - p
            index = bisect_left(people, w)
            if(index == len(people) or w != people[index]):
                index -= 1

            if(index != -1):
                people.pop(index)

        return ans