class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_num = sorted(nums)
        temp_sum = 0
        triplets = set()
        for i in range(0, len(nums)-1):
            target = 0-sorted_num[i]
            left = i+1
            right = len(nums)-1
            while(left<right):
                temp_sum = sorted_num[left] + sorted_num[right]
                if(temp_sum == target):
                    triplets.add((sorted_num[i],
                    sorted_num[left],sorted_num[right]))
                    left = left+1
                    right = right-1
                elif(temp_sum<target):
                    left = left+1
                else:
                    right = right-1
        print(triplets)

        return list(triplets)