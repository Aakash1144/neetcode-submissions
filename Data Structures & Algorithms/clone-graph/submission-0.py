"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, vertex):
        visited = {}
        stack = [vertex]
        visited[vertex] = Node(vertex.val, [])
        while(stack):
            current_vertex = stack.pop()
            copy_node = visited[current_vertex]
            for adj_vertex in current_vertex.neighbors:
                if adj_vertex not in visited:
                    adj_copy_node = Node(adj_vertex.val, [])
                    visited[adj_vertex] = adj_copy_node
                    stack.append(adj_vertex)
                
                copy_node.neighbors.append(visited[adj_vertex])
        return visited

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = self.dfs(node)
        return visited[node]