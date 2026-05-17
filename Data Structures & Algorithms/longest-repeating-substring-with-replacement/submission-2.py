class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_size = 0
        for right in range(0, len(s)):
            if s[right] in freq:
                freq[s[right]]+=1
            else:
                freq[s[right]] = 1
            size = right - left + 1 
            while((size - max(freq.values())>k) and left<=right):
                freq[s[left]] = freq[s[left]] - 1
                left = left + 1       
                size = right - left + 1
            max_size = max(size, max_size)
        return max_size