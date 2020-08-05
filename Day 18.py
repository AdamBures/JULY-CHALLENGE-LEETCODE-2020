class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # dic[i] is the indegree of the node i,  computing will be faster
        dic  = [0 for i in range(numCourses)]
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i] += 1;
            neigh[j].add(i)
        stack  = [i for i in range(numCourses) if dic[i] == 0];
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i] -= 1
                if dic[i] == 0:
                    stack.append(i)
        for i in range(numCourses):
            if dic[i] > 0:
                return []
        return res
