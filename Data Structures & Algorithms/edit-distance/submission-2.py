class Solution:
    def find_min_distance(self, s1: str, s2: str, index1: int, index2: int, memo: dict[[int,int], int]) -> int:
        if(index1 == len(s1)):
            return len(s2)-index2
        if(index2 == len(s2)):
            return len(s1)-index1
        # 2. Check the notepad
        if (index1, index2) in memo:
            return memo[(index1, index2)]

        if(s1[index1] == s2[index2]):
            return self.find_min_distance(s1, s2, index1+1, index2+1, memo)
        else:
            delete_op = 1 + self.find_min_distance(s1, s2, index1+1, index2, memo)
            insert_op = 1 + self.find_min_distance(s1, s2, index1, index2+1, memo)
            replace_op = 1 + self.find_min_distance(s1, s2, index1+1, index2+1, memo)
        memo[(index1, index2)] = min(delete_op, insert_op, replace_op)
        
        return memo[(index1, index2)]
    def minDistance(self, word1: str, word2: str) -> int:
        return self.find_min_distance(word1, word2, 0,0, {})
        