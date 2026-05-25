from typing import List


class Solution:

    def dfs(self, index, nums, target, total, current_path, result, visited):

        if total == target:

            key = tuple(sorted(current_path))

            if key not in visited:
                visited.add(key)
                result.append(current_path[:])

            return

        if total > target:
            return

        if index >= len(nums):
            return

        # include
        current_path.append(nums[index])

        self.dfs(index, nums, target, total + nums[index], current_path, result, visited)

        current_path.pop()

        # exclude
        self.dfs(index + 1, nums, target, total, current_path, result, visited)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        visited = set()

        self.dfs(0, nums, target, 0, [], result, visited)

        return result