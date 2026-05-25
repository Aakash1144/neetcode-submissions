class Solution:

    def longestPalindrome(self, s: str) -> str:

        memo = {}

        def is_palindrome(left, right):

            if left >= right:
                return True

            if (left, right) in memo:
                return memo[(left, right)]

            if s[left] != s[right]:
                memo[(left, right)] = False
                return False

            memo[(left, right)] = is_palindrome(left + 1, right - 1)

            return memo[(left, right)]

        longest = ""

        for i in range(len(s)):

            for j in range(i, len(s)):

                if is_palindrome(i, j):

                    current = s[i:j + 1]

                    if len(current) > len(longest):
                        longest = current

        return longest