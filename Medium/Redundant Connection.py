
class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self,x):
        if self.parent[x]!= x:
            self.parent[x]= self.find(self.parent[x])
        return self.parent[x]

    def union(self,a,b):
        pa= self.find(a)
        pb=self.find(b)
        if pa==pb:
            return False
        if self.rank[pa]<self.rank[pb]:
            self.parent[pa]= pb
        elif self.rank[pb] < self.rank[pa]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1
        return True    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        result = None

        for u, v in edges:
            if not dsu.union(u, v):  
                result = [u, v]

        
        return result
        