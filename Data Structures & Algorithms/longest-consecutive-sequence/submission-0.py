class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0
        for num in nums:
            # check the start of the sequence
            if (num-1) not in nums_set:
                # num is start of the sequnece
                current_streak = 1
                current_num = num
                #increment it one by one untill we have num+1 in set
                while((current_num+1) in nums_set):
                    current_streak += 1
                    current_num += 1
                longest_streak = max(current_streak, longest_streak)

        return longest_streak        