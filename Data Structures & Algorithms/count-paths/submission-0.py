class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def find_unique_paths(m, n, row, col, memo):
            if(row>m-1 or col>n-1):
                return 0
            if(m==0 and n==0):
                return 0
            if((row, col) in memo):
                return memo[(row, col)]
            if(row== m-1 and col == n-1):
                return 1
            else:
                path1 = find_unique_paths(m,n,row, col+1, memo)
                path2 = find_unique_paths(m,n,row+1, col, memo) 
                memo[(row, col)] = path1 + path2
                return memo[(row, col)]
        return find_unique_paths(m,n,0,0, {})