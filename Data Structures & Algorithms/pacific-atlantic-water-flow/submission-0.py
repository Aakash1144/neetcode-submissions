class Solution:
    def dfs(self, vertices: List[Tuple[int, int]], visited: Set[Tuple[int, int]], heights: List[List[int]], row: int, col: int):
        stack = list(vertices)
        print("stack ", stack)
        for v in vertices:
            visited.add(v)
        while(stack):
            current_vertex = stack.pop()
            print(current_vertex)
            (r,c) = current_vertex
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                nr = r+dr
                nc = c + dc
                if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited and heights[nr][nc]>= heights[r][c]:
                    visited.add((nr,nc))
                    stack.append((nr,nc))
        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        # Adding border cells to pacific and atlantic
        for c in range(col):
            pacific.add((0,c))
        for r in range(row):
            pacific.add((r,0))
        for r in range(row):
            atlantic.add((r,col-1))
        for c in range(col):
            atlantic.add((row-1,c))
        # run dfs for each vertex in both hash sets
        # run dfs for pacific
        visited_pacific = set()
        visited_pacific = self.dfs(pacific, visited_pacific, heights, row, col)
        print("visited_pacific ", visited_pacific)
        #run dfs for atlantic
        visited_atlantic = set()
        visited_atlantic = self.dfs(atlantic,visited_atlantic, heights, row, col)
        #vertices common in both will be the answer
        print("visited_atlantic ", visited_atlantic)
        results = []
        for p in visited_pacific:
            if(p in visited_atlantic):
                results.append(p)
        print("results ", results)
        return results