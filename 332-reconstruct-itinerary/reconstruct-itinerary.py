from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        tickets.sort(key=lambda x: x[1], reverse=True)
        for src, dst in tickets:
            graph[src].append(dst)
        route = []
        
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            route.append(airport)
            
        dfs("JFK")
        return route[::-1]