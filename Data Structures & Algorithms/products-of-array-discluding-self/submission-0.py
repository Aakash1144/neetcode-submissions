class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_dict = {}
        prod = 1
        zero_index = []
        for i, num in enumerate(nums):
            if num == 0:
                zero_index.append(i)
                continue
            else:
                prod = prod*num
        if len(zero_index)>1:
            return [0 for num in nums]
        if len(zero_index)==1:
            return [0 if i!=zero_index[0] else prod for i, num in enumerate(nums)]            
        return [int(prod/num) for i, num in enumerate(nums)]


