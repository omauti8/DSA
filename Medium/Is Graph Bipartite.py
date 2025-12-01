from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n= len(graph)
        colour = [-1]* n

        for start in range(n):
            if colour[start]==-1:
                queue=deque([start])
                colour[start]=0

                while queue:
                    u= queue.popleft()
                    for v in graph[u]:
                        if colour[v]==-1:
                            colour[v]=1-colour[u]
                            queue.append(v)
                        elif colour[u]==colour[v]:
                            return False
        return True
        