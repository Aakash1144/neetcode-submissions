class Solution:
    def house_robber(self, houses: List[int], current_house: int, memo: dict[int, int]) -> int:
        if current_house>=len(houses):
            return 0
        if(current_house in memo):
            return memo[current_house]
        else:
            steal_first_house = houses[current_house] + self.house_robber(houses,current_house + 2, memo)
            skip_steal_first = self.house_robber(houses, current_house + 1, memo)
            memo[current_house] = max(steal_first_house, skip_steal_first)
            return memo[current_house]
    def rob(self, nums: List[int]) -> int:
        return self.house_robber(nums, 0, {})
        