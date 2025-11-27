import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i:[] for i in range(n)}
        for u,v,w in flights:
            graph[u].append((v,w))

        heap = [(0,src,0)]
        dist={(src,0):0}

        while heap:
            cost,node,stops= heapq.heappop(heap)

            if node ==  dst:
                return cost
            if stops>k:
                continue

            for neigh,price in graph[node]:
                newcost= cost+price
                if dist.get((neigh,stops+1),float('inf'))> newcost:
                    dist[(neigh,stops+1)]= newcost
                    heapq.heappush(heap, (newcost, neigh, stops + 1))
        return -1