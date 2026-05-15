class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, item in enumerate(nums):
            num2 = target - item
            if num2 in num_dict:
                return [num_dict[num2], index]
            num_dict[item] = index
        return []