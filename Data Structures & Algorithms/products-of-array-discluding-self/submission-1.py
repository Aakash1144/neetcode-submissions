class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_dict = {}
        prod = 1
        prefix_prod = [1]
        suffix_prod = [1]
        
        for i in range(0,len(nums)-1):
            prod = prod*nums[i]
            prefix_prod.append(prod)
        print(prefix_prod)

        nums_rev = nums[::-1]
        prod =1
        for i in range(0,len(nums_rev)-1):
            prod = prod*nums_rev[i]
            suffix_prod.append(prod)
        suffix_prod = suffix_prod[::-1]
        print(suffix_prod)
        output = []
        for i in range(0, len(nums)):
            output.append(int(prefix_prod[i]*suffix_prod[i]))
        return output    