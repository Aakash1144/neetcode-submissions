from collections import deque
class Solution:
    
    def bfs(self, vertex, grid, row, col, visited):
        print("vertex ", vertex)
        current_vertex = vertex
        queue = []
        queue = deque([current_vertex])
        visited.add(current_vertex)

        while(queue):
            (r, c) = queue.popleft()
            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                print("checking neighbour at ", (nr,nc))
                if 0<=nr< row and 0<=nc< col and (nr,nc) not in visited and grid[nr][nc] == "1":
                    queue.append((nr,nc))
                    visited.add((nr,nc))
        print("visited ", visited)    

    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        islands = 0
        visited = set()
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                print("point and visted ", (r,c), visited) 
                if grid[r][c]=="1" and (r,c) not in visited:
                    # code to run bfs
                    self.bfs((r,c), grid, row, col, visited)
                    islands +=1

        return islands
        