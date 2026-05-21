class Solution:

    def hasCycleDFS(self, course, adj_list, visited, path_visited):

        # node already in current DFS path
        if course in path_visited:
            return True

        # already fully processed
        if course in visited:
            return False

        visited.add(course)
        path_visited.add(course)

        for neighbor in adj_list[course]:

            if self.hasCycleDFS(neighbor, adj_list, visited, path_visited):
                return True

        # backtrack
        path_visited.remove(course)

        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build graph
        adj_list = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            adj_list[course].append(prerequisite)

        visited = set()
        path_visited = set()

        # run DFS from every course
        for course in range(numCourses):

            if self.hasCycleDFS(course, adj_list, visited, path_visited):
                return False

        return True