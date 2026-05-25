class Solution:
    def longest_common_sub(self, text1: str, text2: str, index1: int, index2: int, memo: dict[tuple[int, int], int]) -> str:
        if(index1>= len(text1) or index2>= len(text2)):
            return 0
        if((index1, index2) in memo):
            return memo[(index1, index2)]
        
        if(text1[index1] == text2[index2]):
            memo[(index1, index2)] = 1 + self.longest_common_sub(text1, text2, index1+1, index2+1, memo)
            return memo[(index1, index2)]
        
        else:
            sub_1 = self.longest_common_sub(text1, text2, index1+1, index2, memo)
            sub_2 = self.longest_common_sub(text1, text2, index1, index2+1, memo)
            memo[(index1, index2)] = max(sub_1, sub_2)
            return memo[(index1, index2)]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longest_common_sub(text1, text2, 0, 0, {})