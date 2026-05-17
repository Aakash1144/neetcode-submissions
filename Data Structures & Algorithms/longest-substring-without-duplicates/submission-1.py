class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        seen = set()
        max_window =0
        left = 0
        for right in range(0,len(s)):
            while(s[right] in seen):
                print(seen, s[left])
                seen.remove(s[left])
                left = left + 1
            seen.add(s[right])
            size = right - left + 1
            max_window = max(size, max_window)
        return max_window    