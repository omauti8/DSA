class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        indegree = [0]* numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        q= deque([i for i in range(numCourses) if indegree[i]==0])

        order=[]
        while q:
            node= q.popleft()
            order.append(node)

            for neighbour in adj[node]:
                indegree[neighbour] -=1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        if len(order) != numCourses:
            return []

        return order
