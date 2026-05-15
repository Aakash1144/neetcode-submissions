class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] = freq_dict[num]+1
        sorted_freq_dict = dict(sorted(freq_dict.items(), key = lambda item:item[1],reverse = True))
        print((sorted_freq_dict))
        return list(sorted_freq_dict.keys())[:k]