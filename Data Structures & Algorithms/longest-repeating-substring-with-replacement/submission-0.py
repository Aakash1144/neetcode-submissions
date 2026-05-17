class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        freq = {}
        max_window = 0

        for right in range(len(s)):

            # expand window
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1

            size = right - left + 1

            # shrink if invalid
            while size - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1

                # IMPORTANT:
                # size changes after left moves
                size = right - left + 1

            max_window = max(max_window, size)

        return max_window