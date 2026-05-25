class Solution:
    def climbStairs(self, n: int) -> int:
        results = 0
        def count_ways(n, total, memo):
            if(n==total):
                return 1
            elif(n< total):
                return 0
            elif(total in memo):
                return memo[total]
            else:
                path1 = count_ways(n, total+1, memo)
                path2 = count_ways(n, total+2, memo)
                memo[total] = path1+ path2
                return memo[total]
        return count_ways(n,0, {})
                