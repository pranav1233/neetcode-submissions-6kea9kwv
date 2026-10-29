class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)

        for crs,pre in prerequisites:
            prereq[crs].append(pre)

        visited = set()

        def dfs(cur):
            if cur in visited:
                return False

            if prereq[cur] == []:
                return True

            visited.add(cur)

            for pre in prereq[cur]:
                if dfs(pre) == False:
                    return False

            visited.remove(cur)
            prereq[cur] = []

            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False

        return True


            