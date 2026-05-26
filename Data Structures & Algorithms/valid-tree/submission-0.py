from collections import defaultdict
class Solution:
    def dfs(self, node, visited, graph):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                self.dfs(nei, visited, graph)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        if len(edges)!= n-1:
            return False
        self.dfs(0, visited, graph)
        return len(visited) == n