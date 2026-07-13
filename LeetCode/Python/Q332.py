class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        available_tickets = {}

        for ticket in tickets:
            fr = ticket[0]
            to = ticket[1]

            if(fr not in available_tickets.keys()):
                available_tickets[fr] = []
            available_tickets[fr].append(to)

        for fr in available_tickets.keys():
            available_tickets[fr].sort()
            available_tickets[fr] = list(reversed(available_tickets[fr]))

        self.it = []

        self.dfs("JFK", available_tickets)
        return list(reversed(self.it))
    
    def dfs(self, fr, tickets):
        if(fr not in tickets.keys() or len(tickets[fr]) == 0):
            self.it.append(fr)
            return
        while(len(tickets[fr]) != 0):
            to = tickets[fr].pop()
            self.dfs(to, tickets)

        self.it.append(fr)