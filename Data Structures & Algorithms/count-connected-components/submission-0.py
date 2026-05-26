from collections import defaultdict
class Solution:
    def dfs(self, node, visited, graph):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                self.dfs(nei, visited, graph)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        visited = set()
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                self.dfs(node, visited, graph)
        return components