import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph ={i:[] for i in range(1,n+1)}

        for u,v,w in times:
            graph[u].append((v,w))

        min_heap= [(0,k)]
        dist={i: float('inf') for i in range(1,n+1)}
        dist[k]=0

        while min_heap:
            time, node=heapq.heappop(min_heap)

            if time > dist[node]:
                continue

            for neigh , w in graph[node]:
                new_time = time+w

                if new_time< dist[neigh]:
                    dist[neigh]= new_time
                    heapq.heappush(min_heap,(new_time, neigh))
        
        max_time= max(dist.values())
        return -1 if max_time == float('inf') else max_time 
