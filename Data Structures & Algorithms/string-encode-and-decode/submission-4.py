class Solution:
    def encode(self, strs: list[str]) -> str:
        # Format: [length] + [#] + [string]
        # Example: ["hi", "hello"] -> "2#hi5#hello"
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            # Find the delimiter to get the length
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            # The string starts after the '#' and lasts for 'length' characters
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the pointer to the start of the next length prefix
            i = j + 1 + length
        return res
