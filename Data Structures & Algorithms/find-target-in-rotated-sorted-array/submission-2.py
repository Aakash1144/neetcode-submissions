class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1

        while(lo<=hi):
            mid = (lo + hi)//2
            if(nums[mid]==target):
                return mid
            if(nums[lo]<= nums[mid]):
                # left half is sorted
                if(target>= nums[lo] and target<nums[mid]):
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if(target>nums[mid] and target<=nums[hi]):
                    lo = mid+1
                else:
                    hi = mid-1
        return -1
        