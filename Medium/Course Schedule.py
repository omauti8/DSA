class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses) }
        indegree= [0]* numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        q=deque([i for i in range(numCourses) if indegree[i]==0 ])
        count=0

        while q:
            node= q.popleft()
            count +=1

            for neigh in adj[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        return count == numCourses