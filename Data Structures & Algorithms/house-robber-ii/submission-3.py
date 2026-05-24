class Solution:
    def house_robber(self, houses: List[int], current_house: int, last_house: int, memo: dict[int, int]) -> int:
        # Base case: stop when we cross our specific finish line boundary
        if current_house >= last_house:
            return 0
            
        if current_house in memo:
            return memo[current_house]
            
        # FIX 1: Pass the dynamic 'last_house' boundary straight through unchanged
        steal_first_house = houses[current_house] + self.house_robber(houses, current_house + 2, last_house, memo)
        skip_steal_first = self.house_robber(houses, current_house + 1, last_house, memo)
        
        memo[current_house] = max(steal_first_house, skip_steal_first)
        return memo[current_house]

    def rob(self, nums: List[int]) -> int:
        # FIX 3: Catch 1-house edge case immediately at the entry point
        if len(nums) == 1:
            # Cannot slice or run split scenarios on a single house
            return nums[0]
            
        # FIX 2: Call the helper twice with entirely separate memo dictionaries
        # Scenario A: Can rob from house 0 up to (but excluding) the last house
        rob_first_street = self.house_robber(nums, 0, len(nums) - 1, {})
        
        # Scenario B: Can rob from house 1 up to the very last house
        rob_second_street = self.house_robber(nums, 1, len(nums), {})
        
        return max(rob_first_street, rob_second_street)
